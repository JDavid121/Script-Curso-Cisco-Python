# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 00:29:55 2020
EXERCISES
@author: David
"""
# Exercise 1:
# What is the output of the following snippet?
def hi():
    return
    print("Hi!") #This line does not be reachadable.

hi() # None
# Exercise 2
# What is the output of the following snippet?
def isInt(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(isInt(5)) #True
print(isInt(5.0)) #False
print(isInt("5")) #None

# Exercise 3
# What is the output of the following snippet?
def evenNumLst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst

print(evenNumLst(11))
# [0, 2, 4, 6, 8, 10]

# Exercise 4
# What is the output of the following snippet?

def listUpdater(lst):
    updList = []
    for elem in lst:
        elem **= 2
        updList.append(elem)
    return updList

l = [1, 2, 3, 4, 5]
print(listUpdater(l))
# [1, 4, 9, 16, 25]