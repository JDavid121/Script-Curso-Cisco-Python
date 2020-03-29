# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 10:50:30 2020

@author: David
"""

# else function

for i in range (10):
    print (i,end = " ")
else:
    print ("else end count") #else statement has been executed

# *********************

print ("****************")
for i in range (20):
    print (i,end = " ")
    if (i > 15):
        print ("break loop")
        break
else:
    print ("else end count") #else statement had not been executed.