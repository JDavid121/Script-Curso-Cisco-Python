# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 20:50:57 2020

@author: David
"""

import math #importing math module

def sin(x):
    if 2 * x == pi:
        return "uno"
    else:
        return None

pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))

# we can use "sin" name (as also "pi" name) in an arbitrary way.
# without confusion
# math.sin -> sin function from math module
# sin() -> function sin() defined previously on line 10.