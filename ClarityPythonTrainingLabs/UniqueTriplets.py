# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 17:46:49 2018

@author: DK

Create a function taking an array of n integers, find all unique triplets 

   (elements a, b, c) where the sum of the triplet equals zero (a + b + c = 0).


   Example input:    [-1, 0, 2, 1, -1, -4]

   Expected result:  [ [-1, 0, 1], [-1, -1, 2] ]

"""

import itertools

lst = [-1, 0, 2, 1, -1, -4]

triplets = sorted([sorted(list(i)) for i in combinations (lst, 3) if sum(list(i)) == 0])

unique_triplets = [list(i) for i in set(tuple(i) for i in triplets)]