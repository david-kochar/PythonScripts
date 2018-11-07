# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 15:42:13 2018

@author: dkochar

Create a function which creates a random integer value between lowValue and 
highValue parameters. If no value is provided, the integer should be between
0 and 100 inclusive. hint: the function randint in the random module will be 
helpful.  randint takes two parameters (a, b) and returns a random integer N 
such that a <= N <= b

"""
from random import randint

def random_integer(lowval=0, highval=101):
    try:
        rand = randint(lowval, highval+1)
    except ValueError as err:
        print("The first value must be less than or equal to the second value")
        print(err)
    else:
        print(f"A random number between {lowval} and {highval} is {rand}")
        
"""
Using mathematical operators, write a function that calculates the area of a 
triangle, given a base and height. Default base and height should be 10

"""

def triangle_area_calculator(base=10, height=10):
    return 0.5 * base * height