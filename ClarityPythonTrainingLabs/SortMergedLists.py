# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 18:23:32 2018

@author: DK

Create a function to merge two sorted lists into a single sorted list.

  Example input: 
     L1 = [1,3,5,7]
     L2 = [2,6,9]

  Expected result:
     merged_L = [1,2,3,5,6,9]	
     
"""

def lists_sort_and_merge(lst1, lst2):
    return sorted(lst1 + lst2)

lists_sort_and_merge([1,3,5,7], [2,6,9])