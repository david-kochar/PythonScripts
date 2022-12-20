import requests
import pandas as pd
import hashlib
from datetime import datetime
from dateutil.relativedelta import relativedelta
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
    
    source_df["date"] = source_df["date"].apply(str)
    source_df["hS10Code"] = source_df["hS10Code"].apply(str)

    #collect columns that uniquely identify a record to hash
    hash_columns = ["date", 
                    "hS10Code", 
                    "countryCode"]
    
    source_df['sha1_hash'] = pd.DataFrame(source_df[hash_columns].values.sum(axis=1))[0].str.encode('utf-8').apply(lambda x: (hashlib.sha1(x).hexdigest().upper()))

    source_df = source_df.fillna('')
    
    return source_df

#Create dict to add to response json
def assemble_response_dict(df):
    
    #create dict from dataframe for inserts
    inserts = df.to_dict('records')  
    
    return inserts

def handler(req):
    
    request_json = req #req.get_json()
    api_key = request_json['secrets']['apiKey']
    
    if request_json['state']:
        year_month = max(request_json['state'].values())
    else:
        year_month = "201701" #default start month for initial load
        
    year = year_month[0:4]
    month = year_month[4:6].lstrip('0')
    
    current_year_and_month = str(datetime.now().year) + str(datetime.now().month)
    
    #Create 2 month offset lag relative to current month as data may not through current month
    current_year_and_month_offset = (datetime.strptime(current_year_and_month, '%Y%m').date() + relativedelta(months = -2)).strftime("%Y%m")
    
    if int(year_month) < int(current_year_and_month_offset):
        has_more = True
    else:
        has_more = False

    urls = ["https://apps.fas.usda.gov/OpenData/api/gats/censusImports"
            ,"https://apps.fas.usda.gov/OpenData/api/gats/censusExports"
            ,"https://apps.fas.usda.gov/OpenData/api/gats/censusReExports"
            ,"https://apps.fas.usda.gov/OpenData/api/gats/customsDistrictExports"
            ,"https://apps.fas.usda.gov/OpenData/api/gats/customsDistrictImports"
            ,"https://apps.fas.usda.gov/OpenData/api/gats/customsDistrictReExports"
            ]
    
    partner_codes = ["A1", "Z1", "CH"]
    
    #Initialize dict to collect json response
    response_json = {
        "insert" : {},
        "schema" : {}
    }
    
    #Initialize list to collect API url request responses
    url_responses = []
    
    for url in urls:
        
        #derive table name from url
        table_name = url.split("/", 6)[-1].replace("/", "_").lower()
        
        for partner_code in partner_codes:
            
            request_url = ""
            request_url = url + "/partnerCode/" + partner_code + "/year/" + year + "/month/" + month
        
            #Invoke API request function
            response_text = make_request(request_url, api_key)
            
            #if empty response, capture request url
            if response_text == None or len(response_text) == 0:              
                url_responses.append({"empty_requests" : [{"request_url" : request_url}]})
            #if response, invoke helper functions
            else:
                #Invoke dataframe creation function
                response_dataframe = create_dataframe(response_text)
                
                #Invoke dict assembly function and append entity values to response_json
                entity_values = assemble_response_dict(response_dataframe)
                
                url_responses.append({table_name : entity_values})
    
    if has_more:
        next_year_month = (datetime.strptime(year_month, '%Y%m').date() + relativedelta(months = 1)).strftime("%Y%m")
    else:
        next_year_month = year_month
    
    #Combine entity inserts
    inserts = {
            k: [val for sublist in [d[k] for d in url_responses if k in d] for val in sublist]
            for k in set().union(*url_responses)
         }
    
    response_json["insert"] = inserts
    
    response_json["hasMore"] = has_more
    
    entities = list(response_json["insert"].keys())

    states = dict((i, next_year_month) for i in entities)
    
    schemas = {i: ({"primary_key": ["sha1_hash"]} if i != "empty_requests" else {"primary_key": ["request_url"]} ) for i in entities}
    
    response_json["state"] = states
    
    response_json["schema"] = schemas
    
    return response_json

with open('gats_log.txt', 'w') as f:
    f.write(str(handler({
    "secrets": {"apiKey": "2d229880-cae3-4b71-ba65-d7d95e7748b5"},
	"state" : {}
})))