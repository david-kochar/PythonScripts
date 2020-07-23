# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:52:07 2020

@author: kocha
"""

import re

'''
def is_valid_time(time_string):
    time_regex = re.compile(r'^\d{1,2}:\d{2}$')
    match = time_regex.search(time_string)
    if match:
    	return True
    return False
'''

def is_valid_time(time_string):
    time_regex = re.compile(r'^\d{1,2}:\d{2}$')
    return bool(time_regex.search(time_string))
    
is_valid_time("1:23")
