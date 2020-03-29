# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 00:12:15 2020

Import Error

@author: David
"""

# one of this imports will fail - which one?

try:
    import math
    import time
    import abracadabra

except:
    print('One of your imports has failed.')

# a concrete exception raised when an import operation fails
# It has not a particular name as ArithmeticError.