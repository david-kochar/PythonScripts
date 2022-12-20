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
    source_df["begin_code"] = source_df["begin_code"].apply(lambda x: str(x).zfill(2)) #pad leading zero
    source_df["end_code"] = source_df["end_code"].apply(lambda x: str(x).zfill(2)) #pad leading zero
    
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
    
    #create dict from dataframe for inserts
    inserts = df.to_dict('records')
    
    return inserts

def handler(req):
    
    request_json = req #.get_json()
    api_key = request_json['secrets']['apiKey']
    
    #create arrary of years and week numbers combinations to use for state
    years_and_week_nums = pd.date_range(start='01/01/2014', end=str(datetime.now().date()), 
                          freq='W').strftime("%Y%W").tolist()
        
    #add 1 to each year and week combination
    years_and_week_nums = [str(int(i) + 1) for i in years_and_week_nums]
    
    #Ensure combinations are ordered so state will be reliable    
    years_and_week_nums.sort()
    
    if request_json["state"]:
        year_week = request_json["state"]["year_week"]
    else:
        year_week = years_and_week_nums[0] #default for initial load
    
    year = str(year_week[0:4])
    week_num = str(year_week[4:6])
    
    #Declare has_more so we make follow-up calls until last state is reached
    if year_week != years_and_week_nums[-1]:
        has_more = True
    else:
        has_more = False
    
    #Initialize dict to collect json response
    response_json = {
        "insert" : {},
        "schema" : {},
        "state" : {}
    }
            
    url = f"http://quickstats.nass.usda.gov/api/api_GET/?key={api_key}&agg_level_desc=STATE&group_desc=FRUIT%20%26%20TREE%20NUTS&freq_desc=ANNUAL&year={year}&begin_code={week_num}&format=csv"
    
    #Invoke API request function
    response = make_request(url, api_key)

    #if empty response, capture metadata
    if (not response):
        response_json["insert"] = {"empty_requests" : [{"request_url" : url, "year_week" : year_week}]}
        response_json["schema"]["empty_requests"] = {"primary_key": ["year_week"]}
    #if response, invoke helper functions
    else:
        #Invoke dataframe creation function
        response_dataframe = create_dataframe(response)
            
        #Invoke dict assembly function and append entity values to response_json
        entity_values = assemble_response_dict(response_dataframe)
            
        response_json["insert"] = {"nass" : entity_values}
        response_json["schema"]["nass"] = {"primary_key": ["sha1_hash"]}
    
    if has_more:
        next_year_week = years_and_week_nums[years_and_week_nums.index(year_week) + 1]
    else:
        next_year_week = year_week
    
    response_json["hasMore"] = has_more
    
    #increment state
    response_json["state"]["year_week"] = next_year_week
    
    return response_json

with open('nass_log.txt', 'w') as f:
    f.write(str(handler({
    "secrets": {"apiKey": "6FCFC223-607E-3154-A6FB-CBB22663B3F2"},
	"state" : {}
})))