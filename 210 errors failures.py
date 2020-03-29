# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:23:09 2020

@author: David
"""

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ValueError:
    print("You must enter an integer value.")

print("THE END.")