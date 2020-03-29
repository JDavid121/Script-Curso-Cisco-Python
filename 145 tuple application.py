# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:42:13 2020

TUPLE APPLICATION

@author: David
"""

var = 123
t1 = (1,)
t2 = (2,)
t3 = (3,var)
t1,t2,t3 = t2,t3,t1
print(t1,t2,t3)
print(type(t1))