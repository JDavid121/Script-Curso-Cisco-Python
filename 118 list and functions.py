# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 13:15:58 2020

@author: David
"""

def sumOfList(lst):
    sum = 0
    
    for elem in lst:
        sum += elem
    
    return sum

A = sumOfList([5,4,3])
print(A)