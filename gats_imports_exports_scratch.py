from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
from itertools import product


months = pd.date_range('2017-01-01', str(datetime.now().date() + relativedelta(months = -2)), 
              freq='MS').strftime("%Y%m").tolist()

print(months)

print(str(datetime.now().date() + relativedelta(months = -2)))

current_year_and_month = str(datetime.now().year) + str(datetime.now().month) + ""

current_year_and_month_offeset = (datetime.strptime(current_year_and_month, '%Y%m').date() + relativedelta(months = -2)).strftime("%Y%m")

print(current_year_and_month_offeset)

print(current_year_and_month)

year_month = str(current_year_and_month)

next_year_month = (datetime.strptime(year_month, '%Y%m').date() + relativedelta(months = -2)).strftime("%Y%m")

print(next_year_month)

year = year_month[0:4]
month = year_month[4:6].lstrip('0')

print(year)
print(month)

d = {
    "agent" : "<function_connector_name>/<external_id>/<schema>",
    "state": {
        "a": "2",
        "b": "2"
    },
    "secrets": {
        "apiToken": "abcdefghijklmnopqrstuvwxyz_0123456789"
    }
}

print(max(d["state"].values()))

partner_codes = ['A1', 'A2', 'AA', 'AC', 'AE', 'AF', 'AG', 'AJ', 'AL', 'AM', 
                  'AN', 'AO', 'AQ', 'AR', 'AS', 'AU', 'AV', 'AY', 'B1', 'BA', 
                  'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BK', 'BL', 'BM', 
                  'BN', 'BO', 'BP', 'BR', 'BT', 'BU', 'BV', 'BX', 'BY', 'CA', 
                  'CB', 'CD', 'CE', 'CF', 'CG', 'CH', 'CI', 'CJ', 'CK', 'CM', 
                  'CN', 'CO', 'CQ', 'CS', 'CT', 'CU', 'CV', 'CW', 'CY', 'CZ', 
                  'D1', 'DA', 'DJ', 'DO', 'DR', 'E1', 'EC', 'EG', 'EI', 'EK', 
                  'EN', 'ER', 'ES', 'ET', 'EZ', 'F1', 'FG', 'FI', 'FJ', 'FK', 
                  'FM', 'FO', 'FP', 'FR', 'FS', 'G1', 'GA', 'GB', 'GC', 'GE', 
                  'GG', 'GH', 'GI', 'GJ', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 
                  'GT', 'GV', 'GY', 'GZ', 'HA', 'HK', 'HM', 'HO', 'HR', 'HU', 
                  'I1', 'I2', 'IC', 'ID', 'IN', 'IO', 'IR', 'IS', 'IT', 'IV', 
                  'IY', 'IZ', 'JA', 'JM', 'JO', 'KE', 'KG', 'KN', 'KR', 'KS', 
                  'KT', 'KU', 'KV', 'KZ', 'LA', 'LE', 'LG', 'LH', 'LI', 'LO', 
                  'LS', 'LT', 'LU', 'LY', 'MA', 'MB', 'MC', 'MD', 'MF', 'MG', 
                  'MH', 'MI', 'MJ', 'MK', 'ML', 'MN', 'MO', 'MP', 'MQ', 'MR', 
                  'MT', 'MU', 'MV', 'MX', 'MY', 'MZ', 'N1', 'N2', 'N3', 'NC', 
                  'NE', 'NF', 'NG', 'NH', 'NI', 'NL', 'NN', 'NO', 'NP', 'NQ', 
                  'NR', 'NS', 'NT', 'NU', 'NZ', 'OD', 'P1', 'PA', 'PC', 'PE', 
                  'PK', 'PL', 'PM', 'PO', 'PP', 'PQ', 'PS', 'PU', 'QA', 'R1', 
                  'RB', 'RE', 'RM', 'RO', 'RP', 'RQ', 'RS', 'RW', 'S1', 'S2', 
                  'SA', 'SB', 'SE', 'SF', 'SG', 'SH', 'SI', 'SL', 'SM', 'SN', 
                  'SO', 'SP', 'SR', 'ST', 'SU', 'SV', 'SW', 'SX', 'SY', 'SZ', 
                  'TD', 'TH', 'TI', 'TK', 'TL', 'TN', 'TO', 'TP', 'TS', 'TT', 
                  'TU', 'TV', 'TW', 'TX', 'TZ', 'U0', 'UC', 'UG', 'UK', 'UP', 
                  'UR', 'UV', 'UY', 'UZ', 'V1', 'V2', 'V4', 'V5', 'V6', 
                  'V7', 'V8', 'VC', 'VE', 'VI', 'VM', 'VO', 'VT', 'W2', 'W5', 
                  'W6', 'W7', 'WA', 'WE', 'WF', 'WI', 'WQ', 'WS', 'WZ', 'X4', 
                  'X6', 'X8', 'X9', 'Y1', 'Y2', 'Y3', 'Y7', 'Y9', 'YE', 'YM', 
                  'YO', 'YS', 'YU', 'Z1', 'Z2', 'Z5', 'Z6', 'Z7', 'Z8', 'ZA', 
                  'ZB', 'ZI']

print(len(partner_codes))

urls = ["https://apps.fas.usda.gov/OpenData/api/gats/censusImports"
            ,"https://apps.fas.usda.gov/OpenData/api/gats/censusExports"
            ,"https://apps.fas.usda.gov/OpenData/api/gats/censusReExports"
            ,"https://apps.fas.usda.gov/OpenData/api/gats/customsDistrictExports"
            ,"https://apps.fas.usda.gov/OpenData/api/gats/customsDistrictImports"
            ,"https://apps.fas.usda.gov/OpenData/api/gats/customsDistrictReExports"
            ]

partner_codes = ['A1'
                 ,'ZI'
                 ]

year_month = '202208'


for url in urls:
    year = year_month[0:4]
    month = year_month[4:6].lstrip('0')
    for partner_code in partner_codes:
        new_url = ""
        new_url = url + "/partnerCode/" + partner_code + "/year/" + year + "/month/" + month
        print(new_url)
        
        
d = {
    # "state": {
    #     "transaction": "2018-01-02T00:00:00Z",
    #     "campaign": "2018-01-02T00:00:01Z"
    # },
    "insert": {
        "transaction": [
            {"id":1, "amount": 100},
            {"id":2, "amount": 50}
        ],
        "campaign": [
            {"id":101, "name": "Christmas"},
            {"id":102, "name": "New Year"}
        ]
    },
    "delete": {
        "transaction": [
            {"id":3},
            {"id":4}
        ],
        "campaign": [
            {"id":103},
            {"id":104}
        ]
    },
    "schema" : {
        "transaction": {
            "primary_key": ["id"]
        },
        "campaign": {
            "primary_key": ["id"]
        }
    },
    "hasMore" : True
}

response_json = {}

d_tables = list(d["insert"].keys())

states = dict((i,0) for i in d_tables)

response_json["state"] = states

print(response_json)


d = {'insert': {"a":"b"}, 'schema': {}, 'state': {}}

for k,v in d.items(): 
  if d[k] is None or len(d[k]) == 0:
    print("No Value")
  else: 
    print("Has Value")

for key, value in d.iteritems():
    if value is None or len(value) == 0:
        print("None found!")

# with open('gats_import_export_log.txt', 'w') as f:
#     f.write(str(handler({
#     "secrets": {"apiKey": "2d229880-cae3-4b71-ba65-d7d95e7748b5"},
# 	"state" : {}
# })))


months = pd.date_range('2017-01-01', str(datetime.now().date() + relativedelta(months = -2)), 
              freq='MS').strftime("%Y%m").tolist()

partner_codes = ['A1', 'CH', 'ZI']

months_and_partner_codes = []

for e1, e2 in product(months, partner_codes):
    months_and_partner_codes.append(e1 + e2)
    
print(months_and_partner_codes)