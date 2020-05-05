# -*- coding: utf-8 -*-
"""
Created on Mon May  4 18:31:13 2020

@author: kocha
"""

def unique_substrings(test_string):
    
    lst = []
    
    for i in range(0, len(test_string)):
        for j in range(i, len(test_string)):
            unique = []
            sub_string = test_string[i:j + 1]
            for char in sub_string[::]:
                if char not in unique:
                    unique.append(char)
            if len(unique) == len(sub_string):
                lst.append(sub_string)
    return(lst)


unique_substrings('abbcd')
