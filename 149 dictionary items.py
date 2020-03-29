# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:15:44 2020

DICTIONARY VALUES

@author: David
"""
# values() method:
# values() method can access to the values from a list.
dict6 = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
for value in dict6.values():
    print(value)
# other example:
print("**************************")
dict7 = {1:"beta",2:"gamma",4:"iota",3:"theta",9:"zeta",5:"eta"}
print(dict7.values())
# make a list with the values of dict7:
print("**************************")
alist = list(dict7.values()) #list function: It makes a list.
print(alist)

# make a list with the key and values from dict7 dictionary
blist = list(dict7.items())
print(blist) # The list is a tuple list formed with
             # dictionary keys and values.

# print the 4rth element of blist:
print(blist[3]) #output : (3,"theta")

