# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:42:13 2020

DICTIONARY

@author: David
"""

dict1 = {"cat":"chat","dog":"chien","horse":"cheval"}
phonenumbers = {"Horacio" : 1123456, "Susana" : 2334125, "Florinda" : 3456123}
emptyDictionary = {}

print(dict1)
print(phonenumbers)
print(emptyDictionary)
# How to get any value form a list.
print(dict1["cat"])
print(dict1["dog"])
print(phonenumbers["Horacio"])
#print(dict1["pork"]) # KeyError "pork" does not inside on the list dict1

# Create a program that search matches between words and dict1
words = ["cat","lion","horse"]
dict1 = {"cat":"chat","dog":"chien","horse":"cheval"}

# Word searching
for word in words:
    if word in dict1:
        print(word,"->>",dict1[word])
    else:
        print(word,"does not belong to dict1")
