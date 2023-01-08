import requests
import json
import pandas as pd
import datetime
from datetime import timedelta
import time
import hashlib

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
            json_response = json.loads(response.text)
            #Add individual_id to response
            if "Relationships" in url:
                individual_id = url.split("/")[6]
                json_response["individual_id"] = individual_id
            else:
                json_response
            return json_response
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
    source_df_flat.columns = source_df_flat.columns.str.replace(".", "_", regex = False)
    
    return source_df_flat

def assemble_response_dict(df):
    #Creates dictionary from dataframe to add to response json inserts
    
    #create dict from dataframe for inserts
    inserts = df.to_dict('records')  
    
    return inserts

def handler(req):
    #Is entry point for function. Sets variables and executes defined functions
    
    #Create numeric timestamp for state with -1 day offset 
    current_date_offset = (datetime.datetime.now() - timedelta(days = 1)).strftime("%Y%m%d")
    current_ts_offset = f"{current_date_offset}0000"
    
    request_json = req #.get_json()
    app_key = request_json["secrets"]["AppKey"]
    app_password = request_json["secrets"]["AppPassword"]
    app_user_password = request_json["secrets"]["AppUserPassword"]
    
    #fetch credentials for subsequent calls
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
        #Get all Individuals changed on or after a given date
        changed_individuals_url = "https://access.blueberry.org/api/v1/Individuals/ChangedSince/{yyyymmdd_param}/{hhmm_param}/{page_num_param}"
    else:
        #Get all individuals
        changed_individuals_url = "https://access.blueberry.org/api/v1/Individuals/Members/All/{page_num_param}"
        
    if request_json["state"] and "individual_ids" in request_json["state"].keys():
        individual_ids = request_json["state"]["individual_ids"]
    else:
        if "ChangedSince" in changed_individuals_url:
            changed_individuals_json = paginate(changed_individuals_url, credentials, changed_since = changed_since)
            individual_ids = list(set([item for sublist in [i["dataList"] for i in changed_individuals_json] for item in sublist]))
        else:
            changed_individuals_json = paginate(changed_individuals_url, credentials)
            individual_ids = list(set([item["id"] for sublist in [i["dataList"] for i in changed_individuals_json] for item in sublist]))
            
    individual_ids.sort()
    
    if request_json["state"] and "individual_id" in request_json["state"].keys():
        individual_id = request_json["state"]["individual_id"]
    else:
        if individual_ids:
            individual_id = individual_ids[0]
        else:
            individual_id = "" #Assign empty individual_id if no individuals have updates
        
    if individual_ids and individual_id in individual_ids and individual_id != individual_ids[-1]:
        has_more = True
    else:
        has_more = False
    
    urls = [
        f"https://access.blueberry.org/api/v1/Individuals/Profile/{individual_id}/1",
        f"https://access.blueberry.org/api/v1/Individuals/{individual_id}/Relationships/1"
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
                            "id": hashlib.sha1((url + changed_since).encode('utf-8')).hexdigest().upper(),
                            "request_url": request_url,
                            "individual_id": individual_id,
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
        response_json["state"]["individual_ids"] = individual_ids
        next_individual_id = individual_ids[individual_ids.index(individual_id) + 1]
        response_json["state"]["individual_id"] = next_individual_id
    else:
        response_json["state"]["changed_since"] = current_ts_offset
    
    return response_json

with open('impexium_individuals_fivetran_response_test.txt', 'w') as f:
    f.write(str(handler({
        "secrets": {"AppKey" : "HNONuU8D440tCJnp", "AppPassword" : "HNONuU8D440tCJnp", "AppUserPassword" : "1ofuTaSwlqugebosU791!"},
     	"state" : {}
    })))