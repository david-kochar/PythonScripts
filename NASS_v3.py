import requests
import pandas as pd
import io
import hashlib
import datetime

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
                    "state_fips_code"]
    
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
    
    current_year = (datetime.date.today()).year
    
    #create arrary of years to use for state
    years = [i for i in range (2007, current_year)]
    
    #Ensure year list is ordered so state will be reliable    
    years.sort()
    
    if request_json["state"]:
        year = request_json["state"]["year"]
    else:
        year = years[0] #default for initial load
    
    #Declare has_more so we make follow-up calls until last state is reached
    if year != years[-1]:
        has_more = True
    else:
        has_more = False
    
    #Initialize dict to collect json response
    response_json = {
        "insert" : {},
        "schema" : {},
        "state" : {}
    }
            
    url = f"http://quickstats.nass.usda.gov/api/api_GET/?key={api_key}&source_desc=SURVEY&sector_desc=CROPS&commodity_desc=BLUEBERRIES&agg_level_desc=STATE&group_desc=FRUIT%20%26%20TREE%20NUTS&freq_desc=ANNUAL&year={year}&format=csv"
    
    #Invoke API request function
    response = make_request(url, api_key)

    #if empty response, capture metadata
    if (not response):
        response_json["insert"] = {"empty_requests" : [{"request_url" : url, "year" : year}]}
        response_json["schema"]["empty_requests"] = {"primary_key": ["year"]}
    #if response, invoke helper functions
    else:
        #Invoke dataframe creation function
        response_dataframe = create_dataframe(response)
            
        #Invoke dict assembly function and append entity values to response_json
        entity_values = assemble_response_dict(response_dataframe)
            
        response_json["insert"] = {"nass" : entity_values}
        response_json["schema"]["nass"] = {"primary_key": ["sha1_hash"]}
    
    if has_more:
        next_year = years[years.index(year) + 1]
    else:
        next_year = year
    
    response_json["hasMore"] = has_more
    
    #increment state
    response_json["state"]["year"] = next_year
    
    return response_json

with open('nass_log.txt', 'w') as f:
    f.write(str(handler({
    "secrets": {"apiKey": "6FCFC223-607E-3154-A6FB-CBB22663B3F2"},
	"state" : {}
})))

