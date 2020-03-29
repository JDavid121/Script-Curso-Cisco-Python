# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:19:03 2020

errors and fails handle

@author: David
"""

# errors and exceptions handle

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ValueError:
    print("You must enter an integer value.")
except: # general exeption handle
    print("Oh dear, something went wrong...")

print("THE END.")
