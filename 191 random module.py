# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 10:05:47 2020

@author: David
"""

from random import random,seed
# random() function that generates a float random number
# 0.0 <= random() <1.0
for i in range (5):
    print(random())

# seed()        : Put the algorithm seed in a current time
# seed(int_val) : sets the seed with the integer value int_val 
seed(10)
print("**********************")
for i in range (5):
    print(random())
    