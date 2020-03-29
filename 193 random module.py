# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 11:16:27 2020

@author: David
"""

from random import randint, choice, sample

for i in range(10):
    print(randint(1, 10), end=',')
print("")

print("***************************")

# generate a list of numbers from 0 to 10
alist = [] 
for i in range(11):
    alist.append(i)
print(alist)

print("***************************")
print(choice(alist)) #choice an random number from alist
print(sample(alist,5)) # prints a list sample of 5 elements from the alist
print(sample(alist,3)) #sample() function makes a random list from "alist"

# example with string
print("***************************")
word = "dicctionary"
blist = []
for i in word:
    blist.append(i)
print(blist)

print("***************************")
print(choice(blist))
print (sample(blist,3))
print(sample(blist,7))