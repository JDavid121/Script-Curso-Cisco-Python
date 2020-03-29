# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 22:42:37 2020

LIST IN A LIST

@author: David
"""
row = []

for i in range(8):
    row.append("WHITE_PAWN")
print(row)

# The same effect may be achieved by means of a list comprehension, 
# the special syntax used by Python in order to fill massive lists.

# A list comprehension is actually a list, but created on-the-fly 
# during program execution, and is not described statically

# list comprehension
arow = ["WHITE PAWN" for i in range(8)] # list comprehension
print(arow)

# list comprehension
squares = [ x**2 for x in range(10)]
print(squares) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

odds = [x for x in squares if ((x % 2) != 0)]
print(odds)

numbers = [i for i in range(10)]
print(numbers)
