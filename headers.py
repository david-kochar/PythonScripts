# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:50:22 2020

@author: kocha
"""

import requests
from random import choice

url = "https://icanhazdadjoke.com/search"

joke_topic = input ("Let me tell a joke! What's your joke topic? ")

response = requests.get(
    url, 
    headers = {"Accept":"application/json"},
    params = {"term":"cats"}
)

joke_list = [joke["joke"] for joke in response.json()["results"]]

joke_count = len(joke_list)

if len(joke_list) > 0:
    print (f"I've got {joke_count} about {joke_topic}. Here's one:")
    print (choice(joke_list))
else:
    print(f"Sorry, I don't have any jokes about {joke_topic}!")

    
