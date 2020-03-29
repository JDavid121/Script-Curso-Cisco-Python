# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 23:17:18 2020

Scenario
Your task here is even more special than before: 
you must redesign the (ugly) vowel eater from the previous
lab (3.1.2.10) and create a better, upgraded (pretty) vowel eater! 
Write a program that uses:

a for loop;
the concept of conditional execution (if-elif-else)
the continue statement.
Your program must:

1.0 Ask the user to enter a word;
2.0 Use userWord = userWord.upper() to convert the word 
    entered by the user to upper case; we'll talk about 
    the so-called string methods and the upper() method 
    very soon - don't worry;
3.0 Use conditional execution and the continue statement
    to "eat" the following vowels A, E, I, O, U from the
    inputted word;
4.0 Assign the uneaten letters to the wordWithoutVovels
    variable and print the variable to the screen.

Look at the code in the editor. We've created wordWithoutVovels 
and assigned an empty string to it. Use concatenation operation 
to ask Python to combine selected letters into a longer string 
during subsequent loop turns, and assign it to the wordWithoutVovels variable.

Test your program with the data we've provided for you.

@author: David
"""
print("EATEN VOWELS PROGRAM")

userword = input ("Enter a word\t")
userword = userword.upper()
wordWithoutVovels = ""
for i in userword:
    if (i == "A"):
        continue
    elif (i=="E"):
        continue
    elif (i=="I"):
        continue
    elif (i=="O"):
        continue
    elif (i=="U"):
        continue
    wordWithoutVovels = wordWithoutVovels + i
print(wordWithoutVovels)

    
