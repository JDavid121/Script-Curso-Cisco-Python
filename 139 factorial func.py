# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 00:17:13 2020

FACTORIAL FUNCTION

@author: David
"""
# Determinate Factorial func
# 0! = 1
# 1! = 1*1 = 1
# 2! = 1*2 = 2
# 3! = 1*2*3 = 6
# n! = 1*2*3*...*(n-1)*n

def factorialFun(n):
    fact = 1 #factorial result
    if n < 0:
        return None
    if n == 0:
        return 1
    if n == 1:
        return 1
    for i in range (2,n+1):
        fact = fact*i
    return fact

# testing functions
for n in range(1, 6): # testing
    print(n, factorialFun(n))
