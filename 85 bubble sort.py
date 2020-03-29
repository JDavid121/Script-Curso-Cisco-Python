# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:02:15 2020

BUBBLE SORT

INTERACTIVE VERSION

@author: David
"""

#numbers = [10,7,8,1,9,6,4,5,2,3,0,11,14,12,19,18,15,13,12,17,16]
#print(numbers)
swapped = True
a = 0

# How many data do you want to sort?
print("Program to sort a list of numbers")
a = int(input("How may data do you want to sort?\t"))
numbers = [] # Empty list
for i in range(1,a+1,1):
    b = int(input("Set the {} element...\t".format(i)))
    numbers.append(b)
print("The data sets are...")
print(numbers)
    


#Bubble sort method:
c = 0
while swapped:
    swapped = False # No swapped occur
    
    for i in range(len(numbers)-1):
        
        if numbers[i] > numbers[i+1]: # Swapped happends
            swapped = True            # Continue in while loop.
            numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
    c = c + 1 # Number of loop for pass
print("The numbers sorted are...")
print(numbers)
print("The loop's numbers for pass is:\t",c)

