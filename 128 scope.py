# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:04:48 2020

FUNCTIONS AND SCOPES

@author: David
"""
#define a function:

def avrprint():
    print("Var has the following value",var)

var = 1 # var scope: 14 line
avrprint() # var scope inside the function
print(var)

def avrprint2():
    var = 2 #defined var value = 2
    print("Var inside the function has the value",var)
var = 10 # var scope : 21 line
avrprint2() # invoke the function
print(var)