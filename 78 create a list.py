# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 10:48:59 2020

@author: David
"""

number = [1,2,3,4,5,6,7]
total_sum = 0

print(number)

for i in number:    # first form to evaluate a list
    total_sum = total_sum + i
print (total_sum)

print ("**********************")
total_sum = 0      # second form to evaluate a list.
for i in range (len(number)):
    total_sum = total_sum + number[i]
print (total_sum)