# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 23:48:58 2020

ASSERTION INSTRUCTION

@author: David
"""

import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)

# you may want to put it into your code where you want to be 
# absolutely safe from evidently wrong data, and where you 
# aren't absolutely sure that the data has been carefully 
# examined before (e.g., inside a function used by someone else)