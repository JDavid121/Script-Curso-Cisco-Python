# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 10:05:43 2020

@author: David
"""

# Create a list
mylist = [] # empty list
            # the first element created, the first introduced
for i in range(5):
    mylist.append(i+1)
print(mylist)
           #[1,2,3,4,5]

mylist = [] #empty list
           #the first element created, the last element introduced
for i in range(5):
    mylist.insert(0,i+1)
print(mylist)
          # [5,4,3,2,1]