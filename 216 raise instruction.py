# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:36:39 2020

raise instruction

@author: David
"""

# raise: This instruction will immediately re-raise 
# the same exception as currently handled.

# Thanks to this, you can distribute the exception 
# handling among different parts of the code.

# There is one serious restriction: this kind of raise 
# instruction may be used inside the except branch only; 
# using it in any other context causes an error.

def badFun(n):
    try:
        return n / 0
    except: # launch the function exception
        print("I did it again!")
        raise # launch the principal program PP exception

# principal program
try:
    badFun(0) # call badFun function
except ArithmeticError: # principal program PP exception
    print("I see!")

print("THE END.")
