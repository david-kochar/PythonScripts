import requests
import pandas as pd
import json

#Make API request
def make_request(url, api_key):
    
    headers = {"Accept":"application/json", "API_KEY": api_key}
    
    response = requests.get(url, headers = headers)
    
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)
    else:
        return json.loads(response.text)

#Transform API request to Dataframe for manipulation
def create_dataframe(response_json):
    
    source_df = pd.DataFrame.from_dict(response_json)
    
    source_df.rename(columns={
        'statisticalYearMonth': 'statistical_year_month', 
        'reporterCode': 'reporter_code', 
        'productType': 'product_type',
        'releaseTimeStamp': 'release_timestamp'
        }, inplace = True)
    
    return source_df

#Create expected JSON response format
def assemble_response_json(df):
    
    #get max year_and_month for state value
    max_year_and_month = df['statistical_year_month'].astype(int).max()
    max_year_and_month = str(max_year_and_month)
    
    #create dict from dataframe for inserts
    inserts = df.to_dict('records')
    
    response_dict = {
        "state" : {"census_imports_release_dates" : max_year_and_month},
        "insert" : {"census_imports_release_dates" : inserts},
        "schema" : {"census_imports_release_dates" : {"primary_key" : ["statistical_year_month"]}},
        "hasMore" : False
    }

    response_json = response_dict
    
    return response_json

def handler(req):
    
    request_json = req.get_json()
    api_key = request_json['secrets']['apiKey']

    url = "https://apps.fas.usda.gov/OpenData/api/gats/census/data/imports/dataReleaseDates"
    
    #Invoke API request function
    response_text = make_request(url, api_key)
    
    #Invoke dataframe creation function
    response_dataframe = create_dataframe(response_text)
    
    #Invoke json response assembly function
    response_json = assemble_response_json(response_dataframe)
    
    return response_json