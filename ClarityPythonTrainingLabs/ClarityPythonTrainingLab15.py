# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:37:35 2018

Given the following JSON string, parse it and write the data records to a csv 
file called fruits.csv.

{
    "total": 3,
    "data": [
        { "id": 1, "name": "grapes", "quantity": 100, "cost": 1.01 },
        { "id": 2, "name": "strawberries", "quantity": 50, "cost": 3.71 },
        { "id": 3, "name": "lemon", "quantity": 10, "cost": 2.17 }
    ]
}

@author: DK
"""

import json

json_string_fruits = """
{
    "total": 3,
    "data": [
        { "id": 1, "name": "grapes", "quantity": 100, "cost": 1.01 },
        { "id": 2, "name": "strawberries", "quantity": 50, "cost": 3.71 },
        { "id": 3, "name": "lemon", "quantity": 10, "cost": 2.17 }
    ]
}
"""
fruits_dict = json.loads(json_string_fruits)

with open('fruits.csv', 'w') as f:
    for record in fruits_dict["data"]:
        f.write("," .join([str(i) for i in list(record.values())]) + "\n")
        
f.close()