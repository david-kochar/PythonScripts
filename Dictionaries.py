# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 11:49:54 2018

@author: DK
"""

user_info = { "user_name" : "dkochar", "email_address" : "kocha017@gmail.com", "zip_code" : "55401" }

artist = {
    "first" : "Neil",
    "last" : "Young"
}

full_name = artist["first"] + " " + artist["last"]

print(full_name)

# DON'T TOUCH PLEASE!
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# DON'T TOUCH PLEASE!


# Use a loop to add together all the donations and store the resulting number in a variable called total_donations

total_donations = 0

for v in donations.values():
    total_donations += v

print(total_donations)

# This code picks a random food item:    
#from random import choice #DON'T CHANGE!
#food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

food = ["morning bun", "tea cake"]

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:

#if food in bakery_stock.keys():
#    print(f"{bakery_stock[food]} left")
#else:
#    print ("We don't make that")
    
for i in food:
    for j in bakery_stock.keys():
        if j == i:
            print(i)
        else:
            print ("We don't make that")

#DO NOT TOUCH game_properties!
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notications", "achievements"] 

# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0.  Save the result to a variabled called initial_game_state
initial_game_state = dict.fromkeys (game_properties, 0)

print(initial_game_state)

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD

stock_list = {}
stock_list.update(inventory)

# add the value 18 to stock_list under the key "cookie"

stock_list.update({'cookie':18})

# remove 'cake' from stock_list USE A DICTIONARY METHOD

stock_list.pop('cake')

print(stock_list)

#Combine the lists into a dictionary
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = { list1[i]:list2[i] for i in range(0, len(list1)) }
print(answer)

#For each list in the dictionary "person," create key-value pairs where the first item of each list is the key
#and the second item is the value
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

person_key = [i[0] for i in person]

print(person_key)

# use the person variable in your answer
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = dict(person)
print(answer)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = { k:v for k,v in person }
print(answer)   

answer = {k:0 for k in ["a", "e", "i", "o", "u"]}
print(answer)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {thing[0]: thing[1] for thing in person}
print(answer)

for i in range(65,91):
    print(chr(i))
    
answer = {k:chr(k) for k in range(65,91)}
print(answer)