# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:55:07 2018

@author: DK

Write a function that determines if a list
contains duplicate elements.

"""

def list_duplicate_tester(lst):
    flag = all ( [lst.count(i) == 1 for i in lst] )
    if flag:
        return f"The list does NOT contain duplicates"
    else:
        return f"The list DOES contain duplicates"

list_duplicate_tester(["a", "b", "c"])
list_duplicate_tester(["a", "a", "b", "c"])