# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:09:47 2020

TUPLE APPLICATION

@author: David
"""

tupple1 = (1,10,100,1000)
print(tupple1[0])   # output: 1
print(tupple1[-1])  #  output: 1000
print(tupple1[1:])  # output: (10,100,1000)
print(tupple1[:-2]) # output: (1,10)

for element in tupple1:
    print(element)

# This operations are not allowed with tuples:
# tupple1.append(2)
# del tupple1[0]
# tupple1[0] = 2

print(tupple1)

