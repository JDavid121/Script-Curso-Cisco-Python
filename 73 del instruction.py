# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 23:05:04 2020

@author: David
"""

number = [10,2,3,12,4,6,8]
print(number)
del (number[0]) # delete number[0] from the list number
print(number)   # del is an instruction (not a function)
                # del reduces the length of the list by one.
number[6] = 1 #you can not change the value of a element that doesn´ exist.
print(number[6]) # IndexError list index out of range.

