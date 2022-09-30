import requests
import pandas as pd
import io
import hashlib
from datetime import datetime

#Make API request
def make_request(api_key):
    
    #Define rolling begin date to pass to API. Rolling period begin is 3 years prior to beginning of current year
    rolling_period_begin = str(datetime.now().year - 3) + '01'

    url = f"https://www1.tdmlogin.com/tdm/api/api.asp?key={api_key}&lang=EN&flow=B&includeDesc=Y&periodBegin=202206&periodEnd=209912&encoding=UTF8&levelDetail=8"
    
    response = requests.get(url, headers={"content-type":"application/json"}).content
    
    return response

#Transform API request to Dataframe for manipulation
def create_dataframe(response):
    
    source_df = pd.read_csv(io.StringIO(response.decode('utf-8')), index_col=False)
    
    source_df['FLOW'] = source_df['FLOW'].apply(str)
    source_df['CTY_RPT'] = source_df['CTY_RPT'].apply(str)
    source_df['REPORTER'] = source_df['REPORTER'].apply(str)
    source_df['CTY_PTN'] = source_df['CTY_PTN'].apply(str)
    source_df['PARTNER'] = source_df['PARTNER'].apply(str)
    source_df['COMMODITY'] = source_df['COMMODITY'].apply(str)
    source_df['YEAR'] = source_df['YEAR'].apply(str)
    source_df['MONTH'] = source_df['MONTH'].apply(lambda x: str(x).zfill(2))
    source_df['YEAR_AND_MONTH'] = source_df['YEAR'] + source_df['MONTH']
    source_df['REQUEST_TIMESTAMP'] = datetime.utcnow()
    source_df['REQUEST_TIMESTAMP'] = source_df['REQUEST_TIMESTAMP'].apply(str)
    
    hashed_df = source_df
    
    #collect columns that uniquely identify a record to hash
    hash_columns = ['FLOW', 'CTY_RPT', 'REPORTER', 'CTY_PTN', 'PARTNER', 'COMMODITY', 'YEAR_AND_MONTH']
    
    #create sha1_hash for unique identifier
    hashed_df['sha1_hash'] = pd.DataFrame(source_df[hash_columns].values.sum(axis=1))[0].str.encode('utf-8').apply(lambda x: (hashlib.sha1(x).hexdigest().upper()))
    
    return hashed_df

#Create expected JSON response format
def assemble_response_json(df):
    
    #get max year_and_month for state value
    max_year_and_month = df['YEAR_AND_MONTH'].astype(int).max()
    
    #create dict from dataframe for inserts
    inserts = df.to_dict('records')
    
    response_json = {
        "state": {
            "tdm": max_year_and_month
        },
        "schema" : {
            "tdm" : {
                "primary_key" : ["sha1_hash"]
            }
        },
        "insert": {
            "tdm": inserts
        },
        "hasMore" : False
    }
    
    return response_json

print(assemble_response_json(create_dataframe(make_request('dhhqkfpsbglkrybrhbwtoekdkbtdlfbc'))))