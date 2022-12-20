import requests
import pandas as pd
from datetime import datetime
from itertools import product
import json

#Make API request
def make_request(url, api_key):
    
    headers = {"Accept":"application/json", "API_KEY": api_key}
    
    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return json.loads(response.text)
        if response.status_code == 400:
            return None
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)

#Transform API request to Dataframe for manipulation
def create_dataframe(response_json):
    
    source_df = pd.DataFrame.from_dict(response_json)
    
    return source_df

#Create dict to add to response json
def assemble_response_dict(df):
    
    #create dict from dataframe for inserts
    inserts = df.to_dict('records')  
    
    return inserts

def handler(req):
    
    request_json = req #req.get_json()
    api_key = request_json['secrets']['apiKey']

    urls = ["https://apps.fas.usda.gov/OpenData/api/gats/censusImports",
            "https://apps.fas.usda.gov/OpenData/api/gats/censusExports",
            "https://apps.fas.usda.gov/OpenData/api/gats/censusReExports",
            "https://apps.fas.usda.gov/OpenData/api/gats/customsDistrictExports",
            "https://apps.fas.usda.gov/OpenData/api/gats/customsDistrictImports",
            "https://apps.fas.usda.gov/OpenData/api/gats/customsDistrictReExports"]
    
    partner_codes = ['A1']
    
    years = [str(i) for i in range(2012, datetime.now().year + 1)]
    
    months = [i for i in range(1, 13)]
    
    years_partners = []
    
    for i, j in product(years, partner_codes):
        years_partners.append(i + j)
    
    last_year_partner = years_partners[-1]
    
    #Initialize dict with empty keys to collect json response
    response_json = {
        "state" : {},
        "insert" : {},
        "schema" : {}
    }
    
    for url in urls:
        
        #derive table name from url
        table_name = url.split("/", 6)[-1].replace("/", "_").lower()
        
        if request_json['state']:
            year_partner = request_json['state'][table_name]
        #Initial state will be 2012 and first partner code in eligible code list
        else:
            year_partner = '2012A1'
            
        year = year_partner[0:4]
        partner_code = year_partner[4:6]
        
        inserts = []
        
        for month in months:
            
            url = url + f"/partnerCode/{partner_code}/year/{year}/month/{month}"
            print(url)
                
            #Invoke API request function
            response = make_request(url, api_key)
                    
            #if empty response, continue to next iteration
            if response == None:
                continue
            else:
                #Invoke dataframe creation function
                response_dataframe = create_dataframe(response)
                        
                #Invoke dict assembly function and append entity values to response_json
                entity_values = assemble_response_dict(response_dataframe)
                
                inserts.append(entity_values)
                
        #if partner code is the last in the arrary, update state with next partner code in array
        if year_partner != last_year_partner:
            next_year_partner = years_partners[years_partners.index(year_partner) + 1]
        else:
            next_year_partner = year_partner
                        
        response_json["state"][table_name] = next_year_partner
        response_json["insert"][table_name] = [val for sublist in inserts for val in sublist]
        response_json["schema"][table_name] = {"primary_key": ["date"]}
        
    if year_partner != last_year_partner:
        has_more = True
    else:
        has_more = False
        
    response_json["hasMore"] = has_more
    
    return response_json

handler({
    "secrets": {"apiKey": "2d229880-cae3-4b71-ba65-d7d95e7748b5"},
    "state" : {}
})