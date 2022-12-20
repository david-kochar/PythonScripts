import requests
import json
import pandas as pd
import datetime
from datetime import timedelta

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
    
def paginate(url, app_key, app_password, app_user_password):
    
    credentials = get_credentials(
                        {"AppName": "SnowflakeApiProd", "AppKey": app_key}
                        ,         
                        {
                          "AppId" : "SnowflakeApiProd",
                          "AppPassword" : app_password,
                          "AppUserEmail" : "Snowflake_api@integration.com",
                          "AppUserPassword" : app_user_password
                        }
                    )
    
    page_num = 1
    
    responses = []
    
    while True:
        request_url = f"{url}{page_num}"
        response_json = make_request(request_url, credentials)
        if (not response_json):
            break
        responses.append(response_json)
        page_num += 1
    
    return responses
    
def get_org_ids(changed_since, app_key, app_password, app_user_password):
    
    yyyymmdd = changed_since[0:8]
    
    hhmm = changed_since[-4:]
    
    url = f"https://access.blueberry.org/api/v1/Organizations/ChangedSince/{yyyymmdd}/{hhmm}/"
    
    response = paginate(url, app_key, app_password, app_user_password)
    
    return response

def create_dataframe(response_json):
    #Transform API request to Dataframe for manipulation
    
    source_df = pd.DataFrame.from_dict(response_json)
    
    json_struct = json.loads(source_df.to_json(orient="records"))
    
    source_df_flat = pd.json_normalize(json_struct)
    
    source_df_flat.columns = source_df_flat.columns.str.removeprefix("dataList.")
    
    return source_df_flat

def handler(req):
    #Is entry point for function. Sets variables and executes defined functions
    
    #current_ts = (datetime.datetime.now() - timedelta(days = 3)).strftime("%Y%m%d%H%M")
    
    request_json = req #req.get_json()
    app_key = request_json["secrets"]["AppKey"]
    app_password = request_json["secrets"]["AppPassword"]
    app_user_password = request_json["secrets"]["AppUserPassword"]
    
    if request_json["state"]:
        changed_since = request_json["state"]["changed_since"]
    else:
        changed_since = "175301010000" #Min formatted timestamp
        
    #Get all Orgs changed on or after a given date. Initial sync will fetch all orgs
    
    orgs_json = get_org_ids(changed_since, app_key, app_password, app_user_password)
    
    orgs = list(set([item for sublist in [i["dataList"] for i in orgs_json] for item in sublist]))
    
    return orgs
    
    #Get count of Org IDs to use for subsequent requests
    #orgs = [i["id"] for i in d["dataList"]]
        
    # page_num = "1"
    
    # org_id = ""
    
    # base_url = "https://access.blueberry.org/api/v1/Organizations/"
    
    # sub_directories = [f"Profile/{org_id}/{page_num}",
    #                    "/Relationships/",
    #                    "/Certifications/",
    #                    "/Aliases/"]
    
# print(handler({
#     "secrets": {"AppKey" : "HNONuU8D440tCJnp", "AppPassword" : "HNONuU8D440tCJnp", "AppUserPassword" : "1ofuTaSwlqugebosU791!"},
# 	"state" : {}
# }))

with open('impexium_orgs.txt', 'w') as f:
    f.write(str(handler({
        "secrets": {"AppKey" : "HNONuU8D440tCJnp", "AppPassword" : "HNONuU8D440tCJnp", "AppUserPassword" : "1ofuTaSwlqugebosU791!"},
    	"state" : {}
    })))

# print(get_credentials({"AppName": "SnowflakeApiProd", "AppKey": "HNONuU8D440tCJnp"},
#                     {"AppId":"SnowflakeApiProd",
#                     "AppPassword":"HNONuU8D440tCJnp",
#                     "AppUserEmail":"Snowflake_api@integration.com",
#                     "AppUserPassword":"1ofuTaSwlqugebosU791!"}))

# create_dataframe(make_request("https://access.blueberry.org/api/v1/Organizations/Members/All/1", get_credentials({"AppName": "SnowflakeApiProd", "AppKey": "HNONuU8D440tCJnp"},
#                     {"AppId":"SnowflakeApiProd",
#                     "AppPassword":"HNONuU8D440tCJnp",
#                     "AppUserEmail":"Snowflake_api@integration.com",
#                     "AppUserPassword":"1ofuTaSwlqugebosU791!"}))).to_csv("impexium_orgs_flattened.csv")




