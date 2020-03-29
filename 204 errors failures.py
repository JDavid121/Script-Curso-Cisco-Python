# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 09:49:18 2020

errors and failures

@author: David
"""

firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))

if secondNumber != 0:
    print(firstNumber / secondNumber)
else:
    print("This operation cannot be done.")

print("THE END.")

