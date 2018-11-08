# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:13:27 2018

@author: dkochar

Enhance the divideTwoNumbers(num, denom) function to handle the Exception when
num or denom is a string. Handle that case by returning the string 
“Cannot divide strings”

"""

def divideTwoNumbers(num, denom):
	try:
		quotient = num/denom
	except (TypeError) as err:
		print("Cannot divide strings")
	else:
		print(f"{num} divided by {denom} is {quotient}")
        
print(divideTwoNumbers(1,'a'))
print(divideTwoNumbers(4,2))