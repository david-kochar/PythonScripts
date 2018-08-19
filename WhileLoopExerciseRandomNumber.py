# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 14:18:15 2018

@author: DK
"""

from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration

while number != 5:
    number = randint (1, 10)
    i += 1
    
print(i)