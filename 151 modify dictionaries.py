# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:18:27 2020

ADDING KEYS AND VALUES TO A LIST USING update() method

@author: David
"""

# form the dict9 dictionary, add the following keys and their
# corresponding values
# swan cygne
# pig truie
# mouse souris
# fly mouche
# snake serpent
# cow vacue
# monkey singe
# dolphin dauphin
# shark requin
# fish poisson
# donkey ane

dict10 = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
dict10.update({"swan":"cygne"})
print(dict10)
print("*************************")
dict10.update({"pig":"truie"})
print(dict10)
# update() method used with for loop
# key list to update into dict10
keylist=["mouse","fly","snake","cow","monkey","dolphin","shark","fish","donkey"]
# value list to update into dict10
valuelist = ["souris","mouche","serpent","vacue","singe","dauphin","requin","poisson","ane"]

# len(keylist) must be equal to len(valuelist)
for i in range(9):
    dict10.update({keylist[i]:valuelist[i]})
print (dict10)