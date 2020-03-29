# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 11:33:54 2020

Exercise 4

Create a program with a for loop and a continue statement. 
The program should iterate over a string of digits, 
replace each 0 with x, and print the modified string to the screen. 
Use the skeleton below:

@author: David
"""
# Excercise 4 without continue sentence
digit_string = input("Set a digit string\t")
mod_string = ""    
for i in digit_string:
    if (i == "0"):
        mod_string = mod_string + "*"
    else:
        mod_string = mod_string + i
print (mod_string)


# Excercise 4 with continue sentence
digit_string = input("Set a digit string\t")
mod_string = ""    
for i in digit_string:
    if (i == "0"):
        mod_string = mod_string + "*"
        continue
    mod_string = mod_string + i
print (mod_string)
        
