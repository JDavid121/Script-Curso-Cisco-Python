# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:40:21 2020

errors and failures

@author: David
"""

def badFun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None

badFun(0)

print("THE END.")