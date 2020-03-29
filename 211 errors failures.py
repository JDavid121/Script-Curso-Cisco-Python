# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:27:01 2020

errors and failures

@author: David
"""

try:
    y = 1 / 0
except ArithmeticError:
    print("Oooppsss...")

print("THE END.")