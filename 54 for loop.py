# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:09:32 2020

Let's have a look at a short program 
whose task is to write some of the first powers of two:

@author: David
"""

a = 1
b = 0
for exp in range(4):
    print("2 to the power of", exp, "is", a)
    b = b+a
    a = a*2
print ("La suma de los granos de arroz es:",b)
