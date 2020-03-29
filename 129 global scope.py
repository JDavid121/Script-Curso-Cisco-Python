# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:38:13 2020

@author: David
"""

def myFunction():
    global var #global scope
    var = 2
    print("Do I know that variable?", var)

var = 1
myFunction() # global scope var = 2
print(var)   # var = 2 from global scope