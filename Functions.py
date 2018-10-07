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