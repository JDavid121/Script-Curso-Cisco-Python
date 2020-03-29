# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:47:53 2020

FIBONNACI FUNCTION

@author: David
"""

# Fibonnaci Function
# 1,1,2,3,5,8,13

def FibonacciFunc(n):
    if n<1:
        return None
    if n < 3:
        return 1
    fib1 = 1 # first element of Fibonnaci element
    fib2 = 1 # second element of Fibonnaci element
    fibsum = 0 # cumulative Fibonacci
    for i in range(3,n+1):
        fibsum = fib1 + fib2 #cumulative = 2
        fib1,fib2 = fib2,fibsum # to determinate next Fibonnaci element
    return fibsum
# Test the function
for i in range(10):
    print(i,"->",FibonacciFunc(i))
        