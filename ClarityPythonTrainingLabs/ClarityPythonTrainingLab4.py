# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:26:56 2018

@author: dkochar

This script appears to be working when testing the ideal scenario 
(2 arguments passed), but what happens if it is used improperly?
Is this script catching enough common error types? What error types can you 
experience in testing? How can you correct this script such that it averages 
numbers correctly?

    try:
        print("Argument 1: " + sys.argv[1])
        print("Argument 2: " + sys.argv[2])
        arg1 = int(sys.argv[1])
        arg2 = int(sys.argv[2])
    except TypeError:
        print("Error: Cannot perform addition on non-numeric values")
        sys.exit(1)
    except IndexError:
        print("Error: This script requires two arguments")
        sys.exit(1)
    else:
        average = (arg1 + arg2) / len(sys.argv[1:])
        print("Average   : " + str(average))

"""
import sys

def mean_calculator(*args):
    try:
        lst = list(map(int, sys.argv[1:]))
        for arg in lst:
            print(f"Argument {lst.index(arg)+1}: {arg}")
    except ValueError as val_err:
        print(val_err)
        print("Please provide only numeric values")
        sys.exit(1)
    try:
        mean = sum(lst) / len(lst)
    except ZeroDivisionError as div_zero_err:
        print(div_zero_err)
        print("Please provide at least one value")
        sys.exit(1)
    else:
        print(f"Average   : {mean}") 

mean_calculator(*sys.argv[1:])
