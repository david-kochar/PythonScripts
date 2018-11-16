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
        for y in range(1, num2 - (num2 - (x + 1))):
            if x % y == 0:
                lst.append(x)
    return set([i for i in lst if lst.count(i) <= 2])
 
exam_grades_under_50 = find_primes(2,50)
exam_grades_under_20 = sorted(exam_grades_under_50.difference(find_primes(21,50)))
exam_grades_under_50_over_20 = sorted(exam_grades_under_50.difference(exam_grades_under_20))

print(f"Exam grades under 50 are {exam_grades_under_50}")
print(f"Exam grades under 20 are {exam_grades_under_20}")
print(f"Exam grades under 50 and over 20 are {exam_grades_under_50_over_20}")