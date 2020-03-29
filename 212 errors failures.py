# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:33:26 2020

@author: David
"""

try:
    y = 1 / 0


except ArithmeticError: 
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero division error")

print("THE END.")