# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:44:55 2020

@author: David
"""

# break - example

print("The break instruction:")
for i in range(0, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(0, 10):
    if i == 4:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")