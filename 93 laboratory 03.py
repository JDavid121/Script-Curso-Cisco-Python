# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 09:55:03 2020

SORT LIST

@author: David
"""

myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newlist = []

# Evaluate the list

for i in range(len(myList)):
    if (myList[i] not in newlist):
        newlist.append(myList[i])
print (newlist)