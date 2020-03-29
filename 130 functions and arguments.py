# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:46:55 2020

@author: David
"""

# part 1

def myFunction(n):
    print("I got", n)
    n += 1
    print("I have", n)

var = 1
myFunction(var)
print(var)

def myFunction(myList1):
    print(myList1)
    myList1 = [0, 1]

myList2 = [2, 3]
myFunction(myList2)
print(myList2)