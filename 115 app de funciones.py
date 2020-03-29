# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 22:21:16 2020

@author: David
"""
# default parameters
def introduction(firstname = "John",lastname = "Smith"): #default values
    print("Hello my name is",firstname,lastname)

introduction("James","Bond")
introduction("Riga") # default lastname = Smith
introduction(lastname = "Deep") # default firstname = "John"
introduction() # default firstname and lastname

# Exercise 1:
def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")
print("*********************")
intro()

# Exrcise 2:
def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro(b="Sean Connery")

# Exercise 3:
def intro(a, b="Bond"):
    print("My name is", b + ".", a + ".")

intro("Susan")

# Exercise 4:
def sums(a, c, b=2): # to fix the error: def sums(a,c,b=2)
    print(a + b + c)

sums(a=1, c=3)