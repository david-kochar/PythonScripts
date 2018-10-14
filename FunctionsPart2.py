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