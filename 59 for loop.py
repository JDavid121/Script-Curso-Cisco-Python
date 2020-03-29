# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:26:54 2020

Scenario
The break statement is used to exit/terminate a loop.
Design a program that uses a while loop and continuously
asks the user to enter a word unless the user enters
"chupacabra" as the secret exit word, in which case the message 
"You've successfully left the loop." should be printed to the screen, 
and the loop should terminate.

Don't print any of the words entered by the user. 
Use the concept of conditional execution and the break statement.

@author: David
"""
# LABORATORY:
while (True):
    user_word = input("enter the password to leave ...\n")
    if (user_word == "chupacabra"):
        break
    print("try again please...")
print("you've successfully left the loop")
