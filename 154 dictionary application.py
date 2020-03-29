# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:14:48 2020

DICTIONARY APPLICATION

Create a program to create a dictionary that includes student's name and
sets this scores. Then with all scores are entered, the program will 
allow enter a other student's name and their scores.
when all student has been entered, the program will calculate the
average score for each student

@author: David
"""
# create a new dictionary

mathscores = {} #dictionary to save student's names and their scores

while True:
    # enter student's name
    name = input("Enter a student's name:(press q to quit)\t")
    if name == "q": 
        break
    # enter student's scores
    while True:
        score = input("Enter {} score between 0 and 10 (enter yes to quit)\t".format(name))
        if score != "yes":    
            score = int(score) # this is a student's score
        if score == "yes":     # this is an instruction to leave setting scores.
            break

        if name in mathscores:
            mathscores[name] = mathscores[name]+(score,) # second, add scores to the key´s value name.
        else:
            mathscores[name] = (score,) # first create a dictionary tuple.
# average program
for name in (sorted(mathscores.keys())): #.keys() method which can use to evaluate each dictionary keys.
                                         # sorted() function to sort elements in a list or dictionary
    csum = 0
    counter = 0
    for score in mathscores[name]: # evaluate each score in a name´s tuple 
        csum = csum + score
        counter = counter + 1
    print("{} average:".format(name),csum/counter) # average = csum/counter
    print("{} notes:".format(name),mathscores[name])
