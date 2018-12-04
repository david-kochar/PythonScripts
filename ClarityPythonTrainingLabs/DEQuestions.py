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


   Example input:    '1123'

   Expected result:  aabc, kbc (11+2+3), alc (1+12+3), aaw, kw
"""

import itertools

nums = "1123"

def get_all_substrings(input_string):
  length = len(input_string)
  return [input_string[i:j+1] for i in range(length) for j in range(i,length) if len(input_string[i:j+1]) <= 2]

get_all_substrings(nums)

stuff = list(nums)
for i in range(0, len(stuff)+1):
    for subset in itertools.combinations(stuff, i):
        print(f"{i} {subset}")

nums = "1123"

sublist = [] 
  
for i in range(len(nums) + 1): 
    for j in range(i + 1, len(nums) + 1): 
        sub = [i, j, nums[i:j]]
        if len(sub[2]) <= 2:
            sublist.append(sub) 
            
sublist[1][2]

combos = []

for i in sublist:
    sub = []
    while len(sub) <= len(nums):
        sub.append(i[2])
    combos.append(sub)

combos

#create lists for single and two-digit numbers        `
singles_sublist = [i for i in sublist if len(i) == 1]
doubles_sublist = [i for i in sublist if len(i) == 2]

for i in range(len(singles_sublist)):
    print(singles_sublist[i])

#create combinations
combos = []
for i in range(len(singles_sublist)):
    for j in range(i, len(doubles_sublist)):
        for h in range(j, len(singles_sublist)):
            sub = [singles_sublist[i] + doubles_sublist[j] + singles_sublist[h]]
            combos.append(sub)
            
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