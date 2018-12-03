# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 18:06:02 2018

@author: dkochar
"""

"""
Create a function taking an array of n integers, find all unique triplets 

   (elements a, b, c) where the sum of the triplet equals zero (a + b + c = 0).


   Example input:    [-1, 0, 2, 1, -1, -4]

   Expected result:  [ [-1, 0, 1], [-1, -1, 2] ]


"""

import itertools

lst = [-1, 0, 2, 1, -1, -4]

triplets = sorted([sorted(list(i)) for i in combinations (lst, 3) if sum(list(i)) == 0])

unique_triplets = [list(i) for i in set(tuple(i) for i in triplets)]

"""
Given a=1, b=2, c=3, ... z=26, create a function to find all possible letter

   combinations the string can generate.


   Example input:    ‘1123‘

   Expected result:  aabc, kbc (11+2+3), alc (1+12+3), aaw, kw
"""

nums = "1123"

# store all the sublists  
sublist = [] 
  
# first loop  
for i in range(len(nums) + 1): 
      
    # second loop  
    for j in range(i + 1, len(nums) + 1): 
          
        # slice the subarray  
        sub = [i, j, nums[i:j]]
        if len(sub) <= 3:
            sublist.append(sub) 
        
singles_sublist = [i for i in sublist if len(i[2]) == 1]
doubles_sublist = [i for i in sublist if len(i[2]) == 2]

combos = []
for i in singles_sublist:
    for j in doubles_sublist:
        x = range(i[0],i[1])
        y = range(j[0],j[1])
        xs = set(x)
        if not xs.intersection(y) and i[0] < j[0]:
            combos.append([i[2],j[2]])
            
combos


#singles = [i for i in nums]
#doubles = list(set(map("".join, itertools.combinations(nums, 2))))
#singles_and_doubles = singles + doubles

doubles_combos = list(map(",".join, itertools.combinations(doubles, 2)))
n_combos = list(map(",".join, itertools.combinations(singles_and_doubles, len(nums))))
n_minus1_combos = list(map(",".join, itertools.combinations(singles_and_doubles, len(nums) - 1)))

all_combos = n_combos + n_minus1_combos + doubles_combos
all_combos

[i for i in all_combos if len(i.replace(",","")) == 4]

list(map("".join, itertools.combinations(singles, len(singles))))

list(set(map("".join, itertools.combinations(nums, 2))))