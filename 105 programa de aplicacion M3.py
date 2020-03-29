# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 00:14:38 2020
LIST
@author: David
"""
# Create a list of the first 10 integer numbers:
newlist = [] #empty list
for i in range(10):
    newlist.append(i)
print (newlist)

#from the newlist, calculate the sum of their all elements.
total_sum = 0 #start of the sum
for i in range(len(newlist)):
    total_sum = total_sum + newlist[i]
print(total_sum)

# Second option:
total_sum = 0
for i in newlist: # You don't need a indexing here
    total_sum = total_sum + i
print(total_sum)

mylist = [10,8,6,4,2]
print(mylist)
newlist=mylist[-1:-3]
print(newlist)
# delete all the elements in a list. Make it empty
print(mylist)
del(mylist[:])
print(mylist)

# in and not in operators.
    
