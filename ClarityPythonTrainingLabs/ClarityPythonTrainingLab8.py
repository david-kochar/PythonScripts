# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:51:43 2018

@author: DK

Write a function that returns the number of
items in a list.

"""

def list_item_counter(lst):
    cnt = 0
    for i in lst:
        cnt += 1
    return f"The list contains {cnt} items."

list_item_counter([1,2,3])