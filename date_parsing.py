# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:25:48 2020

@author: kocha
"""

import re

def parse_date(date_string):
    date_regex = re.compile(r'^(?P<d>\d{2})[\/\,\.](?P<m>\d{2})[\/\,\.](?P<y>\d{4})$')
    matches = date_regex.search(date_string)
    if bool(date_regex.search(date_string)):
        return {"d":matches.group("d"), "m":matches.group("m"), "y":matches.group("y")}

parse_date("12,04,2003")
parse_date("12,04,200312")