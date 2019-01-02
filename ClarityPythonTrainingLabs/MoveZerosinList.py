# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 21:39:09 2018

@author: DK

Create a function that moves all zero valued elements of a provided array to 
the right while maintaining the original order of the remaining elements.
(Do not create any new arrays)

  Example Input:    [1, 0, 0, 4, 3, 5, 0, 0, 7, 8]
  Expected result:  [1, 4, 3, 5, 7, 8, 0, 0, 0, 0]
  
"""
def move_zero_valued(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]
    
move_zero_valued([1, 0, 0, 4, 3, 5, 0, 0, 7, 8])
