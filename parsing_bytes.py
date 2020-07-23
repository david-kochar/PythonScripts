# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:52:30 2020

@author: kocha
"""

import re

def parse_bytes(string):
    bytes_regex = re.compile(r'\b[0-1]{8}\b')
    return bytes_regex.findall(string)
    
parse_bytes("my data is: 10101010 11100010")
