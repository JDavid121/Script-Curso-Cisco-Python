# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 22:35:16 2020

Scenario
The continue statement is used to skip the current block
and move ahead to the next iteration, without executing 
the statements inside the loop.

It can be used with both the while and for loops.

Your task here is very special: you must design a vowel eater! 
Write a program that uses:

a for loop;
the concept of conditional execution (if-elif-else)
the continue statement.
Your program must:

1.0 ask the user to enter a word;
2.0 use userWord = userWord.upper() to convert the word entered 
    by the user to upper case; we'll talk about the so-called 
    string methods and the upper() method very soon - don't worry;
3.0 use conditional execution and the continue statement to "eat" 
    the following vowels A, E, I, O, U from the inputted word;
4.0 print the uneaten letters to the screen, each one of them on a separate line.

@author: David
"""
#Laboratory
userword = input("set a word\t")
userword =userword.upper()
#print(userword)
A=list(userword)
#print(A)
#print(A)
for i in range(0,len(A)):
    if (A[i]=="A"):
        print("*")
        continue
    elif (A[i]=="E"):
        print("*")
        continue
    elif (A[i]=="I"):
        print("*")
        continue
    elif (A[i]=="O"):
        print("*")
        continue
    elif (A[i]=="U"):
        print("*")
        continue
    print (A[i],"\n")

