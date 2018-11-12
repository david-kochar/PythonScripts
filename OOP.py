# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 13:42:04 2018

@author: DK
"""

# define the Vehicle class below:
class Vehicle:
    pass
# instantiate a new Vehicle and save it to a variable called car:
car = Vehicle()
# instantiate a new Vehicle and save it to a variable called boat:
boat = Vehicle()

class Comment:
    
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text     = text
        self.likes    = likes
        
c = Comment("davey123", "lol you're so silly", 3)

print(c.username)
print(c.text)
print(c.likes)