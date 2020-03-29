# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 21:17:32 2020

DICTIONARY APPLICATION

Tuples and dictionaries can work together
We've prepared a simple example, showing how tuples and dictionaries 
can work together.

Let's imagine the following problem:

    You need a program to evaluate the students' average scores;
the program should ask for the student's name, followed by 
her/his single score;
    The names may be entered in any order;
    Entering an empty name finishes the inputting of the data;
    A list of all names, together with the evaluated average score, 
should be then emitted.
Look at the code in the editor. This how to do it.

@author: David
"""

schoolClass ={} #empty dictionary
while True:
    name = input("Enter the student´s name (or type exit to quit):")
    if name == "exit":
        break
    score = int(input("Enter the student´s score (0-10):"))
    if name in schoolClass:
        schoolClass[name] = schoolClass[name]+(score,) # creates a tuple with
    else:                                              # the student's scores
        schoolClass[name] = (score,) # create a new tuple array
                                     # for a new student
for name in sorted(schoolClass.keys()):
    csum = 0
    score_counter = 0
    for score in schoolClass[name]:
        csum = csum +score
        score_counter = score_counter + 1
    print (name, ":",csum/score_counter)
    print(schoolClass[name])
print(schoolClass)