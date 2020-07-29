# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 09:52:35 2020

@author: kocha
"""

import urllib, json

pizzaOrdersRaw = json.loads(urllib.request.urlopen("https://www.olo.com/pizzas.json").read())
