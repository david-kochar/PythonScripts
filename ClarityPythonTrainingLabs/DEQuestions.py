# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 18:06:02 2018

@author: dkochar
"""

from itertools import combinations

lst = [-1, 0, 2, 1, -1, -4]

[list(i) for i in combinations (lst, 3) if sum(list(i)) == 0]

#[list(item) for item in set(tuple(row)) for row in lst]

