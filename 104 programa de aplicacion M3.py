# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 23:57:06 2020

CREATE A LIST

@author: David
"""
# A list always numbered starting from zero
num = [10,12,5,8,2,13,20]
# print the first element of the list:
print(num[0]) # R: 10
#print all the elements of the list:
print("**************")
for i in num: #indexing a list (form 1)
    print(i)
print("**************")
for i in range(len(num)): #indexing a list (form 2)
    print(num[i])
# Toogle elements num[0] and num[1], print the list
num[0],num[1] = num[1],num[0]
print(num)

#Delete the fourth element
del(num[3])
print(num)
print(len(num))
#Delete the entire list
del(num)
print(num)
