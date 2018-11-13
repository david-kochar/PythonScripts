# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:23:12 2018

@author: DK

Make the following more readable with literate programming:
    
class aClassName():
    def __init__(self):
        return
    def method1(self, arg1, arg2):
        return arg1 + arg2
    def method2(self, arg1, arg2):
        return arg1 - arg2
    def method3(self, arg1, arg2):
        return arg1 * arg2
    def method4(self, arg1, arg2):
        return arg1 / arg2
    if __name__ == "__main__":
        object = aClassName()
        print(object.method1(1,2))
        print(object.method2(1,2))
        print(object.method3(1,2))
        print(object.method4(1,2))

"""

class aSimpleCalculator():
    def __init__(self):
        return
    def addition(self, num1, num2):
        return num1 + num2
    def subtraction(self, num1, num2):
        return num1 - num2
    def multiplication(self, num1, num2):
        return num1 * num2
    def division(self, num1, num2):
        return num1 / num2
    
if __name__ == "__main__":
    object = aSimpleCalculator()
    print(object.addition(1,2))
    print(object.subtraction(1,2))
    print(object.multiplication(1,2))
    print(object.division(1,2))