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

headers = {'user-agent': 'Minneapolis-Condos/0.0.1'}
url = "https://www.zillow.com/homes/for_sale/Minneapolis-MN/pmf,pf_pt/condo_type/5983_rid/globalrelevanceex_sort/45.107211,-92.92923,44.815941,-93.421212_rect/11_zm/"
page = requests.get(url, headers = headers)
tree = html.fromstring(page.content)

"""
pagetext = page.text
tree_output = open("ZillowSearchHTML.txt",'w')
tree_output.write(pagetext)
tree_output.close()
"""

addresses = [str(i) for i in tree.xpath('//span[@class="zsg-photo-card-address"]/text()')]
prices = [str(i) for i in tree.xpath('//span[@class="zsg-photo-card-price"]/text()')]
specs = [str(i).replace("<!--", "").replace("-->", "") for i in tree.xpath('//li//div//comment()')]
