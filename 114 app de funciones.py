# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 21:52:19 2020

FUNCTION APPLICATION

@author: David
"""
def cumulative(a,b,c):
    print(a,"+",b,"+",c,"=",a+b+c) #sum of a,b,c

cumulative(1,2,3) #positional argument passing
cumulative(a = 1, b = 2, c = 3) #keyword arguments
cumulative(3, b = 4, c = 5) #mixed positional and keyword arguments.
cumulative(3,c = 5,b = 4) #mixed positional and keyword arguments.
cumulative(3,5,c = 4) # Do this makes any sense?

