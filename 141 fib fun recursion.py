# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:31:07 2020

RECURSION FUNCTION

@author: David
"""
# recursion
# Fibonacci Function:
# Fib(i) = Fib(i-1) + Fib(i-2)
# The Fibonacci Function is a recursive function
# For a recursion function is important to define the initial values:
def fibo(n):
    if n<1: #define values for fibo(0)
        return None
    if n<3: # fibo(1) = 1, fibo(2) = 1
        return 1
    return fibo(n-1) + fibo(n-2)

# If you forget to consider the conditions which can stop the chain
# of recursive invocations, the program may enter an infinite loop. 
# You have to be careful.
    
# To test Fibonnaci Function
for i in range (1,10):
    print(i, "->>",fibo(i))