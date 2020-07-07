# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 09:54:22 2020

@author: kocha
"""

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

l2 = [[[1, 2], [3, 4]], [[4, 5], [6, 7]]]

#Flatten nested list
[ j for i in l for j in i ]

#Flatten double nested list        
[ k for i in l2 for j in i for k in j ]
