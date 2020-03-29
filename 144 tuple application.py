# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:30:06 2020

TUPLE APLICATION

@author: David
"""

myTuple = (1, 10, 100)

t1 = myTuple + (1000, 10000)
t2 = myTuple * 3

print(t1) # output: (1, 10, 100, 1000, 10000)
print(t2) # output: (1, 10, 100, 1, 10, 100, 1, 10, 100)
print(len(t2)) # output: 9
print(10 in myTuple) # True
print(11 in myTuple) # False
print(10 not in myTuple) # False
print(11 not in myTuple) # True.
#print(len(t2))
#print(t1)
#print(t2)
#print(10 in myTuple)
#print(-10 not in myTuple)
