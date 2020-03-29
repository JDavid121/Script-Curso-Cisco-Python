# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:26:34 2020
WHILE LOOP

@author: David
"""
import numpy as np
# Do an example of while loop
c = 1
a = 0
while (c): # with c = 1 while is true
    a = a + 1
    print(a,end=" ")
    if a > 100:
        c = 0 # with c = 0 while is false
print("\n\n")
i = 0
while (i < 100):
    print("*"*i)
    i = i + 1
while (i > 0):
    print("*"*i)
    i = i - 1

# Do an example with for loop
# Make a table of the following function x = t^2
# from -5 < t < 5 with increments of 0.2

for t in range(-25,26,1): #increment is scalable in 5
    x = ((t/5)**2)
    print(t/5," ",x)

#Write a program of the five primary powers of two 2^0, 2^1, etc:
for i in range(5):
    x = 2**i
    print(i, " ",x)

# Make use of break and continue statements.
# To print an even number list
print("***************")
x = 0
while x<20:
    x = x + 1 #counter up from contnue statement, if not, they not will be reached.
    if (x % 2 == 0): #even numbers    
        print(x)
        continue
# To print an odd number list
print("***************")
x = 0
while x<20:
    x = x + 1 #counter up from contnue statement, if not, they not will be reached.
    if (x % 2 != 0): #odd numbers    
        print(x)
        continue
# else sentence in while loop
print("*****************")
x = 0 # Counter
while x < 100:
    print(x, end = " ")
    x = x +1
    if ( x > 50):
        break #with break sentence, else sentence is not excetuted.
else:
    print("")
    print("We've reached the end of while loop")

print("*********************")
for i in range(100):
    print(i, end = " ")
    if ( i > 50):
        break #with break sentence, else sentence is not excetuted.
else:
    print("")
    print("We've reached the end of while loop")
# continue statement and break:
        
print("*****************")
x = 0 # Counter
while x < 100:
    print(x, end = " ")
    x = x +1
    if ( x > 50):
        continue #with continue sentence, else sentence is excetuted.
else:
    print("")
    print("We've reached the end of while loop")

print("*********************")
for i in range(100):
    print(i, end = " ")
    if ( i > 50):
        continue #with continue sentence, else sentence is excetuted.
else:
    print("")
    print("We've reached the end of while loop")
        