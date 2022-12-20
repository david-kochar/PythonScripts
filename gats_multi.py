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
    
    source_df.rename(columns={source_df.columns[0]: 'statisticalYearMonth'}, inplace = True)
    
    source_df['year_month_length'] = source_df.iloc[:, 0].map(str).apply(len)
    
    source_df.loc[source_df['year_month_length'] == 4, 'statisticalYearMonth'] = source_df['statisticalYearMonth'] + '01'
    
    source_df = source_df.drop('year_month_length', axis = 1)
    
    return source_df

#Create dict to add to response json
def assemble_response_dict(df):
    
    #get max year_and_month for state value
    max_year_and_month = df['statisticalYearMonth'].astype(int).max()
    max_year_and_month = str(max_year_and_month)
    
    #create dict from dataframe for inserts
    inserts = df.to_dict('records')
    
    response_dict = {
        "state" : max_year_and_month,
        "insert" : inserts,
        "primary_key" : ["statisticalYearMonth"]
    }   
    
    return response_dict

def handler(api_key):
    
    #request_json = req.get_json()
    api_key = api_key #request_json['secrets']['apiKey']

    urls = ["https://apps.fas.usda.gov/OpenData/api/gats/census/data/exports/dataReleaseDates",
            "https://apps.fas.usda.gov/OpenData/api/gats/census/data/imports/dataReleaseDates",
            "https://apps.fas.usda.gov/OpenData/api/gats/UNTrade/data/exports/dataReleaseDates",
            "https://apps.fas.usda.gov/OpenData/api/gats/UNTrade/data/imports/dataReleaseDates"]
    
    #Initialize dict with empty keys to collect json response
    
    response_json = {
        "state" : {},
        "insert" : {},
        "schema" : {},
        "hasMore" : False
    }   
    
    for url in urls:
        
        #derive table name from url
        table_name = url.split("/", 6)[-1].replace("/", "_").lower()
    
        #Invoke API request function
        response_text = make_request(url, api_key)
        
        #Invoke dataframe creation function
        response_dataframe = create_dataframe(response_text)
        
        #Invoke dict assembly function and append entity values to response_json
        entity_values = assemble_response_dict(response_dataframe)
        
        response_json["state"][table_name] = entity_values["state"]
        response_json["insert"][table_name] = entity_values["insert"]
        response_json["schema"][table_name] = {"primary_key": entity_values["primary_key"]}
        
    return response_json

print(handler("2d229880-cae3-4b71-ba65-d7d95e7748b5"))