import requests
import pandas as pd
import hashlib
from datetime import datetime
from dateutil.relativedelta import relativedelta
from itertools import product
import json

def make_request(url, api_key):
    #Makes API request and raises response error when encountered
    
    headers = {"Accept":"application/json", "API_KEY": api_key}
    
    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return json.loads(response.text)
        if response.status_code == 400:
            return None
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)

def create_dataframe(response_json):
    #Transform API request to Dataframe for manipulation
    
    source_df = pd.DataFrame.from_dict(response_json)
    
    source_df["date"] = source_df["date"].apply(str)
    source_df["hS10Code"] = source_df["hS10Code"].apply(str)

    #collect columns that uniquely identify a record to hash
    hash_columns = ["date", 
                    "hS10Code", 
                    "countryCode"]
    
    source_df['sha1_hash'] = pd.DataFrame(source_df[hash_columns].values.sum(axis=1))[0].str.encode('utf-8').apply(lambda x: (hashlib.sha1(x).hexdigest().upper()))

    source_df = source_df.fillna('')

    #Filter to qualifying HS10 codes
    source_df = source_df[source_df['hS10Code'].str.startswith(("0810", "0811", "0813"))]
    
    return source_df

def assemble_response_dict(df):
    #Creates dictionary from dataframe to add to response json inserts
    
    #create dict from dataframe for inserts
    inserts = df.to_dict('records')  
    
    return inserts

def handler(req):
    #Is entry point for function. Sets variables and executes defined functions
    
    request_json = req #req.get_json()
    api_key = request_json["secrets"]["apiKey"]
    
    months_and_partner_codes = []
    
    #create arrary of months to use for state value. Use -2 month offset as API data lags
    if request_json["state"]:
        start_year_month = request_json["state"]["year_month"]
        dt = start_year_month[:4] + "-" + start_year_month[4:6] + "-01"
        months = pd.date_range(dt, str(datetime.now().date() + relativedelta(months = -2)), 
                    freq='MS').strftime("%Y%m").tolist()
    #create years and months array from 2000 for initial sync
    else:
        months = pd.date_range('2000-01-01', str(datetime.now().date() + relativedelta(months = -2)), 
                    freq='MS').strftime("%Y%m").tolist()
    
    #based on GATS country codes
    partner_codes = ["A1", "A2", "AA", "AC", "AE", "AF", "AG", "AJ", "AL", "AM", 
                    "AN", "AO", "AQ", "AR", "AS", "AU", "AV", "AY", "B1", "BA", 
                    "BB", "BC", "BD", "BE", "BF", "BG", "BH", "BK", "BL", "BM", 
                    "BN", "BO", "BP", "BR", "BT", "BU", "BV", "BX", "BY", "CA", 
                    "CB", "CD", "CE", "CF", "CG", "CH", "CI", "CJ", "CK", "CM", 
                    "CN", "CO", "CQ", "CS", "CT", "CU", "CV", "CW", "CY", "CZ", 
                    "D1", "DA", "DJ", "DO", "DR", "E1", "EC", "EG", "EI", "EK", 
                    "EN", "ER", "ES", "ET", "EZ", "F1", "FG", "FI", "FJ", "FK", 
                    "FM", "FO", "FP", "FR", "FS", "G1", "GA", "GB", "GC", "GE", 
                    "GG", "GH", "GI", "GJ", "GL", "GM", "GN", "GP", "GQ", "GR", 
                    "GT", "GV", "GY", "GZ", "HA", "HK", "HM", "HO", "HR", "HU", 
                    "I1", "I2", "IC", "ID", "IN", "IO", "IR", "IS", "IT", "IV", 
                    "IY", "IZ", "JA", "JM", "JO", "KE", "KG", "KN", "KR", "KS", 
                    "KT", "KU", "KV", "KZ", "LA", "LE", "LG", "LH", "LI", "LO", 
                    "LS", "LT", "LU", "LY", "MA", "MB", "MC", "MD", "MF", "MG", 
                    "MH", "MI", "MJ", "MK", "ML", "MN", "MO", "MP", "MQ", "MR", 
                    "MT", "MU", "MV", "MX", "MY", "MZ", "N1", "N2", "N3", "NC", 
                    "NE", "NF", "NG", "NH", "NI", "NL", "NN", "NO", "NP", "NQ", 
                    "NR", "NS", "NT", "NU", "NZ", "OD", "P1", "PA", "PC", "PE", 
                    "PK", "PL", "PM", "PO", "PP", "PQ", "PS", "PU", "QA", "R1", 
                    "RB", "RE", "RM", "RO", "RP", "RQ", "RS", "RW", "S1", "S2", 
                    "SA", "SB", "SE", "SF", "SG", "SH", "SI", "SL", "SM", "SN", 
                    "SO", "SP", "SR", "ST", "SU", "SV", "SW", "SX", "SY", "SZ", 
                    "TD", "TH", "TI", "TK", "TL", "TN", "TO", "TP", "TS", "TT", 
                    "TU", "TV", "TW", "TX", "TZ", "U0", "UC", "UG", "UK", "UP", 
                    "UR", "UV", "UY", "UZ", "V1", "V2", "V4", "V5", "V6", 
                    "V7", "V8", "VC", "VE", "VI", "VM", "VO", "VT", "W2", "W5", 
                    "W6", "W7", "WA", "WE", "WF", "WI", "WQ", "WS", "WZ", "X4", 
                    "X6", "X8", "X9", "Y1", "Y2", "Y3", "Y7", "Y9", "YE", "YM", 
                    "YO", "YS", "YU", "Z1", "Z2", "Z5", "Z6", "Z7", "Z8", "ZA", 
                    "ZB", "ZI"]
    
    #create arrary of months and partnery code combinations to use for state
    for i, j in product(months, partner_codes):
        months_and_partner_codes.append(i + j)

    #Ensure combinations are ordered so state will be reliable    
    months_and_partner_codes.sort()
    
    if request_json["state"]:
        year_month_partner = request_json["state"]["year_month_partner"]
    else:
        year_month_partner = months_and_partner_codes[0]

    #parse state to use for url request parameters    
    year = str(year_month_partner[0:4])
    month = str(year_month_partner[4:6].lstrip('0'))
    partner_code = year_month_partner[6:8]
    
    #make follow-up calls until last state
    if year_month_partner != months_and_partner_codes[-1]:
        has_more = True
    else:
        has_more = False

    urls = [
            "https://apps.fas.usda.gov/OpenData/api/gats/customsDistrictExports",
            "https://apps.fas.usda.gov/OpenData/api/gats/customsDistrictImports",
            "https://apps.fas.usda.gov/OpenData/api/gats/customsDistrictReExports"
        ]
    
    #Initialize dict to collect json response
    response_json = {
        "insert" : {},
        "schema" : {},
        "state" : {}
    }
    
    #Initialize list to collect API url request responses
    url_responses = []
    
    for url in urls:
        
        #derive table name from url
        table_name = url.split("/", 6)[-1].replace("/", "_").lower()
            
        request_url = f"{url}/partnerCode/{partner_code}/year/{year}/month/{month}"
    
        #Invoke API request function
        response_text = make_request(request_url, api_key)
        
        #if empty response, capture metadata
        if (not response_text):              
            url_responses.append({"empty_requests" : [{"request_url" : request_url, "year_month_partner" : year_month_partner}]})
        #if response, invoke helper functions
        else:
            #Invoke dataframe creation function
            response_dataframe = create_dataframe(response_text)
            
            #If dataframe is empty, capture metatadata
            if response_dataframe.empty:
                url_responses.append({"non_qualifying_hs10_requests" : [{"request_url" : request_url, "year_month_partner" : year_month_partner}]})
            else:
                #Invoke dict assembly function and append entity values to response_json
                entity_values = assemble_response_dict(response_dataframe)
                
                url_responses.append({table_name : entity_values})
    
    if has_more:
        next_year_month_partner = months_and_partner_codes[months_and_partner_codes.index(year_month_partner) + 1]
    else:
        next_year_month_partner = months_and_partner_codes[0]
    
    #Combine entity inserts
    inserts = {
            k: [val for sublist in [d[k] for d in url_responses if k in d] for val in sublist]
            for k in set().union(*url_responses)
        }
    
    response_json["insert"] = inserts
    
    response_json["hasMore"] = has_more
    
    #get array of entity names
    entities = list(response_json["insert"].keys())
    
    #apply schemas to entity names
    schemas = {i: ({"primary_key": ["sha1_hash"]} if i not in ["empty_requests", "non_qualifying_hs10_requests"] else {"primary_key": ["year_month_partner"]}) for i in entities}
    
    response_json["schema"] = schemas
    
    #Increment state
    response_json["state"]["year_month_partner"] = next_year_month_partner
    response_json["state"]["year_month"] = next_year_month_partner[0:6]
    
    return response_json


with open('gats_log.txt', 'w') as f:
    f.write(str(handler({
    "secrets": {"apiKey": "2d229880-cae3-4b71-ba65-d7d95e7748b5"},
	"state" : {}
})))