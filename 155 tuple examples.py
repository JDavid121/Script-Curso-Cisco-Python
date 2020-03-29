# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 23:43:29 2020

@author: David
"""
# Tuple examples
myTuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
print(myTuple)

myList = [1, 2, True, "a string", (3, 4), [5, 6], None]
print(myList)

# empty tuple
emptyTuple = ()
print(type(emptyTuple))    # outputs: <class 'tuple'>

# one element tuple
oneElemTup1 = ("one", )    # brackets and a comma
oneElemTup2 = "one",     # no brackets, just a comma

# access tuple elements indexing.
myTuple = (1, 2.0, "string", [3, 4], (5, ), True)
print(myTuple[3])    # outputs: [3, 4]

# delete tuples as a whole
myTuple = 1, 2, 3, 
del myTuple
#print(myTuple)    # NameError: name 'myTuple' is not defined

# Example 1 acess to each element in a tuple
t1 = (1, 2, 3)
for elem in t1:
    print(elem)

# Example 2 verify if an element is in (not in) a tuple
t2 = (1, 2, 3, 4)
print(5 in t2)
print(5 not in t2)

# Example 3 len() function onto a tuple
t3 = (1, 2, 3, 5)
print(len(t3))

# Example 4 join (+) tuples, multiply (*) tuples
t4 = t1 + t2
t5 = t3 * 2

print(t4)
print(t5)