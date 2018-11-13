# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:15:43 2018

@author: DK

-Take 15 minutes to create a class in Python.
-Remember to include properties and methods.
-Then, take 5 minutes to share your class with your
classmates.
-If you defined your class well, your classmates will
be able to create and do things with objects of your
class.
"""
#Class "BankAccount" allows the creation of bank account, initialized with a
#name and zero dollar balance. Deposits and withdrawals are the primary methods

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