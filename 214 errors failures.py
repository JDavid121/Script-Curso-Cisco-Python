# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:44:46 2020

errors and failures

@author: David
"""
def badFun(n):
    return 1/n
try:
    badFun(0)
except ArithmeticError:
    print("What happend? An exception was raised!")

print("The end")

