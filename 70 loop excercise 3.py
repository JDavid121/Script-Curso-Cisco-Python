# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 11:22:05 2020

Create a program with a for loop and a break statement.
The program should iterate over characters in an email address, 
exit the loop when it reaches the @ symbol, and print 
the part before @ on one line.

@author: David
"""
# refer to 62 for loop.py for help
# program iterative over characters in a email adress
email_adress = input("Set a email adress\t")
part_to_print = ""
for i in email_adress:
    
    if (i == "@"):
        break
    
    part_to_print = part_to_print+i

print(part_to_print)
