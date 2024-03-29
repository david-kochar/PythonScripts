import requests
import pandas as pd
import io
import hashlib
from datetime import datetime

#Make API request
def make_request(url, api_key):
    
    response = requests.get(url, headers = {"content-type":"application/octet-stream", "charset":"utf-8"})
    
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)
    else:
        return response.text

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

#Create expected JSON response format
def assemble_response_json(df):
    
    #get max year_and_month for state value
    max_year_and_month = df['year_and_month'].astype(int).max()
    max_year_and_month = str(max_year_and_month)
    
    #create dict from dataframe for inserts
    inserts = df.to_dict('records')
    
    response_dict = {
        "state" : {"tdm" : max_year_and_month},
        "insert" : {"tdm" : inserts},
        "schema" : {"tdm" : {"primary_key" : ["sha1_hash"]}},
        "hasMore" : False
    }

    response_json = response_dict
    
    return response_json

def handler(req):
    
    request_json = req.get_json()
    api_key = request_json['secrets']['apiKey']

    #Define rolling begin date to pass to API. Rolling period begin is 2 years prior to beginning of current year
    rolling_period_begin = str(datetime.now().year - 2) + '01'
    
    #periodEnd of 209912 is unbounded, to get most recent data
    #API parameters are here: https://docs.google.com/document/d/1kS0qg2QNWffispPBek4xbg99KdZrYTe6/edit?usp=sharing&ouid=103569479876314240031&rtpof=true&sd=true
    url = f"https://www1.tdmlogin.com/tdm/api/api.asp?key={api_key}&reporter=US&lang=EN&flow=B&includeDesc=Y&periodBegin={rolling_period_begin}&periodEnd=209912&encoding=UTF8&levelDetail=8&includeUnits=BOTH"
    
    #Invoke API request function
    response_text = make_request(url, api_key)
    
    #Invoke dataframe creation function
    response_dataframe = create_dataframe(response_text)
    
    #Invoke json response assembly function
    response_json = assemble_response_json(response_dataframe)
    
    return response_json