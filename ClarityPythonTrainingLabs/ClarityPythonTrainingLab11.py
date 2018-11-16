# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 13:50:51 2018

Create and output a set, exam_grades_under_50, containing the prime numbers 
under 50.

@author: DK
"""
def find_primes(r):
    r = r + 1
    lst = []
    
    for x in range(1,r):
        for y in range(1, r - (r-(x+1))):
            if x % y == 0:
                lst.append(x)
    primes = set([i for i in lst if lst.count(i) <= 2])
    
    print(primes)

find_primes(50)
