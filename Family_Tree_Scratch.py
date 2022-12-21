import requests
from requests.auth import HTTPBasicAuth
import json

def get_credentials(url, client_id, client_secret):
    
    authorization =  HTTPBasicAuth(client_id, client_secret)
    
    response = requests.get(url, auth = authorization, headers = {"content-type":"application/json"})
    
    response_json = json.loads(response.text)
    
    access_token = response_json["access_token"]
    
    return access_token

def make_request(url, access_token):
    
    headers = {"Content-Type": "application/json" , "Authorization": f"bearer {access_token}"}
    
    try:
        response = requests.get(url, headers = headers)
        print(response.status_code)
        if response.status_code == 200:
            return json.loads(response.text)
        if response.status_code == 404 or response.status_code == 400:
            return None
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)

print(get_credentials("https://api.domo.com/oauth/token?grant_type=client_credentials&scope=data", 
                                        "93f3c045-4bbb-4b48-a578-d67db7382383",
                                        "7f49b3493c16f8fef90579a35c801216d0093904987d7aeaa941c829ab80b086"))

print(
      make_request(
      "https://api.domo.com/v1/datasets/bc653162-0fe6-450a-b508-66acc2dd88b4",
      get_credentials("https://api.domo.com/oauth/token?grant_type=client_credentials&scope=data", 
                                        "93f3c045-4bbb-4b48-a578-d67db7382383",
                                        "7f49b3493c16f8fef90579a35c801216d0093904987d7aeaa941c829ab80b086")
          )
      )

