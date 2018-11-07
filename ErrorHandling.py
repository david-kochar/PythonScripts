# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 13:16:28 2018

@author: DK
"""

# Write a function called divide, which accepts two parameters (you can call them num1 and num2). 
# The function should return the result of num1 divided by num2. If you do not pass the correct amount of arguments to the function, 
# it should return the string "Please provide two integers or floats". If you pass as the second argument a 0, Python will raise a ZeroDivisionError, 
# so if this function is invoked with a 0 as the value of num2, return the string "Please do not divide by zero"

    # Examples
    
    # divide(4,2)  2
    # divide([],"1")  "Please provide two integers or floats"
    # divide(1,0)  "Please do not divide by zero"

"""   
def divide(num1, num2):
    if not all([type(i) in (int,float) for i in [num1, num2]]):
        raise TypeError("Please provide two integers or floats")
    if num2 == 0:
        raise ZeroDivisionError ("Please do not divide by zero")
    return num1 / num2
"""

def divide(a,b):
    try:
        total = a / b
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    return total