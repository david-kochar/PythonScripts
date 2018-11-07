# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 10:09:52 2018

@author: DK
"""

def contains_purple(*args):
    if "purple" in args:
        return True
    return False

def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word

combine_words("child")

# Write a lambda that accepts a single number and cubes it. Save it in a variable called cube.
cube = lambda num: num**3

cube(2)

#nums = [1,2,3,4]
#map(lambda x: x*2, nums)

def decrement_list(lst):
    return list(map(lambda x: x-1, lst))

decrement_list([1,2,3])

def remove_negatives(lst):
    return list(filter(lambda x: x >= 0, lst))

remove_negatives([-1, 3, 4, -99])