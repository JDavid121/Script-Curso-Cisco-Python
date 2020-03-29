# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:09:24 2020

errors and exception handle

@author: David
"""
# program that handle a various types of exceptions

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError: # Divide by zero error
    print("You cannot divide by zero, sorry.")
except ValueError: # Value entered must be a number.
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")
