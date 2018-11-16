# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 12:44:50 2018

@author: DK

Given this list of student names:

["morgan", "david", "jeff", "david", "clara", "morgan", "david"]

Write a function that prints out how many times a name occurs in the list

"""

def name_occurence(lst):
    name_counts = {k:lst.count(k) for k in lst}
    for k,v in name_counts.items():
        print(f"{k} has {v} occurence(s)")

name_occurence(["morgan", "david", "jeff", "david", "clara", "morgan", "david"])