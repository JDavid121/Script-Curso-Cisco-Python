# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 00:41:07 2020

@author: David
"""

# What happens when you attempt to run the following snippet?
myTup = (1, 2, 3)
print(myTup[2]) # output 3

# What is the output of the following snippet?
tup = 1, 2, 3
a, b, c = tup
print(a * b * c) #output: 6

# Complete the code to correctly use the count() method to find 
# the number of duplicates of 2 in the following tuple.

tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

# count(n) A method that counts how many times is present the value n into
# a list or tuple.

print(duplicates)    # outputs: 4

# Write a program that will "glue" the two dictionaries (d1 and d2) together and create a new one (d3).

d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)
    # update() method to add a key and values to a dictionar
print(d3)

# Write a program that will convert the l list to a tuple.

l = ["car", "Ford", "flower", "Tulip"]

t = tuple(l)
print(t)

# Write a program that will convert the colors tuple to a dictionary.

colors = (("green", "#008000"), ("blue", "#0000FF"))

colDict = {} #empty Dict
colDict.update(colors)
print(colDict)

# other way
print("********************************")
colors = (("green", "#008000"), ("blue", "#0000FF"))
colDict = {} #empty Dict
colDict = dict(colors)
print(colDict)

# What will happen when you run the following code?
myDict = {"A":1, "B":2}
copyMyDict = myDict.copy()
myDict.clear()

print(copyMyDict) #output {"A":1, "B":2}

# What is the output of the following program?

colors = {
    "white" : (255, 255, 255),
    "grey"  : (128, 128, 128),
    "red"   : (255, 0, 0),
    "green" : (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb)
    # output:
    # white : (255,255,255)
    # grey : (128,128,128)
    # red : (255,0,0)
    # green : (0,128,0)
