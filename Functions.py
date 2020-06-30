# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 19:23:40 2018

@author: dkochar
"""
#Define a function that prints "THE CROWD GOES WILD"

#Define your make_noise function below
def make_noise():
    print("THE CROWD GOES WILD")


#Then, call make_noise once:
make_noise()

#create a coin-flipping function
from random import random
def flip_coin():
    r = random()
    if r > 0.5:
        return "Heads"
    else:
        return "Tails"
    
print(flip_coin())

def speak_pig():
    return ("oink")

speak_pig()

def generate_evens():
    return [num for num in range(1,50) if num % 2 == 0]

generate_evens()

print(2**8)

def yell(string):
    return string.upper() + "!"

def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"

def speak(animal='dog'):
    noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
    return noises.get(animal, '?')

def product(num1, num2):
    return num1 * num2

product(2,2) # 4
product(2,-2) # -4

def return_day(day):
    day_of_week = {1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 7:'Saturday'}
    return day_of_week.get(day, 'None')

return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None

def last_element(l):
    if len(l) > 0:
        return l[-1]
    return None
    
last_element([1,2,3])

def number_compare(num1, num2):
    if num1 != num2:
        if num1 > num2:
            return "First is greater"
        return "Second is greater"
    return "Numbers are equal"

number_compare(2,1)

#define single_letter_count below:

def single_letter_count(word, letter):
    letter = letter.lower()
    word = word.lower()
    if letter in word:
        return word.count(letter)
    return 0

def single_letter_count(string,letter):
    return string.lower().count(letter.lower())

single_letter_count("Hello World", "h")

def multiple_letter_count(word):
    return { i:word.count(i) for i in word }

multiple_letter_count("awesome")
    
def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection

chars = "H s  t"

chars = chars.lower().replace(" ", "")

print(chars)
    
def is_palindrome(chars):
    chars = chars.lower().replace(" ", "")
    if chars == chars[::-1]:
        return True
    return False

is_palindrome('amanaplanacanalpanama')

def frequency(lst, search_term):
    return lst.count(search_term) 

frequency([1,2,3,4,4,4], 4)

def multiply_even_numbers(lst):
    total = 1
    for val in lst:
        if val % 2 == 0:
            total *= val
    return total

multiply_even_numbers([2,3,4,5,6])

def capitalize(chars):
    return chars[0].upper() + chars[1:]

capitalize("tim")
        
def compact(lst):
    return [ item for item in lst if item ]

compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]


# flesh out intersection pleaseeeee
def intersection(a, b):
    return list(set(a) & set(b))

def isEven(num):
    return num % 2 == 0

lst = [1,2,3,4]
truthy_set = [num for num in lst if isEven(num)]

print(truthy_set)

def partition(lst, isEven):
    truthy_set = set([num for num in lst if isEven(num)])
    falsy_set  = set(lst) ^ truthy_set
    return [list(truthy_set), list(falsy_set)]

#def partition(lst, fn):
#    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]
    
power = 5
print(len(range(power)))

for i in range(6):
    result = i
    
print(result)

def exponent_calc(num, power):
    total = 1
    for i in range(power):
        total *= num
    return total

exponent_calc(2,3)