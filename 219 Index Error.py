# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 23:57:44 2020

Index Error

@author: David
"""
# the code shows an extravagant way
# of leaving the loop

alist = [1, 2, 3, 4, 5]
ix = 0
doit = True

while doit:
    try:
        print(alist[ix])
        ix = ix + 1
    except IndexError:
        doit = False
print('Done')

