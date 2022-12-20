import requests
import pandas as pd
import json

#Make API request
def make_request(url, api_key):
    
    headers = {"Accept":"application/json", "API_KEY": api_key}
    
    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return json.loads(response.text)
        if response.status_code == 400:
            return None
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)

#Transform API request to Dataframe for manipulation
def create_dataframe(response_json):
    
    source_df = pd.DataFrame.from_dict(response_json)
    
    return source_df

#Create expected JSON response format
def assemble_response_json(df):
    
    #get max year_and_month for state value
    max_unit_of_measure_id = df['unitOfMeasureId'].astype(int).max()
    max_unit_of_measure_id = str(max_unit_of_measure_id)
    
    #create dict from dataframe for inserts
    inserts = df.to_dict('records')
    
    response_dict = {
        "state" : {"units_of_measure" : max_unit_of_measure_id},
        "insert" : {"units_of_measure" : inserts},
        "schema" : {"units_of_measure" : {"primary_key" : ["unitofmeasureid"]}},
        "hasMore" : False
    }

    response_json = response_dict
    
    return response_json

def handler(req):
    
    request_json = req.get_json()
    api_key = request_json['secrets']['apiKey']

    url = "https://apps.fas.usda.gov/OpenData/api/gats/unitsOfMeasure"
    
    #Invoke API request function
    response_text = make_request(url, api_key)
    
    #Invoke dataframe creation function
    response_dataframe = create_dataframe(response_text)
    
    #Invoke json response assembly function
    response_json = assemble_response_json(response_dataframe)
    
    return response_json