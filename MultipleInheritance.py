# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 16:01:03 2020

@author: kocha
"""

# Define your classes below:
class Mother:
    def __init__(self):
        self.eye_color  = "brown"
        self.hair_color = "dark brown"
        self.hair_type  = "curly"
    
class Father:
    def __init__(self):
        self.eye_color  = "blue"
        self.hair_color = "blond"
        self.hair_type  = "straight"

class Child(Mother, Father):
    def __init__(self):
        super().__init__()
    
    def __repr__(self):
        return f"The child has {self.eye_color} eyes, and {self.hair_type}, and {self.hair_color} hair"
        
Jane = Mother()

John = Father()

Dave = Child()

print(Dave)