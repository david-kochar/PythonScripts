# -*- coding: utf-8 -*-
"""
Given an array of sorted integers without duplicates, and two indices, i and j.
Write a function to calculate the number of missing integers between these two 
indices.  
 
For example [2,4,7,8,9,15],  

# of missing integers between index 0,1 is 1. 
# of missing integers between index 1,2 is 2. 
# of missing integers between index 0,2 is 3.
"""

def find_missing_ints ( num_list, idx_1, idx_2 ):
    return abs(num_list[idx_1] - num_list[idx_2]) - abs(idx_1 - idx_2)

find_missing_ints([2,4,7,8,9,15], 0, 1)
    