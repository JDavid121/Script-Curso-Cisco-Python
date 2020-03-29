# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 10:40:29 2020

@author: David
"""

from math import e, exp, log

print(exp(log(e)))
print(pow(e, 1))
print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))