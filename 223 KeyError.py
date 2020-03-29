# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 00:15:39 2020

Key Error

@author: David
"""

# how to abuse the dictionary
# and how to deal with it

dict = { 'a' : 'b', 'b' : 'c', 'c' : 'd' }
ch = 'a'
try:
    while True:
        ch = dict[ch]
        print(ch)
except KeyError:
    print('No such key:', ch)

# KeyError
# a concrete exception raised when you try to access a 
# collection's non-existent element (e.g., a dictionary's element)
