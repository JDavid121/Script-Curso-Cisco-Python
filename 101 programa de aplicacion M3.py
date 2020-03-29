# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:08:44 2020

@author: David
"""

# Prorgama de aplicación de sentencia if:
#Application of if sentence:

# first example
# ****************************************
print("Program to set a dinner")
a = input("Do you like coffe? Y/N\t")
if (a == "Y"): #Client likes coffe
    print("We have american coffe or milk with coffe")
print("You´re welcome") # this sentences is always done, no matter the if
                        # conditional
# second example
# The if else statement:
print("Second example if-else")
a = input ("Do you like a coffe? Y/N\t")
if (a == "Y"):
    print("We have a delicious coffe")
else:
    print("We have a delicious juice, instead of coffe")
print("You´re welcome")

# Third example:
# nested if statements:
print("third example nested if")
a = input("Do you like coffee? Y/N\t")
if (a=="Y"):
    b = input("Do you like american coffee(A) or milk with coffee(B)")
    if (b == "A"): #American coffe
        print("One american coffe with sugar")
    if (b == "B"): #Milk with coffee
        print("One milk with cofee without sugar")
else: #If the client doesn´t like cofee:
    c = input("Do you like apple juice(A) or pineapple juice(B)")
    if (c == "A"): #apple juice
        print("One apple juice to the table")
    if (c=="B"): #pineapple juice
        print("One pinapple juice with two teaspons")
print("You´re welcome")

# fourth example:
# else if statement:
# Use else if if you nedd to do a lot of comparision
a = 0
b = "N"
while(True):
    if (b == "Y"):
        break #We scape for while loop
    a = int(input("Enter the air temperature"))
    if (a < 5):
        print("it´s cold here!")
        print("Termometer: *00000")
    elif (a<10): # statement completed if 5 < a < 10
        print("Until cold, but getting hot slowly")
        print("Termometer: **0000")
    elif (a<15): #statement executed if 10 < a < 15
        print("A little cold, mostly hot")
        print("Termometer: ***000")
    elif (a<20): #staements executed if 15 < a < 20
        print("Ideal temperature")
        print("Termometer: ****00")
    elif (a<25): #statement executed if 20 < a < 25
        print("until ideal temperature, no more hot")
        print("Termometer: *****00")
    elif (a<30): #statement excuted if 25 < a < 30
        print("It is getting hot slowly")
        print("Termometer: ******0")
    elif (a<35): #statement executed if 30 < a < 35
        print("It is hot here, reduce temperatue")
        print("Termometer: *******")
    else: #statement executed if a > 35
          #this statement is executed if any "if" or "elif" statement was executed before.
        print("Set a temperature less than 35°C")
    b = input("Do you want to quit? Y/N\t") #this statement is always executed. 
                                            # It isn't into if cascade.
print("You´re welcome")    
    
                        