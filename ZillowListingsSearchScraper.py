# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 20:33:07 2019

@author: dkochar
"""

import requests 
from lxml import html

import ast

headers = {'user-agent': 'ListingsScraper/0.0.1'}
url = "https://www.zillow.com/homes/for_sale/Minneapolis-MN/5983_rid/globalrelevanceex_sort/45.116055,-93.015404,44.825073,-93.507386_rect/11_zm/"
base_url = url
urls = [base_url]
specs_dict = {} #create empty dict

path_counter = 1
while True:
    page = requests.get(url, headers = headers)
    if page.status_code != 200:
        break
    path_counter += 1
    url = base_url + str(path_counter) + "_p/"
    urls.append(url)

    for url in urls:
        page  = requests.get(url, headers = headers)
        tree  = html.fromstring(page.content)
        specs = [str(i).replace("<!--", "").replace("-->", "").replace("\\", "").replace("false", "False").replace("true", "True")
                for i in tree.xpath('//li//div//comment()')] 
    
    #Parse listing data. Note that "specs" will need to be further parsed as it
    #contains nested dicts of property details
    specs = [ast.literal_eval(i) for i in specs] #remove quotes to allow iteration
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
    for i in specs:
        for k in i["homeInfo"]:
            specs_dict[specs.index(i)] = {k: i["homeInfo"].get(k, None) for k in specs_homeinfo_keys} #Export csv of listings

with open('ZillowReport.csv', 'w') as f: #create csv
    
    #write header row
    f.write("," .join([i for i in specs_homeinfo_keys]) + "\n")
    
    #write row for each listing dict.values
    for record in specs_dict.values(): 
        f.write("," .join([str(i) for i in list(record.values())]) + "\n")
        
f.close()