# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 12:08:06 2020

@author: David
"""

# exercise 1
# What is the output of the following snippet?

def message():
    alt = 1
    print("Hello, World!")

#print(alt) #error, alt var must be defined
           # alt var scope has n't be defined properly.

# exercise 2
# What is the output of the following snippet?

a = 1 # a var scope in line 21
def fun():
    a = 2 # a var scope inside fun() fuction
    print(a)

fun() #invoke the function, it takes a = 2 (function scope and print (a))
print(a) #prints a = 1, a var scope starts in line 21
# ***********************************************************************

# exercise 3
# What is the output of the following snippet?
a = 1 # a var scope strarts in line 30
def fun():
    global a #makes a var as a global scope var
    a = 2 # writes a = 2 (a is a global scope var)
    print(a)

fun() #invoke fun function, print 2
a = 3 # rewrites a = 3
print(a) #prints actual value of a 3

# exercise 4
# ***********************************************************************
a = 1 # var scope starts in line 44 
def fun():
    global a #makes a a global scope var
    a = 2 #rewrite a value
    print(a) #print a var value

a = 3 #change a var from 2 to 3
fun() # invoke fun function, a = 2, print (a)
print(a) #print current value of a (a = 2)