# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 09:52:35 2020

@author: kocha
"""

import urllib, json

pizzaOrdersRaw = json.loads(urllib.request.urlopen("https://www.olo.com/pizzas.json").read())

'''
#Append to orders key value pairs of toppings and counter of 1 for each order
for order in pizzaOrders:
    for i in order.values():
        toppings = i
        toppings.sort() #order toppings for subsequent aggregation - only consider order combinations
        orders.append({"toppings":tuple(toppings), "counter":1}) #key must be immutable, tuple is used


orders = [ {"toppings":tuple(sorted(i)), "counter":1} for order in pizzaOrders for i in order.values() ]
        
orders
'''

with open(f"{pizzaOrdersRaw}.json, 'w'", 'w') as outfile:
    json.dump(pizzaOrdersRaw, outfile)