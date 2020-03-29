# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 12:55:08 2020

BUBBLE SORT

@author: David
"""
numbers = [10,7,8,1,9,6,4,5,2,3,0,11,14,12,19,18,15,13,12,17,16]
print(numbers)
swapped = True
a = 0
#Bubble sort method:
while swapped:
    swapped = False # No swapped occur
    
    for i in range(len(numbers)-1):
        
        if numbers[i] > numbers[i+1]: # Swapped happends
            swapped = True            # Continue in while loop.
            numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
    a = a + 1 # Number of loop for pass
print(numbers)
print("The number of loop for pass is:\t",a)
