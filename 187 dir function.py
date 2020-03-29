# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 09:31:31 2020

@author: David
"""

import math
print(dir(math))    # dir() It is able to reveal all the names provided throught
                    # a particular module.
for name in dir(math):
    print(name)
print("***************")
import pandas
for name in dir(pandas):
    print(name)