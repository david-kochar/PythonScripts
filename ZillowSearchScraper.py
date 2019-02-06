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
url = "https://www.zillow.com/homes/for_sale/Minneapolis-MN/pmf,pf_pt/condo_type/5983_rid/globalrelevanceex_sort/45.107211,-92.92923,44.815941,-93.421212_rect/11_zm/"
page = requests.get(url, headers = headers)
tree = html.fromstring(page.content)

"""
pagetext = page.text
tree_output = open("ZillowSearchHTML.txt",'w')
tree_output.write(pagetext)
tree_output.close()
"""

"""
Parse listing data. Note that "specs" will need to be further parsed as it
contains dictionaries
"""

#addresses = [str(i) for i in tree.xpath('//span[@class="zsg-photo-card-address"]/text()')]
#prices = [str(i) for i in tree.xpath('//span[@class="zsg-photo-card-price"]/text()')]
specs = [str(i).replace("<!--", "").replace("-->", "").replace("\\", "").replace("false", "False").replace("true", "True")
        for i in tree.xpath('//li//div//comment()')]

specs = [ast.literal_eval(i) for i in specs]

addresses = [i["homeInfo"]["streetAddress"] for i in specs]

addresses


t = [{  
   "bed":2,
   "miniBubbleType":1,
   "image":"https://photos.zillowstatic.com/p_a/ISmedy1xckd2g10000000000.jpg",
   "sqft":941,
   "label":"$160K",
   "isPropertyTypeVacantLand":False,
   "datasize":9,
   "title":"$160K",
   "bath":1.0,
   "homeInfo":{  
      "zpid":71815870,
      "streetAddress":"3441 Portland Ave APT 3",
      "zipcode":"55407",
      "city":"Minneapolis",
      "state":"MN",
      "latitude":44.939852,
      "longitude":-93.26721,
      "price":160000.0,
      "dateSold":1212390000000,
      "bathrooms":1.0,
      "bedrooms":2.0,
      "livingArea":941.0,
      "yearBuilt":1920,
      "lotSize":-1.0,
      "homeType":"CONDO",
      "homeStatus":"FOR_SALE",
      "photoCount":43,
      "imageLink":"https://photos.zillowstatic.com/p_g/ISmedy1xckd2g10000000000.jpg",
      "daysOnZillow":4,
      "isFeatured":False,
      "shouldHighlight":False,
      "brokerId":12920,
      "contactPhone":"9528292900",
      "zestimate":160416,
      "rentZestimate":1395,
      "listing_sub_type":{  
         "is_FSBA":True
      },
      "priceReduction":"",
      "isUnmappable":False,
      "rentalPetsFlags":192,
      "mediumImageLink":"https://photos.zillowstatic.com/p_c/ISmedy1xckd2g10000000000.jpg",
      "isPreforeclosureAuction":False,
      "homeStatusForHDP":"FOR_SALE",
      "priceForHDP":160000.0,
      "festimate":123520,
      "isListingOwnedByCurrentSignedInAgent":False,
      "timeOnZillow":1549035780000,
      "isListingClaimedByCurrentSignedInUser":False,
      "hiResImageLink":"https://photos.zillowstatic.com/p_f/ISmedy1xckd2g10000000000.jpg",
      "watchImageLink":"https://photos.zillowstatic.com/p_j/ISmedy1xckd2g10000000000.jpg",
      "contactPhoneExtension":"",
      "lotId":1002431721,
      "tvImageLink":"https://photos.zillowstatic.com/p_m/ISmedy1xckd2g10000000000.jpg",
      "tvCollectionImageLink":"https://photos.zillowstatic.com/p_l/ISmedy1xckd2g10000000000.jpg",
      "tvHighResImageLink":"https://photos.zillowstatic.com/p_n/ISmedy1xckd2g10000000000.jpg",
      "zillowHasRightsToImages":False,
      "lotId64":1002431721,
      "desktopWebHdpImageLink":"https://photos.zillowstatic.com/p_h/ISmedy1xckd2g10000000000.jpg",
      "isNonOwnerOccupied":True,
      "hideZestimate":False,
      "isPremierBuilder":False,
      "isZillowOwned":False,
      "currency":"USD",
      "country":"USA"
   }
},
{  
   "bed":2,
   "miniBubbleType":1,
   "image":"https://photos.zillowstatic.com/p_a/ISircnhzwh3u890000000000.jpg",
   "sqft":1006,
   "label":"$240K",
   "isPropertyTypeVacantLand":False,
   "datasize":9,
   "title":"$240K",
   "bath":1.0,
   "homeInfo":{  
      "zpid":98346077,
      "streetAddress":"3508 Emerson Ave S APT 101",
      "zipcode":"55408",
      "city":"Minneapolis",
      "state":"MN",
      "latitude":44.939154,
      "longitude":-93.294928,
      "price":240000.0,
      "dateSold":1342681200000,
      "bathrooms":1.0,
      "bedrooms":2.0,
      "livingArea":1006.0,
      "yearBuilt":1925,
      "lotSize":-1.0,
      "homeType":"CONDO",
      "homeStatus":"FOR_SALE",
      "photoCount":35,
      "imageLink":"https://photos.zillowstatic.com/p_g/ISircnhzwh3u890000000000.jpg",
      "daysOnZillow":5,
      "isFeatured":False,
      "shouldHighlight":False,
      "brokerId":13733,
      "contactPhone":"9529285563",
      "zestimate":237610,
      "rentZestimate":1650,
      "listing_sub_type":{  
         "is_FSBA":True
      },
      "priceReduction":"",
      "isUnmappable":False,
      "mediumImageLink":"https://photos.zillowstatic.com/p_c/ISircnhzwh3u890000000000.jpg",
      "isPreforeclosureAuction":False,
      "homeStatusForHDP":"FOR_SALE",
      "priceForHDP":240000.0,
      "festimate":182959,
      "isListingOwnedByCurrentSignedInAgent":False,
      "timeOnZillow":1548961320000,
      "isListingClaimedByCurrentSignedInUser":False,
      "hiResImageLink":"https://photos.zillowstatic.com/p_f/ISircnhzwh3u890000000000.jpg",
      "watchImageLink":"https://photos.zillowstatic.com/p_j/ISircnhzwh3u890000000000.jpg",
      "contactPhoneExtension":"",
      "tvImageLink":"https://photos.zillowstatic.com/p_m/ISircnhzwh3u890000000000.jpg",
      "tvCollectionImageLink":"https://photos.zillowstatic.com/p_l/ISircnhzwh3u890000000000.jpg",
      "tvHighResImageLink":"https://photos.zillowstatic.com/p_n/ISircnhzwh3u890000000000.jpg",
      "zillowHasRightsToImages":False,
      "desktopWebHdpImageLink":"https://photos.zillowstatic.com/p_h/ISircnhzwh3u890000000000.jpg",
      "isNonOwnerOccupied":False,
      "hideZestimate":False,
      "isPremierBuilder":False,
      "isZillowOwned":False,
      "currency":"USD",
      "country":"USA"
   }
}
]
new_list = [i["homeInfo"]["streetAddress"] for i in t]
new_list