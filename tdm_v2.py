import requests
import pandas as pd
import io
import hashlib
from datetime import datetime
from dateutil.relativedelta import relativedelta

#Make API request
def make_request(url, api_key):
    
    try:
        response = requests.get(url, headers = {"content-type":"application/octet-stream", "charset":"utf-8"})
        if response.status_code == 200:
            return response.text
        if response.status_code == 400:
            return None
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)

#Transform API request to Dataframe for manipulation
def create_dataframe(response_text):
    
    source_df = pd.read_csv(io.StringIO(response_text), sep = ',', index_col = False)
    
    source_df['FLOW'] = source_df['FLOW'].apply(str)
    source_df['CTY_RPT'] = source_df['CTY_RPT'].apply(str)
    source_df['REPORTER'] = source_df['REPORTER'].apply(str)
    source_df['CTY_PTN'] = source_df['CTY_PTN'].apply(str)
    source_df['PARTNER'] = source_df['PARTNER'].apply(str)
    source_df['COMMODITY'] = source_df['COMMODITY'].apply(str)
    source_df['DESCRIPTION'] = source_df['DESCRIPTION'].str.strip()
    source_df['YEAR'] = source_df['YEAR'].apply(str)
    source_df['MONTH'] = source_df['MONTH'].apply(lambda x: str(x).zfill(2)) #pad leading zero to get 2 digit month
    source_df['YEAR_AND_MONTH'] = source_df['YEAR'] + source_df['MONTH']
    source_df['VALUE'] = source_df['VALUE'].apply(float)
    source_df['QTY1'] = source_df['QTY1'].apply(float)
    source_df['UNIT1'] = source_df['UNIT1'].apply(str)
    source_df['QTY2'] = source_df['QTY2'].apply(float)
    source_df['UNIT2'] = source_df['UNIT2'].apply(str)
    source_df['CURRENCY'] = source_df['CURRENCY'].apply(str)
    
    #collect columns that uniquely identify a record to hash
    hash_columns = ['FLOW', 'CTY_RPT', 'REPORTER', 'CTY_PTN', 'PARTNER', 'COMMODITY', 'YEAR_AND_MONTH']
    
    #create sha1_hash for unique identifier
    source_df['SHA1_HASH'] = pd.DataFrame(source_df[hash_columns].values.sum(axis=1))[0].str.encode('utf-8').apply(lambda x: (hashlib.sha1(x).hexdigest().upper()))

    source_df.rename(columns={
        'FLOW': 'flow', 
        'CTY_RPT': 'cty_rpt', 
        'REPORTER': 'reporter', 
        'CTY_PTN': 'cty_ptn', 
        'PARTNER': 'partner', 
        'COMMODITY': 'commodity',
        'DESCRIPTION': 'description',
        'YEAR': 'year',
        'MONTH': 'month',
        'YEAR_AND_MONTH': 'year_and_month',
        'VALUE': 'value',
        'QTY1': 'qty1',
        'UNIT1': 'unit1',
        'QTY2': 'qty2',
        'UNIT2': 'unit2',
        'CURRENCY': 'currency',
        'SHA1_HASH': 'sha1_hash'}, inplace = True)
    
    return source_df

def assemble_response_dict(df):
    #Creates dictionary from dataframe to add to response json inserts
    
    #create dict from dataframe for inserts
    inserts = df.to_dict('records')  
    
    return inserts

def handler(req):
    
    request_json = req#.get_json()
    api_key = request_json['secrets']['apiKey']
    
    #create arrary of months to use for state. Use -2 month offset as API data lags 
    months = pd.date_range('2000-01-01', str(datetime.now().date() + relativedelta(months = -2)), 
                freq='MS').strftime("%Y%m").tolist()
    
    #Ensure combinations are ordered so state will be reliable  
    months.sort()
    
    if request_json["state"]:
        year_month = request_json["state"]["year_month"]
    else:
        year_month = months[0] #default for initial load
    
    #Declare has_more so we make follow-up calls until last state is reached
    if year_month != months[-1]:
        has_more = True
    else:
        has_more = False
    
    #Initialize dict to collect json response
    response_json = {
        "insert" : {},
        "schema" : {},
        "state" : {}
    }

    #API parameters are here: https://docs.google.com/document/d/1kS0qg2QNWffispPBek4xbg99KdZrYTe6/edit?usp=sharing&ouid=103569479876314240031&rtpof=true&sd=true
    url = f"https://www1.tdmlogin.com/tdm/api/api.asp?key={api_key}&reporter=US&lang=EN&flow=B&includeDesc=Y&periodBegin={year_month}&periodEnd={year_month}&encoding=UTF8&levelDetail=8&includeUnits=BOTH"
    
    #Invoke API request function
    response = make_request(url, api_key)

    #if empty response, capture metadata
    if (not response):
        response_json["insert"] = {"empty_requests" : [{"request_url" : url, "year_month" : year_month}]}
        response_json["schema"]["empty_requests"] = {"primary_key": ["year_month"]}
    #if response, invoke helper functions
    else:
        #Invoke dataframe creation function
        response_dataframe = create_dataframe(response)
            
        #Invoke dict assembly function and append entity values to response_json
        entity_values = assemble_response_dict(response_dataframe)
            
        response_json["insert"] = {"tdm" : entity_values}
        response_json["schema"]["tdm"] = {"primary_key": ["sha1_hash"]}
    
    if has_more:
        next_year_month = months[months.index(year_month) + 1]
    else:
        next_year_month = year_month
    
    response_json["hasMore"] = has_more
    
    #increment state
    response_json["state"]["year_month"] = next_year_month
    
    return response_json

with open('tdm_log.txt', 'w') as f:
    f.write(str(handler({
    "secrets": {"apiKey": "dhhqkfpsbglkrybrhbwtoekdkbtdlfbc"},
	"state" : {}
})))