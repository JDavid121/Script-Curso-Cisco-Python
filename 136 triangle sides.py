# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 22:58:48 2020

Function that indicates if we can built a triangle using three sides as
a input.
The function output is true when it is possible
The functiion is false when it is not possible.

Note: With three sides as a input, a triangle can be made only if the sum
of two arbitrary sides is longer than the third side.

We know from school that the sum of two arbitrary sides has to be longer 
than the third side.

@author: David
"""
# **************************
# original function

def isaTriangle(a,b,c):
    if (a+b) > c:
        if (b+c) > a:
            if (a+c) > b:        
                return True
            else:
                return False
        else:
            return False
    else:
        return False
# ****************************
# Example 1
def isItATriangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

# ****************************
# Example 2

def isItATriangle2(a, b, c):
    if a + b <= c or b + c <= a or \
    c + a <= b:
        return False
    return True

# ***************************
# Example 3

def isItATriangle3(a, b, c):
    return a + b > c and b + c > a and c + a > b
# ***************************
# Test
print(isItATriangle(1, 1, 1))
print(isItATriangle(1, 1, 3))

