# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 21:19:45 2020

Try to make a program that involves all of you had learned in modules
2,3

@author: David
"""
# Module 2 Print functions
import numpy as np

print("Program that generate a random number")
a = np.random.randn(1)
print("Random number is ...\t",a[0])
# Use scape instruction \
print("Program to use the scape and newline characters")
for i in range(5):
    print("\t*\n")
# Use the keyword instruction.
print("Program to use the keyword end & sep ")
for i in range(5):
    print("*",end=" ")
    print("")
print ("Angela","Rosa","Laura",sep="&")
# Use literal
# Print a string literal named Alondra
print("Alondra")
# Print a integer literal equals to 101
print(101)
#print the following integer literal: 11_111_111
a = 11_111_111
print(a)
# Octal numbers
a = 0O123 #octal number equivalent to decimal number: 83
print(a)
# Check the following sum
a = 0o76 
b = 0o56
c = a + b # c = 108 (decimal)
print(c) 
#Hexadecimal number
a = 0x76
b = 0x56
c = a + b #hexadecimal
print(c)

# scientific notation
print("Scientific Notation")
a = 3.1e9
print(a)
#Print the constant Plank
h = 6.62607e-34 # Use a negative exponent without parentheses
print(h)
#Create a program that calculates the distance travelled by the light
# in a specific time
print("**************************")
print("Travel distance of light vs time")
a=0
#a = float(input("Set the time in seconds...\t"))
C = 2.99792458e8 # Speed of light in meters per seconds
dist = a*C # distance in meters
dist = "{:.2f}".format(dist)
print("The travel distance of light in {} seconds is {} millions of meters".format(a,dist))
# M2 Arithmetic operators:
# exponentiation
print(2 ** 3)
#Multiplication
print(2 * 3)
# Division (float)
print(2/3)
# Integer division (floor division)
print (2//3) # rounded to the nearest integer value that is less than the real 
             # (not rounded) result.
print(-6/4)
print(-6//4) #rounded to the lesser integer value. (-1.5 rounded to -2)

#Modulo remainder of the division
print(5%2) # 5//2 = 2 then: 2x2 = 4 then 5 - 4 = 1
           # 5 % 2 = 1
           # 5 % 2 the rest (reminder or modulo) of the division (5//2)
print(12 % 4.5) #(12 % 4.5) = 3.0
# addition:
print( 3 + 4)
# substracction:
print (3 - 4)

# Operators and their priorities:
# left side binding: The calculation of the expression is performed from left 
# to right.
print(9%6%2)
print(9%6) # = 3
print(3%2) # (3%2) = 1
# (9%6%2) = 1

# exponentiation has a right side binding
print(2**3**1) #(3**1) = 3 then 2**(3) = 8
# guess the following snippet code:
print(2*3%5) #(2*3)=6 then (6%5)=1 R=1

# parentheses: Operation in parentheses are allways calculated first.
# Guess the following snippet code:
print((5*((25%13)+100)/(2*13))//2)
# (25 % 13) = 12
# (25 % 13) + 100 = 112
#((25 % 13) + 100)/(2*13) = 112/26 = 4.308
#5 * ((25 % 13) + 100)/(2*13) = 21.538
# 5*((25 % 13) + 100)/(2*13)//2 = 10
# R = 10.0

# What is the output of the following snippet?
print(2**4,(2*4.),(2*4)) # R: 16 8.0 8

# What is the output of the following snippet?
print((-2/4),(2/4),(2//4),(-2//4)) # R: -0.5 0.5 0 -1

#  ************************ round function
a = 2/3
a = round(a,2) # Round function that sets a number with a specific decimal digits.
               # var a is set using two decimal digits rounded.
print(a) # R = 0.67

#write a program to calculate the area of a rectangle
print("Program to calculate the area of a rectangle")
a = 0.0
b = 0.0
# a = float(input("Set the first side a in meters...\t"))
# b = float(input("Set the second side b in meters...\t"))
c = a*b
print("The total area of the rectangle is...{}".format(c))

# Concatenation

# Example of concatenation:
a = ""
for i in range(20):
    a = a + str(i) + " " # perform a concatenated string with the values of i
                         # values of i must be transformed into string before
                         # concatenate them.
print(a)

# ********************** MODULE 3 ***************************

# Comparison operators

var1 = 23
var2 = 23.0
print(var1 == var2) # equal operator.
var1 = 23
var2 = 1
print(var1 == var2) # equal operator.
var3 = 12
var4 = 6.0
print(var3 != var4) # not equal operator.
var3 = 12
var4 = 12.0
print(var3 != var4) # not equal operator.

# greater than operator
a = 0 # Ascending counter
while (a < 100): #prints the integer numbres from 0 to 99
    print(a,end=" ")
    a = a + 1
# Descending counter.
a = 100
while (a > 0):
    print(a,end=":-)")
    a = a - 1 #prints the integer numbres from 100 to 1
# Greater than, or equal to
#print a Fibonacci series 0, 1, 1, 2, 3, 5, 8, 13, 21
firstn = 0
secondn = 1
x = 0
while (x < 10):
    if (x == 0):
        print(x)
        x = 1
        continue
    if (x == 1):
        print(x)
        x = 2
        continue
    x = x + 1 # counter.        
    nextn = firstn +secondn
    firstn = secondn
    secondn = nextn
    print(nextn)

# Conditions and conditional execution.

# Conditional
#a = int(input("Enter a number from 0 to 1000\t"))
a = 250
if (a > 500):
    print("Number {} is greater than 500".format(a))
if (a>100):
    print("Number {} is greater than 100".format(a))
print("End of program")

a = 0 #Counter
while (a < 100):
    if (a > 20):
        print("Note {} is greater than...20".format(a))
    if (a > 50):
        print("You see {} is greater than ...50".format(a))
    if (a > 75):
        print("by the way {} is greater than ...75".format(a))
    a = a + 1
print("End of program")  

# If-else statement  
print("What do you like chesse or jamon?")
a = input("for chesse press C,")
if ( a == "C"):
    print ("You had choice chesse")
else:
    print("You had choice jamon")
print("end of program")

# Elif statement
print ("\nWelcome to dinner\n")
a = input ("Do you like coffe,juice,soda A,B,C\t")
if (a == "A"):
    print("We have 2 types of coffe for you")
elif (a == "B"):
    print("We have orange juice")
elif (a == "C"):
    print("Soda is not good for dinner")
b = input("Do you like eggs(Y), jamon(J), tocino (T)? Y/N\t")
if (b == "Y"):    
    print ("We have only french eggs for you")
elif (b == "N"):
    print("We have two jamons for you")
elif (b == "T"):
    print("We have a delicious tocinet for you")
c = input ("Do you like bread(B), cereal(C), rice (R)? Y/N\t")
if (c == "B"):
    print ("We have german bread and croussant")
elif (c == "C"):
    print("We have bolas de verde for you")
elif (c == "R"):
    print("We can offer black rice for you")
print("Bonn Apetite")
print("**************  order ****************")

# 

