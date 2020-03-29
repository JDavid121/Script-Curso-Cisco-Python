# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 22:11:20 2020

EXCERCISES

@author: David
"""
# Exercise 1:
# What is the output of the following snippet?

l1 = ["A", "B", "C"]
l2 = l1
l3 = l2

del l1[0]
del l2[0]

print(l3) # "C"

# Exercise 2:
# What is the output of the following snippet?

l1 = ["A", "B", "C"]
l2 = l1
l3 = l2

del l1[0]
del l2 # Does nothing, because doesn't use slices

print(l3)

# Exercise 3:
# What is the output of the following snippet?


l1 = ["A", "B", "C"]
l2 = l1
l3 = l2

del l1[0] # ["B","C"]
del l2[:] # All operations are maded in l1

print(l3) # []

# Exercise 4:
# What is the output of the following snippet?

l1 = ["A", "B", "C"]
l2 = l1[:] # l2 = ["A", "B", "C"]
l3 = l2[:] # l3 = ["A", "B", "C"]

del l1[0] #["B","C"]
del l2[0] #["B","C"]

print(l3) #["A", "B", "C"]

# Exercise 5:
# Insert in or not in instead of ??? so that the code outputs the expected result.

myList = [1, 2, "in", True, "ABC"]

print(1 in myList) # outputs True
print("A" not in myList) # outputs True
print(3 not in myList) # outputs True
print(False in myList) # outputs False
