# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 14:47:47 2020

@author: kocha
"""

import re

def censor(phrase):
    pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    return pattern.sub("CENSORED", phrase)

censor("I hope you fracking die")
    