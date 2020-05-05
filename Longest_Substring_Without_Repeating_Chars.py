# -*- coding: utf-8 -*-
"""
Created on Tue May  5 09:02:11 2020

@author: dkochar1

Given a string, find the length of the longest substring without repeating characters

"""

def substr_no_repeat(test_string):
    
    lst = []
    
    for i in range(0, len(test_string)-1):
        for j in range(i, len(test_string)-1):
            sub_string = test_string[i:j+2]
            for k in range(0, len(sub_string)):
                counter = 0
                if sub_string[k-1] == sub_string[k]:
                    counter += 1
                    break
            if counter == 0:
                lst.append(sub_string)
            
    return(len(max(lst, key = len)))

substr_no_repeat('abbcde')