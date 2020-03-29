# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 08:55:07 2020

@author: David
"""

pi = 3.14	# line 08

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None	# line 14

# from line 08 to line 14 we define our own pi and sin names
# in the namespace code.

print(sin(pi/2))	# line 19


from math import sin, pi	# line 22

print(sin(pi/2))	# line 24

# from line 22 to line 24 we redefine pi and sin names in the
# module namespace
