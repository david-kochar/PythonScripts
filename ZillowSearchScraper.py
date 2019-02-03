# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 10:00:33 2019

@author: DK
"""
import os
os.chdir("C:\\Users\DK\Documents\\GitHub\\PythonScripts")

from lxml import html
import requests

url = "https://www.zillow.com/homes/for_sale/pmf,pf_pt/condo,townhouse_type/1-_beds/150000-250000_price/592-987_mp/mostrecentchange_sort/45.023067,-93.209639,44.950281,-93.332634_rect/13_zm/X1.dash.SS.dash.16fg02arlqet_4n5nu_sse/ec9b9592c8X1-CRylkhrb73r81q_vpzyi_crid/"
page = requests.get(url)
pagetext = page.text
sourcecode = page.content #get string of source code from response
tree = html.fromstring(page.content)

type(sourcecode)

tree_output = open("ZillowSearchHTML.txt",'w')
tree_output.write(pagetext)
tree_output.close()

import os
print(os.getcwd())