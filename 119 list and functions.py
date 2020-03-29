# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 13:20:53 2020

@author: David
"""
# A list as a function output.

def strangeListFunction(n):
    strangeList = [] # empty list
    
    for i in range(0, n):
        strangeList.insert(0, i) # insert i at the begining of the list.
    
    return strangeList # strangeList return of the function.

print(strangeListFunction(5))