import requests
import pandas as pd
import io
import hashlib
from datetime import datetime

def make_request(url, api_key):
    
    try:
        response = requests.get(url, headers = {"content-type":"text/html", "charset":"utf-8"})
        if response.status_code == 200:
            return response.text
        if response.status_code == 400:
            return None
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)

#Transform API request to Dataframe for manipulation
def create_dataframe(response):
    
    source_df = pd.read_csv(io.StringIO(response), sep = ',', index_col = False)
    
    source_df["state_fips_code"] = source_df["state_fips_code"].apply(lambda x: str(x).zfill(2)) #pad leading zero
    source_df["begin_code"] = source_df["begin_code"].apply(str)
    source_df["end_code"] = source_df["end_code"].apply(str)
    
    #collect columns that uniquely identify a record to hash
    hash_columns = ["group_desc", 
                    "commodity_desc", 
                    "class_desc", 
                    "prodn_practice_desc", 
                    "util_practice_desc", 
                    "statisticcat_desc", 
                    "unit_desc",
                    "state_fips_code",
                    "begin_code",
                    "end_code"]
    
    #create sha1_hash for unique identifier
    source_df['sha1_hash'] = pd.DataFrame(source_df[hash_columns].values.sum(axis=1))[0].str.encode('utf-8').apply(lambda x: (hashlib.sha1(x).hexdigest().upper()))

    source_df = source_df.fillna('')
    
    return source_df

#Create dict to add to response json
def assemble_response_dict(df):
    
    #get max week_ending for state value
    max_week_ending = df['week_ending'].max()
    
    #create dict from dataframe for inserts
    inserts = df.to_dict('records')
    
    response_dict = {
        "state" : max_week_ending,
        "insert" : inserts
    }
    
    return response_dict

def handler(req):
    
    #request_json = req.get_json()
    api_key = req#request_json['secrets']['apiKey']
    
    #Define rolling begin date to pass to API.
    rolling_year_begin = datetime.now().year - 8
    
    #Define rolling end date to pass to API. Rolling period end is current year
    rolling_year_end = datetime.now().year + 1
    
    years = range(rolling_year_begin, rolling_year_end)
    
    #Eligibile State FIPS Codes. May require period maintenance
    state_fips_codes = ['01', '02', '04', '05', '06', '08', '09', '10', '11', '12', 
                        '13', '15', '16', '17', '18', '19', '20', '21', '22', '23', 
                        '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', 
                        '34', '35', '36', '37', '38', '39', '40', '41', '42', '72', 
                        '44', '45', '46', '47', '48', '49', '50', '51', '78', '53', 
                        '54', '55', '56']
    
    max_week_ending = []
    
    inserts = []
    
    for j in years:
    
        for i in state_fips_codes:
            
            url = f"http://quickstats.nass.usda.gov/api/api_GET/?key={api_key}&agg_level_desc=STATE&group_desc=VEGETABLES&group_desc=FRUIT%20%26%20TREE%20NUTS&freq_desc=WEEKLY&year={j}&state_fips_code={i}&format=csv"
        
            #Invoke API request function
            response = make_request(url, api_key)
    
            #if empty response, continue to next iteration
            if response == None:
                continue
            #if response, invoke helper functions
            else:
                #Invoke dataframe creation function
                response_dataframe = create_dataframe(response)
                
                #Invoke dict assembly function and append entity values to response_json
                entity_values = assemble_response_dict(response_dataframe)
                
                max_week_ending.append(entity_values["state"])
                inserts.append(entity_values["insert"])
    
    max_week_ending = str(max(max_week_ending))
    
    response_json = {
        "state" : {"nass": max_week_ending},
        "insert" : {"nass": [val for sublist in inserts for val in sublist]},
        "schema" : {"nass" : {"primary_key" : ["sha1_hash"]}},
        "hasMore" : False
    } 
    
    return response_json

with open('nass_log.txt', 'w') as f:
    f.write(str(handler("6FCFC223-607E-3154-A6FB-CBB22663B3F2")))