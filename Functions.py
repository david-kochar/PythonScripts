# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 19:23:40 2018

@author: dkochar
"""
#Define a function that prints "THE CROWD GOES WILD"

#Define your make_noise function below
def make_noise():
    print("THE CROWD GOES WILD")


#Then, call make_noise once:
make_noise()

#create a coin-flipping function
from random import random
def flip_coin():
    r = random()
    if r > 0.5:
        return "Heads"
    else:
        return "Tails"
    
print(flip_coin())

def speak_pig():
    return ("oink")

speak_pig()

def generate_evens():
    return [num for num in range(1,50) if num % 2 == 0]

generate_evens()