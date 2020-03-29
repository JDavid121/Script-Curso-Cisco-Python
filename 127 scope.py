# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 10:47:13 2020

SCOPE EXERCISES

@author: David
"""
# functions and scopes
def myFunction():
    print("Do I know that variable?", var)

var = 1 # var scope: code when a var is properly defined.
myFunction() #this function takes var value in line 13
print(var) # prints var value

def myFunction():
    var = 2 # var scope. var is defined inside the function, the var scope is 
            # the function
    print("Do I know that variable?", var)

var = 1 # var scope: code from line 22
myFunction() # change var scope. inside function.
print(var) #return to var scope from line 22
