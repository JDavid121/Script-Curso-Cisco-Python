# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 23:45:42 2020

LABORATORY

Estimated time: 10-15 minutes

Level of difficulty: Easy

Objectives
improving the student's skills in defining, using and testing functions.

Scenario
A car's fuel consumption may be expressed in many different ways. 
For example, in Europe, it is shown as the amount of fuel consumed 
per 100 kilometers.

In the USA, it is shown as the number of miles traveled by a car using one 
gallon of fuel.

Your task is to write a pair of functions converting l/100km into mpg, 
and vice versa.

The functions:

are named l100kmtompg and mpgtol100km respectively;
take one argument (the value corresponding to their names)
Complete the code in the editor.

Run your code and check whether your output is the same as ours.

Here is some information to help you:

1 American mile = 1609.344 metres;
1 American gallon = 3.785411784 litres.

@author: David
"""

def l100kmtompg(liters):
    a = (100*3.785411784/(liters*1.609344))
    return a
def mpgtol100km (mpg):
    a = (100*3.785411784/(mpg*1.609344))
    return a

# Tips:
# 3.9 liters are using to travel 100 km
# (A): mpg = (100*3.785411784/(liters*1.609344))  
#    3.9 liters per 100 km are equivalent to 60.31143162393162 mpg

# To find the liters per 100 km, from (A) equation find liters
#   liters = (100*3.785411784/(mpg*1.609344))
    
print(l100kmtompg(3.9)) # output: 60.31143162393162 
print(l100kmtompg(7.5)) # output: 31.36194444444444
print(l100kmtompg(10.)) # outout: 23.52145833333333
print(mpgtol100km(60.3)) # output: 3.9007393587617467 
print(mpgtol100km(31.4)) # output: 7.490910297239915 
print(mpgtol100km(23.5)) # output: 10.009131205673757