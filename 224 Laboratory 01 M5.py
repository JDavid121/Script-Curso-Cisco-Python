# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 00:22:18 2020

LABORATORY

Scenario

Your task is to write a function able to input integer 
values and to check if they are within a specified range.

The function should:

accept three arguments: a prompt, a low acceptable limit, 
and a high acceptable limit;

if the user enters a string that is not an integer value, 
the function should emit the message Error: wrong input, 
and ask the user to input the value again;

if the user enters a number which falls outside the 
specified range, the function should emit the message Error: 
the value is not within permitted range (min..max) and ask 
the user to input the value again;

if the input value is valid, return it as a result.

@author: David
"""
# FUNCTION

def readint(minv,maxv):
    try:
        print("\nEnter a valid number between",minv,"and",maxv)
        promt = int(input("Enter the number\t"))
        assert (promt >= minv) and (promt <= maxv)
        return print("\nNumber entered is",promt)
    except ValueError: 
        print("\nWARNING, enter a valid number, not a string")
        readint(minv,maxv)
    except AssertionError:
        if promt < minv:    
            print("\nWARNING, number must be greater than",minv)
        if promt > maxv:    
            print("\nWARNING, number must be less than",maxv)
        readint(minv,maxv)
    except:
        print("Sorry we have an unexpected error")
        readint(minv,maxv)
        
# principal program
        
readint(-3,3)
    
