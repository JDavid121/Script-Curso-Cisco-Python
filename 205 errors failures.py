# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 09:51:21 2020

errors and fails

@author: David
"""

firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))

try:
    print(firstNumber / secondNumber)
except:
    print("This operation cannot be done.")

print("THE END.")