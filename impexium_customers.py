import requests
import json
import pandas as pd
import datetime
from datetime import timedelta
import time

def get_credentials(access_body, auth_body):
    
    #Get Web API End Point and Access Token
    access_url = "https://public.impexium.com/Api/v1/WebApiUrl"
    
    headers = {"Content-Type": "application/json; charset=utf-8"}
     
    access_response = requests.post(access_url, 
                                    headers = headers, 
                                    json = access_body).json()
    
    #Authenticate App, and get app token and user token (SSO Token)
    
    auth_url = access_response["uri"]
    
    auth_token = access_response["accessToken"]
    
    headers = {"Content-Type": "application/json", "AccessToken": auth_token}
    
    auth_response = requests.post(auth_url, 
                                  headers = headers, 
                                  json = auth_body).json()
    
    return auth_response

def make_request(url, credentials):
    
    app_token = credentials["appToken"]
    
    user_token = credentials["userToken"]
    
    headers = {"Content-Type": "application/json", "UserToken" : user_token, "AppToken" : app_token}
    
    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return json.loads(response.text)
        if response.status_code == 404 or response.status_code == 400:
            return None
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)
    
def paginate(url, credentials, **kwargs):
    #Paginate requests through an indeterminate number of pages
    
    page_num = 1
    
    responses = []
    
    while True:
        if kwargs.get("changed_since"):
            yyyymmdd = kwargs["changed_since"][0:8]
            hhmm = kwargs["changed_since"][-4:]
            request_url = url.format(yyyymmdd_param = yyyymmdd, hhmm_param = hhmm, page_num_param = page_num)
        elif (not kwargs.get("changed_since")) and kwargs.get("org_id"):
            org_id = kwargs["org_id"]
            request_url = url.format(org_id_param = org_id, page_num_param = page_num)          
        else:
            request_url = url.format(page_num_param = page_num)
            
        response_json = make_request(request_url, credentials)
        
        #Break out if no response
        if (not response_json):
            break
        responses.append(response_json)
        
        #if response, increment page number to paginate
        page_num += 1

        #Pause for 1 second to avoid API limitations
        time.sleep(1)
    
    return responses

def create_dataframe(response_json):
    #Transform API request to Dataframe for manipulation
    
    source_df = pd.DataFrame.from_dict(response_json)
    
    json_struct = json.loads(source_df.to_json(orient="records"))
    
    #unnest json
    source_df_flat = pd.json_normalize(json_struct)
    
    #remove prefix from dataframe column headers
    source_df_flat.columns = source_df_flat.columns.str.removeprefix("dataList.")
    source_df_flat.columns = source_df_flat.columns.str.removeprefix("relatedToCustomer.")
    
    return source_df_flat

def assemble_response_dict(df):
    #Creates dictionary from dataframe to add to response json inserts
    
    #create dict from dataframe for inserts
    inserts = df.to_dict('records')  
    
    return inserts

def handler(req):
    #Is entry point for function. Sets variables and executes defined functions
    
    #Create numeric timestamp for state with -30 day offset 
    current_date_offset = (datetime.datetime.now() - timedelta(days = 30)).strftime("%Y%m%d")
    current_ts_offset = f"{current_date_offset}0000"
    
    request_json = req #req.get_json()
    app_key = request_json["secrets"]["AppKey"]
    app_password = request_json["secrets"]["AppPassword"]
    app_user_password = request_json["secrets"]["AppUserPassword"]
    
    credentials = get_credentials(
        {"AppName": "SnowflakeApiProd", "AppKey": app_key},
        {
            "AppId": "SnowflakeApiProd",
            "AppPassword": app_password,
            "AppUserEmail": "Snowflake_api@integration.com",
            "AppUserPassword": app_user_password,
        },
    )
    
    if request_json["state"] and "changed_since" in request_json["state"].keys():
        changed_since = request_json["state"]["changed_since"]
    else:
        changed_since = "175301010000" #Min formatted timestamp
        
    #Get all Orgs changed on or after a given date. Initial sync will fetch all orgs
    changed_orgs_url = "https://access.blueberry.org/api/v1/Organizations/ChangedSince/{yyyymmdd_param}/{hhmm_param}/{page_num_param}"
    
    changed_orgs_json = paginate(changed_orgs_url, credentials, changed_since = changed_since)
    
    #Org IDs reside in DataList element, and the arrarys need to be flattened
    org_ids = list(set([item for sublist in [i["dataList"] for i in changed_orgs_json] for item in sublist]))
    
    org_ids.sort()
    
    if request_json["state"] and "org_id" in request_json["state"].keys():
        org_id = request_json["state"]["org_id"]
    else:
        org_id = org_ids[0]
        
    if org_id != org_ids[-1]:
        has_more = True
    else:
        has_more = False
    
    urls = [
        f"https://access.blueberry.org/api/v1/Organizations/Profile/{org_id}/1",
        f"https://access.blueberry.org/api/v1/Organizations/{org_id}/Relationships/1",
        f"https://access.blueberry.org/api/v1/Organizations/{org_id}/Services"
        #,f"https://access.blueberry.org/api/v1/Organizations/{org_id}/Subscriptions/1"
    ]
    
    #Initialize dict to collect json response
    response_json = {
        "insert" : {},
        "schema" : {},
        "state" : {}
    }
    
    #Initialize list to collect API url request responses
    url_responses = []
    
    for url in urls:
        
        #derive table name from url
        table_name = [i for i in url.split("/", 6)[-1].split("/") if i and i[0].isupper()][0].lower()
        
        request_url = url
        
        request_response = make_request(request_url, credentials)
        
        #Pause for 1 seconds to avoid API limitations
        time.sleep(1)
        
        #if empty response, capture metadata
        if (not request_response):              
            url_responses.append(
                {
                    "empty_requests": [
                        {
                            "id": f"{org_id}-{changed_since}",
                            "request_url": request_url,
                            "org_id": org_id,
                            "changed_since": changed_since,
                        }
                    ]
                }
            )
            
        #if response, invoke helper functions
        else:
            response_dataframe = create_dataframe(request_response)
            
            entity_values = assemble_response_dict(response_dataframe)
            
            url_responses.append({table_name : entity_values})
        
    #Combine entity inserts
    inserts = {
        k : [val for sublist in [d[k] for d in url_responses if k in d] for val in sublist] for k in set().union(*url_responses)
    }
    
    response_json["insert"] = inserts
    
    response_json["hasMore"] = has_more
    
    #get array of entity names
    entities = list(response_json["insert"].keys())
    
    #apply schemas to entity names
    schemas = {i: ({"primary_key": ["id"]} if i not in ["services", "subscriptions"] else {"primary_key": ["code"]}) for i in entities}
    
    response_json["schema"] = schemas
    
    #Update state
    if has_more:
        next_org_id = org_ids[org_ids.index(org_id) + 1]
        response_json["state"]["org_id"] = next_org_id
        response_json["state"]["changed_since"] = changed_since
    else:
        response_json["state"]["changed_since"] = current_ts_offset
    
    return response_json

# with open('impexium_orgs.txt', 'w') as f:
#     f.write(str(handler({
#         "secrets": {"AppKey" : "HNONuU8D440tCJnp", "AppPassword" : "HNONuU8D440tCJnp", "AppUserPassword" : "1ofuTaSwlqugebosU791!"},
#     	"state" : {}
#     })))
