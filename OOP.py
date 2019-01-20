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

"""
Define a new class called "BankAccount"
Each bank account should have an owner
Each bank account should have a balance attribute, with default $0.00
Each instance should have a deposit method which adds to and returns
the balance
Each instance should have a withdraw method
"""

class BankAccount:
    
    def __init__(self, name):
        self.name    = name
        self.balance = 0.00
        
    def getBalance(self):
        return f"Balance is {self.balance}"
    
    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        return f"Balance is {self.balance}"
    
    def withdraw(self, withdrawal_amount):
        self.balance -= withdrawal_amount
        return f"Balance is {self.balance}"
    
acct = BankAccount("Darcy", 1000)

acct.getBalance()

acct.owner
acct.balance
acct.deposit(10)
acct.withdraw(3)
acct.balance
    
"""
Create a Chicken class, where each Chicken has a name, species, and eggs 
(nunber of eggs laid, starting at 0).

Each Chicken should also have an instance method called lay_egg() which should
increment and then return that particular Chicken's eggs attribute. lay_egg()
should also increment a class variable called total_eggs
"""
class Chicken:
    
    total_eggs = 0
    
    def __init__(self, name, species):
        self.name    = name
        self.species = species
        self.eggs    = 0
        
    def lay_egg(self):
        self.eggs          += 1
        Chicken.total_eggs += 1
        return self.eggs
    
c1 = Chicken(name = "Alice", species = "Partridge Silkie")
c2 = Chicken(name = "Amelia", species = "Speckled Sussex")
Chicken.total_eggs
c1.lay_egg()
Chicken.total_eggs
c2.lay_egg()
Chicken.total_eggs
c2.lay_egg()
Chicken.total_eggs

"""
Define a base class "Character" with name, hp (hit points), level
(experience level)

Also, define  a subclass "NPC" (Non-playing character) that inherits from
Character, and has an additional instance method called speak which prints the
speech the character would say when a player interacts with them
"""

class Character:
    
    def __init__(self, name, hp, level):
        self.name  = name
        self.hp    = hp
        self.level = level
        
class NPC(Character):
    
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)
        self.name  = name
        self.hp    = hp
        self.level = level
    
    def speak(self):
        print("I heard there were monsters running around last night!")

villager = NPC("Bob", 100, 12)
villager.name
villager.hp
villager.level
villager.speak()















