import requests
import pandas as pd
import io
import hashlib
#from datetime import datetime

def make_request(url, api_key):
    
    response = requests.get(url, headers = {"content-type":"text/html", "charset":"utf-8"})
    
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)
    else:
        return response.text

#Transform API request to Dataframe for manipulation
def create_dataframe(response_text):
    
    source_df = pd.read_csv(io.StringIO(response_text), sep = ',', index_col = False)
    
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
    
    request_json = req.get_json()
    api_key = request_json['secrets']['apiKey']
    
    #Define rolling begin date to pass to API. Rolling period begin is 2 years prior to beginning of current year
    #rolling_year_begin = str(datetime.now().year - 2)
    
    state_fips_codes = ['05', '08']
    
    max_week_ending = []
    
    inserts = []
    
    for i in state_fips_codes:
        
        state_code = str(i)
        
        url = f"http://quickstats.nass.usda.gov/api/api_GET/?key={api_key}&agg_level_desc=STATE&group_desc=VEGETABLES&group_desc=FRUIT%20%26%20TREE%20NUTS&freq_desc=WEEKLY&year=2022&state_fips_code={state_code}&format=csv"
    
        #Invoke API request function
        response_text = make_request(url, api_key)
        
        #Invoke dataframe creation function
        response_dataframe = create_dataframe(response_text)
        
        #Invoke dict assembly function and append entity values to response_json
        entity_values = assemble_response_dict(response_dataframe)
        
        max_week_ending.append(entity_values["state"])
        inserts.append(entity_values["insert"])
    
    max_week_ending = str(max(max_week_ending))
    
    response_json = {
        "state" : {"nass": max_week_ending},
        "insert" : {"nass": inserts[0]},
        "schema" : {"nass" : {"primary_key" : ["sha1_hash"]}},
        "hasMore" : False
    } 
    
    return response_json