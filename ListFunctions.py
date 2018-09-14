# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 20:38:36 2018

@author: dkochar
"""

instructors = []

instructors.extend(["Colt","Blue", "Lisa"])

print(instructors)

names = ["John", "David", "John"]

for i in names:
    names.remove("John")

print(names)

names = ["John", "David", "John"]
idxs = []
nameslen = len(names)

names.index("John", 0, nameslen)

for i in names:
   idxs = names.index("John", 0, nameslen)

print(idxs)
