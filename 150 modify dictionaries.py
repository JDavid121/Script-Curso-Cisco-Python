# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:33:33 2020

MODIFYING DICTIONARIES

@author: David
"""

# From dict7 dictionary, replace "chat" with "miauuu"

dict7 = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
print(dict7)
dict7["cat"] = "miauuu"
print(dict7)

# If the list is so long, you must search the key corresponding to "chat"
print("***************************")
dict8 = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
for key,value in dict8.items():
    if value == "chat": 
        print (key) # prints the key corresponding to "chat" value

