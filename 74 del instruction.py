# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 23:19:59 2020

Indexing list

@author: David
"""

number = [10,2,3,12,4,6,8]
print(number)
del (number[0]) # delete number[0] from the list number
print(number)   # del is an instruction (not a function)
                # del reduces the length of the list by one.
number[6] = 1 #you can not change the value of a element that doesn´ exist.
print(number[6]) # IndexError list index out of range.

number = [10,11,12,19,15]
print(number)
print("number[-1] = ",number[-1])
print("number[-2] = ",number[-2])
print("number[-3] = ",number[-3])
print("number[-4] = ",number[-4])
print("number[-5] = ",number[-5])
print("number[-6] = ",number[-6]) # IndexError: list index out of range