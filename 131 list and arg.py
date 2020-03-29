# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:53:34 2020

@author: David
"""

def myFunction(myList1):
    print(myList1)
    myList1 = [0, 1]

myList2 = [2, 3]
myFunction(myList2) #prints myList2
print(myList2) #also prints myList2

# *********************************

def myFunction1(myList1):
    print(myList1)
    del myList1[0] #modify myList2. It changes

myList2 = [2, 3]
myFunction1(myList2) #print original myList2
print(myList2) #print modifided myList2