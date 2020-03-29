# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 08:50:06 2020

@author: David
"""

from math import sin, pi # import selected entities.

print(sin(pi/2)) # make use of the imported entities.

pi = 3.14   # redefine the meaning of pi and sin
            # they supersede the original (imported) definitions
            # with the code's namespace

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print(sin(pi/2))