# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:26:56 2018

@author: dkochar

This script appears to be working when testing the ideal scenario 
(2 arguments passed), but what happens if it is used improperly?
Is this script catching enough common error types? What error types can you 
experience in testing? How can you correct this script such that it averages 
numbers correctly?

"""
from sys import argv

def mean_calculator(*args):
    lst = list(map(int, argv[1:]))
    for arg in lst:
        print(f"Argument {lst.index(arg)+1}: {arg}")
    #args = list(args)
    #print(args)
    #for i in args:
    #    print(f"Argument {i}: {argv[i]}")

mean_calculator(*argv[1:])
"""
def mean_calculator(nums):
    mean = sum(num for num in nums) / len(nums)
    print(str(mean))
    for i in sys.argv:
        print(str(i))
    #return [print(f"Index {nums.index(num)} number is {num}") for num in nums]
    #mean = sum(nums) / len(list(nums))
    #return print(str(mean))
    #mean = sum(num for num in args) / len(args)
    #return(f"The average of thse numbers is {mean}")
#map(int, raw_input("Enter your list of numbers : ").split(",")) 
nums = list(map(int, input("Enter your list of numbers, separated by commas : ").split(",")))

mean_calculator(nums)
"""
    
"""    
    try:
        print("Argument 1: " + sys.argv[1])
        print("Argument 2: " + sys.argv[2])
        arg1 = int(sys.argv[1])
        arg2 = int(sys.argv[2])
    except TypeError:
        print("Error: Cannot perform addition on non-numeric values" )
        sys.exit(1)
    except IndexError:
        print("Error: This script requires two arguments")
        sys.exit(1)
    else:
        average = (arg1 + arg2) / len(sys.argv[1:])
        print("Average   : " + str(average))
"""