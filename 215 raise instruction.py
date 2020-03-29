# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:49:29 2020

RAISE INSTRUCTION

@author: David
"""

#   The raise instruction raises the specified exception
#   as if it was raised in a normal (natural) way

def badFun(n):
    raise ZeroDivisionError

try:
    badFun(0)
except ArithmeticError:
    print("What happend? An error?")
print("The End")

# In this way, you can test your exception handling routine 
# without forcing the code to do stupid things
    

