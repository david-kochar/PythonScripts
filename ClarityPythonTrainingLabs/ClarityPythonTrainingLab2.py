# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:00:17 2018

@author: dkochar

Write a program which calculates a student’s letter grade based on their score. 
Default score should be 100. Use the following logic. if ...
score is greater than or equal to 90, then it is an A
score is greater than or equal to 80, then it is a B
score is greater than or equal to 70, then it is a C
score is greater than or equal to 60, then it is a D
else for all other score, it is an F

"""

def score_grader(score=100):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return (f"The letter grade is {grade}")
