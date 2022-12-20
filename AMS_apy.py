import requests
from requests.auth import HTTPBasicAuth

#requests.get('https://marsapi.ams.usda.gov/services/v1.2/reports', auth=HTTPBasicAuth('api_key','pEhHNZ2t9pmu+08YlMxQWVnnguIft0MO'))

def make_request(url, api_key):
    
    response = requests.get(url, auth=HTTPBasicAuth('api_key', api_key))
    
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)
    else:
        return response.text
    
make_request("https://marsapi.ams.usda.gov/services/v1.2/reports/1234", "pEhHNZ2t9pmu+08YlMxQWVnnguIft0MO")