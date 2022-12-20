import requests
from requests.auth import HTTPBasicAuth
#import pandas as pd
#from pandas import json_normalize 
#import io
import json

def make_request(url, api_key):
    
    response = requests.get(url, auth=HTTPBasicAuth('api_key', api_key), headers = {"content-type":"application/json"})
    
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)
    else:
        return response.text

response_data = json.loads(make_request("https://marsapi.ams.usda.gov/services/v1.2/reports/", "pEhHNZ2t9pmu+08YlMxQWVnnguIft0MO"))


for i in response_data:
    print(i['report_title'])