# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 10:09:52 2018

@author: DK
"""

def contains_purple(*args):
    if "purple" in args:
        return True
    return False

contains_purple(25, "purple")

def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word

combine_words("child")

<<<<<<< HEAD
# Write a lambda that accepts a single number and cubes it. Save it in a variable called cube.
cube = lambda num: num**3

cube(2)

#nums = [1,2,3,4]
#map(lambda x: x*2, nums)

def decrement_list(lst):
    return list(map(lambda x: x-1, lst))

decrement_list([1,2,3])

def remove_negatives(lst):
    return list(filter(lambda x: x >= 0, lst))

remove_negatives([-1, 3, 4, -99])
=======
# NO TOUCHING! =================================================================
def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
# NO TOUCHING! =================================================================

# Write your code below:

result1 = count_sevens(1,4,7)

result2 = count_sevens(*nums)
print(result2)

'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''

def calculate(make_float, operation, first, second, message="The result is"):
    if make_float:
        if operation == "divide":
            return message + " " + str(first / second)
        elif operation == "multiply":
            return message + " " + str(first * second)
    elif operation == "add":
        return message + " " + str(first + second)
    
def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final

calculate(make_float=False, operation='add', message='You just added', first=2, second=4)
>>>>>>> 1ac7b42825c046edbe53d0693ea686ed1591f1c3
