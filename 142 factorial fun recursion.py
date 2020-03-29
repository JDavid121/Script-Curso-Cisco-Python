# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 12:11:55 2020

FACTORIAL FUNCTION

@author: David
"""

# Factorial function is also a recursion function
# n! = 1 x 2 x 3 x ... x (n-1) x n
# n! = (n-1)! x n

def factFunc(n):
    if n < 0:
        return None
    if n < 2: #Define initial values of factorial function
        return 1
    return n*factFunc(n-1) # n! = n * (n-1)!

# Test the factorial function
print(factFunc(5))
for i in range(11):    
    print(i,"->>",factFunc(i))
