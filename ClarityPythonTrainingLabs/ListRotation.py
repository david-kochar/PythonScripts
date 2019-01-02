# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 18:28:00 2018

Create a function that performs n left rotations on a provided array of integers.
  (A left rotation shifts each of the array's elements one unit to the left.)

  Example input:    [1, 2, 3, 4, 5], n = 4
  Expected result:  [5, 1, 2, 3, 4]

@author: DK
"""

def rotate(l, n):
    return l[n:] + l[:n]

rotate([1, 2, 3, 4, 5], 4)
    
