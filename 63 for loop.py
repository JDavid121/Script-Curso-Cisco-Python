# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 23:49:04 2020

@author: David
"""

i = 5
while i < 5:
    print(i)
    i += 1
else: # The loop's else branch is always executed once, 
      # regardless of whether the loop has entered its body or not.
    print("else:", i)