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
    
    request_json = req.get_json()
    api_key = request_json['secrets']['apiKey']
    if req['state']:
        year = req['state']['nass']
    else:
        year = '2014'
        
    current_year = datetime.now().year
    
    if int(year) < current_year:
        has_more = True
    else:
        has_more = False
    
    #Eligibile State FIPS Codes. May require periodic maintenance
    state_fips_codes = ['01', '02', '04', '05', '06', '08', '09', '10', '11', '12', 
                        '13', '15', '16', '17', '18', '19', '20', '21', '22', '23', 
                        '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', 
                        '34', '35', '36', '37', '38', '39', '40', '41', '42', '72', 
                        '44', '45', '46', '47', '48', '49', '50', '51', '78', '53', 
                        '54', '55', '56']
    
    inserts = []
    
    for i in state_fips_codes:
            
        url = f"http://quickstats.nass.usda.gov/api/api_GET/?key={api_key}&agg_level_desc=STATE&group_desc=VEGETABLES&group_desc=FRUIT%20%26%20TREE%20NUTS&freq_desc=WEEKLY&year={year}&state_fips_code={i}&format=csv"
        
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
                
            inserts.append(entity_values["insert"])
    
    if has_more:
        next_year = str(int(year) + 1)
    else:
        next_year = year
    
    response_json = {
        "state" : {"nass": next_year},
        "insert" : {"nass": [val for sublist in inserts for val in sublist]},
        "schema" : {"nass" : {"primary_key" : ["sha1_hash"]}},
        "hasMore" : has_more
    } 
    
    return response_json