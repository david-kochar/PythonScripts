# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 17:47:45 2018

@author: DK

Given an array of integers and a sum "S", create a function to return True if 
a continuous sequence that sums to S exists.

Example input:    [ 23, 5, 4, 7, 2, 11 ],  S = 20
Expected result:  True (7 + 2 + 11 = 20, consecutive in array, not numerically)

"""

def get_all_substrings(lst, s):
  length = len(lst)
  subs = [lst[i:j+1] for i in range(length) for j in range(i,length)]
  return any([sum(sub) == s for sub in subs])

get_all_substrings([23, 5, 4, 7, 2, 11], 20)