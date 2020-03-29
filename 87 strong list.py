# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:43:37 2020

@author: David
"""

list1 = [1]
list2 = list1
print(list2)
list1[0] = 2
print(list2)

list1 = [1]
list2 = list1[:]
list1[0] = 2
print(list2)

print("******************")
myList = [10, 8, 6, 4, 2]
print(myList)
newList = myList[1:3]
print(newList)