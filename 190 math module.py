# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 10:47:39 2020

@author: David
"""

# math functions

from math import ceil,floor,trunc

x = 1.2
print(x)
print(ceil(x))

x = 2.0
print(x)
print(ceil(x))

x = 3.7
print(x)
print(ceil(x))

# ceil(x) returns the smallest integer value 
# greater than or equal to x

print("**************")
x = 1.2
print(x)
print(floor(x))

x = 2.0
print(x)
print(floor(x))

x = 3.7
print(x)
print(floor(x))

print("**************")
x = 1.2
print(x)
print(trunc(x))

x = 1.5
print(x)
print(trunc(x))

x = 2.0
print(x)
print(trunc(x))

print("**************")

x = 1.4
y = 2.6

print(floor(x), floor(y))   # 1, 2
print(floor(-x), floor(-y)) # -2, -3
print(ceil(x), ceil(y))     # 2, 3
print(ceil(-x), ceil(-y))   # -1, -2
print(trunc(x), trunc(y))   # 1, 2
print(trunc(-x), trunc(-y)) # -1, -2