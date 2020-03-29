# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 09:25:58 2020

SORT LIST

@author: David
"""

myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#myList = [1, 2, 4]
newlist=[] #empty list

# Charge the first value in the newlist

newlist.append(myList[0])

# To evaluate the list:
for i in range(len(myList)):
        if (myList[i] not in newlist): #evaluates if myList[i] not in newlist    
            newlist.append(myList[i])
myList = newlist[:]
print (myList)
    