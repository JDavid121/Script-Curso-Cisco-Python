# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 23:31:09 2020

Objectives
Familiarize the student with:

using basic instructions related to lists;
creating and modifying lists.

Scenario
There once was a hat. The hat contained no rabbit, 
but a list of five numbers: 1, 2, 3, 4, and 5.

Your task is to:

1.0 write a line of code that prompts the user to replace 
the middle number in the list with an integer number entered by the user (step 1)

2.0 write a line of code that removes the last element from the list (step 2)

3.0 write a line of code that prints the length of the existing list (step 3.)
Ready for this challenge?

@author: David
"""

# Laboratory

hat = [1,2,3,4,5]
print(hat)
hat[2] = int(input("Enter a new value"))
print(hat)
del (hat[4])
print(hat)
print (len(hat))
