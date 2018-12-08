# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 15:19:23 2018

@author: dkochar

Given a=1, b=2, c=3, ... z=26, create a function to find all possible letter

   combinations the string can generate.


   Example input:    '1123'

   Expected result:  aabc, kbc (11+2+3), alc (1+12+3), aaw, kw
"""

def letter_combinations(nums):
    from itertools import combinations, chain
    from string import ascii_lowercase
    from operator import sub
    
    #create integer-to-letter dictionary lookup
    letters_lookup = {str(index):letter for index, letter in enumerate(ascii_lowercase, start=1)}
    
    #cast nums as string
    nums = str(nums)
    sequences_filtered = []
    letter_partitions = []
    
    #find the integer sequences which sum to nums integer length
    n = len(nums)
    b, mid, e = [0], list(range(1, n)), [n]
    splits = (d for i in range(n) for d in combinations(mid, i)) 
    sequences = sorted([list(map(sub, chain(s, e), chain(b, s))) for s in splits])
    
    #create new list from sequences where sequence members are less than 3 (up to 2 will decode alphabet),
    #and the sequence sum is equal to nums integer length (remove incomplete sequences)
    sequences_filtered = [i for i in [[num for num in i if num < 3] for i in sequences] if sum(i) == n]
    
    #build list of decoded sequences
    for i in sequences_filtered:
        offset = 0
        sub = []
        for j in i:
            #each subsequent substring starts at the offset (end of last substring)
            letter = letters_lookup.get(nums[offset:j + offset])
            #If letter exists in letters_lookup, append sub
            if letter:
                sub.append(letter)
            #increment offset by length of last substring
            offset += j
        #append and format letter_combos
        letter_partitions.append(''.join(sub))
        
    return letter_partitions

letter_combinations(1123)