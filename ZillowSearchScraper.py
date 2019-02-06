# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 10:00:33 2019

@author: DK

This is a webscraper app for Zillow listings, which exports to csv
"""

import os
os.chdir("C:\\Users\DK\Documents\\GitHub\\PythonScripts")

import requests 
from lxml import html

import ast

headers = {'user-agent': 'ListingsScraper/0.0.1'}
url     = "https://www.zillow.com/homes/for_sale/Minneapolis-MN/pmf,pf_pt/condo_type/5983_rid/globalrelevanceex_sort/45.107211,-92.92923,44.815941,-93.421212_rect/11_zm/"
page    = requests.get(url, headers = headers)
tree    = html.fromstring(page.content)

"""
Parse listing data. Note that "specs" will need to be further parsed as it
contains nested dicts of property details
"""
specs = [str(i).replace("<!--", "").replace("-->", "").replace("\\", "").replace("false", "False").replace("true", "True")
        for i in tree.xpath('//li//div//comment()')]

specs = [ast.literal_eval(i) for i in specs] #remove quotes to allow iteration

"""
#Individual variables example

zpid = [i["homeInfo"]["zpid"] for i in specs]
isZillowOwned = [i["isZillowOwned"] for i in specs]
"""

#Create sets of dict keys from specs
#specs_keys          = set().union(*(d.keys() for d in specs))
specs_homeinfo_keys = ["zpid", 
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
                      ] #set().union(*(d["homeInfo"].keys() for d in specs))

#Create a nested dict of all listings

#Generate nested dicts where each dict represents a listing record
specs_dict = {} #create empty dict

for i in specs:
    for k in i["homeInfo"]:
        specs_dict[specs.index(i)] = {k: i["homeInfo"].get(k, None) for k in specs_homeinfo_keys}

#Export csv of listings
with open('ZillowReport.csv', 'w') as f: #create csv
    
    #write header row
    f.write("," .join([i for i in specs_homeinfo_keys]) + "\n")
    
    #write row for each listing dict.values
    for record in specs_dict.values(): 
        f.write("," .join([str(i) for i in list(record.values())]) + "\n")
        
f.close()
