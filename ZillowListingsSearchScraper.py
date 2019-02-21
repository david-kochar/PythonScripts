# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 20:33:07 2019

@author: dkochar

This is a webscraper app for Zillow listings, which exports to csv

"""

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from lxml import html

session = requests.Session()
retry   = Retry(connect=3, backoff_factor=0.5) #used for request to delay to avoid blacklisting
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

headers    = {'user-agent': 'ListingsScraper/0.0.1'} #create headers for legimate requests
url        = "https://www.zillow.com/homes/for_sale/Minneapolis-MN/5983_rid/globalrelevanceex_sort/45.116055,-93.015404,44.825073,-93.507386_rect/11_zm/" #base url for Minneapolis listings
base_url   = url
urls       = [base_url] #seed urls list with base url
specs      = [] #create empty list for listing dicts
specs_dict = {} #create empty dict for nesting listing dicts

path_counter = 2 #succesive listing pages start at 2
while True:
    url = base_url + str(path_counter) + "_p/" #zillow.com url structure appends page count and _p/
    response = requests.head(url, headers = headers)
    if response.status_code != 200: #build url list for all valid listing pages
        break
    urls.append(url)
    path_counter += 1

for url in urls:
    page = session.get(url, headers = headers)
    tree = html.fromstring(page.content)
    #relevant listing info is embedded in comments, and need to pre-scrub html to coerce into dicts
    specs.append( [str(i).replace('<!--', '').replace('-->', '').replace('\\', '').replace('false', 'False').replace('true', 'True').replace('null', '"' + '' + '"' )
            for i in tree.xpath('//li//div//comment()')] )

#Parse listing data. Note that "specs" will need to be further parsed as it
#contains nested dicts of property details

specs = [ eval(i) for lst in specs for i in lst ] #remove quotes to allow iteration

#create list of relevant dict keys for nested "homeInfo" dicts
specs_homeinfo_keys = [
                       "zpid", 
                       "streetAddress", 
                       "zipcode", 
                       "city", 
                       "state",
                       "price",
                       "dateSold", 
                       "bathrooms", 
                       "bedrooms", 
                       "livingArea", 
                       "yearBuilt", 
                       "lotSize", 
                       "homeType", 
                       "homeStatus", 
                       "daysOnZillow", 
                       "brokerId", 
                       "contactPhone", 
                       "zestimate" 
                      ] 

#Generate nested dicts where each dict represents a listing record    
for i in specs:
    for k in i["homeInfo"]:
        specs_dict[specs.index(i)] = {k: i["homeInfo"].get(k, '') for k in specs_homeinfo_keys} 

#Export csv of listings
with open('ZillowReport.csv', 'w') as f: #create csv
    
    #write header row
    f.write("," .join([i for i in specs_homeinfo_keys]) + "\n")
    
    #write row for each listing dict.values
    for record in specs_dict.values(): 
        f.write("," .join([str(i) for i in list(record.values())]) + "\n")
        
f.close()