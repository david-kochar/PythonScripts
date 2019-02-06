# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 10:00:33 2019

@author: DK

Webscraper for Zillow listings
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
pagetext = page.text
tree_output = open("ZillowSearchHTML.txt",'w')
tree_output.write(pagetext)
tree_output.close()
"""

"""
Parse listing data. Note that "specs" will need to be further parsed as it
contains nested dicts of property details
"""

#addresses = [str(i) for i in tree.xpath('//span[@class="zsg-photo-card-address"]/text()')]
#prices = [str(i) for i in tree.xpath('//span[@class="zsg-photo-card-price"]/text()')]
specs = [str(i).replace("<!--", "").replace("-->", "").replace("\\", "").replace("false", "False").replace("true", "True")
        for i in tree.xpath('//li//div//comment()')]

specs = [ast.literal_eval(i) for i in specs] #remove quotes to allow iteration

"""
#Individual variables

zpid = [i["homeInfo"]["zpid"] for i in specs]
streetAddress = [i["homeInfo"]["streetAddress"] for i in specs]
zipcode = [i["homeInfo"]["zipcode"] for i in specs]
city = [i["homeInfo"]["city"] for i in specs]
state = [i["homeInfo"]["state"] for i in specs]
price = [i["homeInfo"]["price"] for i in specs]
dateSold = [i["homeInfo"]["dateSold"] for i in specs]
bathrooms = [i["homeInfo"]["bathrooms"] for i in specs]
bedrooms = [i["homeInfo"]["bedrooms"] for i in specs]
livingArea = [i["homeInfo"]["livingArea"] for i in specs]
yearBuilt = [i["homeInfo"]["yearBuilt"] for i in specs]
lotSize = [i["homeInfo"]["lotSize"] for i in specs]
homeType = [i["homeInfo"]["homeType"] for i in specs]
homeStatus = [i["homeInfo"]["homeStatus"] for i in specs]
daysOnZillow = [i["homeInfo"]["daysOnZillow"] for i in specs]
brokerId = [i["homeInfo"]["brokerId"] for i in specs]
contactPhone = [i["homeInfo"]["contactPhone"] for i in specs]
zestimate = [i["homeInfo"]["zestimate"] for i in specs]
isPreforeclosureAuction = [i["isPreforeclosureAuction"] for i in specs]
homeStatusForHDP = [i["homeStatusForHDP"] for i in specs]
priceForHDP = [i["priceForHDP"] for i in specs]
festimate = [i["festimate"] for i in specs]
isListingOwnedByCurrentSignedInAgent = [i["isListingOwnedByCurrentSignedInAgent"] for i in specs]
timeOnZillow = [i["timeOnZillow"] for i in specs]
isListingClaimedByCurrentSignedInUser = [i["isListingClaimedByCurrentSignedInUser"] for i in specs]
contactPhoneExtension = [i["contactPhoneExtension"] for i in specs]
lotId = [i["lotId"] for i in specs]
lotId64 = [i["lotId64"] for i in specs]
isNonOwnerOccupied = [i["isNonOwnerOccupied"] for i in specs]
isPremierBuilder = [i["isPremierBuilder"] for i in specs]
isZillowOwned = [i["isZillowOwned"] for i in specs]
"""

#Create sets of dict keys from specs
specs_keys          = set().union(*(d.keys() for d in specs))
specs_homeinfo_keys = ["zpid", "streetAddress", "zipcode", "city", "state",        
"price","dateSold", "bathrooms", "bedrooms", "livingArea", "yearBuilt", 
"lotSize", "homeType", "homeStatus", "daysOnZillow", "brokerId", "contactPhone", 
"zestimate"] #set().union(*(d["homeInfo"].keys() for d in specs))

#Create a nested dict of all listings
specs_dict = {}

for i in specs:
    for k in i["homeInfo"]:
        specs_dict[specs.index(i)] = {k: i["homeInfo"].get(k, None) for k in specs_homeinfo_keys}
        

