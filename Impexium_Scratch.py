import requests
import json
import pandas as pd
import hashlib

def get_urls(base_url, credentials):
    
    app_token = credentials["appToken"]
    
    user_token = credentials["userToken"]
    
    headers = {"Content-Type": "application/json", "UserToken" : user_token, "AppToken" : app_token}
    
    page_number = 1
    #base_url = "https://access.blueberry.org/api/v1/Organizations/Members/All/"
    urls = []
    
    while True:
        session = requests.Session()
        url = f"{base_url}{page_number}"
        print(url)
        response = session.head(url, headers = headers)
        print(response.status_code)
        if response.status_code != 200:
            break
        urls.append(url)
        page_number += 1
    
    return urls

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
    
    response = requests.get(url, headers = headers)
    
    return json.loads(response.text) #response.text

def create_dataframe(response_json):
    #Transform API request to Dataframe for manipulation
    
    source_df = pd.DataFrame.from_dict(response_json)
    
    source_df["dataList"] = source_df["dataList"].apply(str)
    
    hash_columns = ["dataList"]
    
    source_df['sha1_hash'] = pd.DataFrame(source_df[hash_columns].values.sum(axis=1))[0].str.encode('utf-8').apply(lambda x: (hashlib.sha1(x).hexdigest().upper()))
    
    data_top = source_df.head()
    
    print(data_top)
    
    return source_df

create_dataframe(make_request("https://access.blueberry.org/api/v1/Organizations/Members/All/1", get_credentials({"AppName": "SnowflakeApiProd", "AppKey": "HNONuU8D440tCJnp"},
                    {"AppId":"SnowflakeApiProd",
                    "AppPassword":"HNONuU8D440tCJnp",
                    "AppUserEmail":"Snowflake_api@integration.com",
                    "AppUserPassword":"1ofuTaSwlqugebosU791!"})))

get_urls("https://access.blueberry.org/api/v1/Organizations/Members/All/", get_credentials({"AppName": "SnowflakeApiProd", "AppKey": "HNONuU8D440tCJnp"},
                    {"AppId":"SnowflakeApiProd",
                    "AppPassword":"HNONuU8D440tCJnp",
                    "AppUserEmail":"Snowflake_api@integration.com",
                    "AppUserPassword":"1ofuTaSwlqugebosU791!"}))


# with open('impexium_org_sample.txt', 'w') as f:
#     f.write(str(make_request("https://access.blueberry.org/api/v1/Organizations/Members/All/1", get_credentials({"AppName": "SnowflakeApiProd", "AppKey": "HNONuU8D440tCJnp"},
#                         {"AppId":"SnowflakeApiProd",
#                         "AppPassword":"HNONuU8D440tCJnp",
#                         "AppUserEmail":"Snowflake_api@integration.com",
#                         "AppUserPassword":"1ofuTaSwlqugebosU791!"}))))

