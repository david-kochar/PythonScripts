# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:12:50 2018

@author: DK
"""

import math

answer = math.sqrt(15129)

import keyword

def contains_keyword(*args):
    if [item for item in args if keyword.iskeyword(item)]:
        return True
    return False

contains_keyword("def", "lol")

