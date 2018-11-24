# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 13:50:51 2018

Create and output a set, exam_grades_under_50, containing the prime numbers 
under 50.

Create and output a set, exam_grade_under_20, containing the prime numbers 
under 20, derived from the set in step (1).

Create and output a set, exam_grades_under_50_over_20, containing the prime
numbers under 50 and over 20, by utilizing the sets from steps (1) and (2).

@author: DK
"""

def find_primes(num1, num2):
    
    lst = []
    
    for x in range(num1, num2):
        factor_counter = 0
        for y in range(1, num2, 1): #for y in range(1, num2 - (num2 - (x + 1))):
            if x % y == 0:
                factor_counter += 1
            if factor_counter > 2:
                break
        if factor_counter == 2:
            lst.append(x)
    return set(lst)

exam_grades_under_50 = find_primes(2,50)
exam_grades_under_20 = exam_grades_under_50.difference(find_primes(21,50))
exam_grades_under_50_over_20 = exam_grades_under_50.difference(exam_grades_under_20)

print(f"Exam grades under 50 are {exam_grades_under_50}")
print(f"Exam grades under 20 are {exam_grades_under_20}")
print(f"Exam grades under 50 and over 20 are {exam_grades_under_50_over_20}")

"""
lst = []

for x in range(2, 11):
    factor_counter = 0
    for y in range(1, 11, 1): #for y in range(1, num2 - (num2 - (x + 1))):
        if x % y == 0:
            factor_counter += 1
        if factor_counter > 2:
            break
    if factor_counter == 2:
        lst.append(x)
        
print(lst)
"""
