# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 12:22:11 2020

@author: David
"""
# swap elements in a list

mylist = [10,1,8,3,5]
print(mylist)
mylist[0],mylist[4] = mylist[4],mylist[0]
mylist[1],mylist[2] = mylist[2],mylist[1]
print(mylist)

# Swap elements i a for loop

myList = [10, 1, 8, 3, 5]
length = len(myList) # length = 5
print(myList)

# length // 2 = 2 (integer division)

for i in range(length // 2):
    myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]
    # myList[0],myList[2-0-1] = myList[2-0-1],myList[0]
    # myList[1],myList[1-0-1] = myList[1-0-1],myList[1]

print(myList)

print("***************************")
mylist = [11,12,13,14,15,16,17,18,19,20]
length = len(mylist)
print (mylist)

for i in range (length//2): #length//2 = 10//2 = 5
    mylist[i],mylist[length - i - 1] = mylist[length - i - 1],mylist[i]
    # mylist[0],mylist[10 - 0 - 1] = mylist[10 - 0 - 1],mylist[0]
    # mylist[1],mylist[10 - 1 - 1] = mylist[10 - 1 - 1],mylist[1]
    # ...
    # mylist[4],mylist[10 - 4 - 1] = mylist[10 - 4 - 1],mylist[4]
    
print(mylist)