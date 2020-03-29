# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 23:58:06 2020

@author: David
"""

for i in range(5):
    print(i)
else:
    print("else:", i) #The i variable retains its last value.
    
i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i) # When the loop's body isn't executed, 
                      # the control variable retains the value it had before the loop.
    
 # Note: if the control variable doesn't exist before the loop starts,
 # it won't exist when the execution reaches the else branch.