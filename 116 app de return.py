# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 05:05:14 2020

@author: David
"""

# return sentence
def happyNewYear(wishes = True): # Happy new year function
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    print("Happy New Year!")

happyNewYear()      # Providing True as an argument:
                    # function prints the wishes.
print("*************")
happyNewYear(False) # Providing False as an argument:

                    # will modify the function's behavior - 
                    # the return instruction will cause its termination 
                    # just before the wishes