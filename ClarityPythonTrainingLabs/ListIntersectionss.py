# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 19:52:25 2018

@author: DK

Create a function that returns False if there are intersections between
three provided integer arrays. Please limit use of native functionality.

   Example Input:
       A = [6, 5, 4, 1, 7, 8, 9, 0, 1, 6, 5, 7, 5, 4, 1, 7, 8, 9, 0, 1, 6, 5, 7]
       B = [61, 54, 6, 8, 13, 70, 18, 0, 61, 6]
       C = [6, 6, 0, 71, 5]
       
   Expected result: True
       (Two intersections exist: 0 and 6)

"""

lst1 = [6, 5, 4, 1, 7, 8, 9, 0, 1, 6, 5, 7, 5, 4, 1, 7, 8, 9, 0, 1, 6, 5, 7]
lst2 = [61, 54, 6, 8, 13, 70, 18, 0, 61, 6]
lst3 = [6, 6, 0, 71, 5]

def lists_intesection(lst1, lst2, lst3):
    if [i for i in lst1 if i in lst2 and i in lst3]:
        return True

lists_intesection(lst1, lst2, lst3)