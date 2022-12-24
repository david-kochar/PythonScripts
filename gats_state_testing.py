from datetime import datetime
from dateutil.relativedelta import relativedelta
from itertools import product
import pandas as pd

#200001A1

request_json = {
    "secrets": {"apiKey": "2d229880-cae3-4b71-ba65-d7d95e7748b5"},
	"state" : {} #"year_month_partner" : "202210A2", "start_year_month" : "202210"
}

if request_json["state"]:
    start_year_month = request_json["state"]["start_year_month"]
    months = [start_year_month]
else:
    months = pd.date_range('2022-09-01', str(datetime.now().date() + relativedelta(months = -2)), 
                freq='MS').strftime("%Y%m").tolist()

months_and_partner_codes = []

partner_codes = ["A1", "A2"]

for i, j in product(months, partner_codes):
    months_and_partner_codes.append(i + j)

if request_json["state"]:
    year_month_partner = request_json["state"]["year_month_partner"]
else:
    year_month_partner = months_and_partner_codes[0]
    
if year_month_partner != months_and_partner_codes[-1]:
    has_more = True
else:
    has_more = False


if has_more:
    next_year_month_partner = months_and_partner_codes[months_and_partner_codes.index(year_month_partner) + 1]
else:
    next_year_month_partner = months_and_partner_codes[0] #year_month_partner

print(months_and_partner_codes)
print(has_more)
print(next_year_month_partner)


partner_code = "A1"
year = "2022"
month = "10"
url = "https://apps.fas.usda.gov/OpenData/api/gats/customsDistrictExports"

request_url = f"{url}/partnerCode/{partner_code}/year/{year}/month/{month}"

print(request_url)

year_month = "202211"

dt = year_month[:4] + "-" + year_month[4:6] + "-01"


months = pd.date_range(dt, str(datetime.now().date() + relativedelta(months = -2)), 
            freq='MS').strftime("%Y%m").tolist()

print(months)