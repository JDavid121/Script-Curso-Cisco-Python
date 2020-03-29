# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 09:58:15 2020

DICTIONARY ITEMS

@author: David
"""
dict3 = {1:"beta",2:"gamma",4:"iota",3:"theta",9:"zeta",5:"eta"}
# items() method
# This method returns a "class" of tuples.
# Each tuple is a key,value pair

print(dict3.items())
print("**********************")
for key,value in dict3.items():
    print(key,"->",value)
print("**********************")
for key,value in dict3.items():
    print(value,"->",key)
print("***********************")
A = dict3.items()
print(A)
print(len(A))
print(type(A))

