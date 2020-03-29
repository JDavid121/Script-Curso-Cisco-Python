# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:35:37 2020

@author: David
"""
dict10 = {'cat': 'chat', 'dog': 'chien', 'horse': 'cheval', 'swan': 'cygne', 'pig': 'truie', 'mouse': 'souris', 'fly': 'mouche', 'snake': 'serpent', 'cow': 'vacue', 'monkey': 'singe', 'dolphin': 'dauphin', 'shark': 'requin', 'fish': 'poisson', 'donkey': 'ane'}
print(dict10)

#remove "shark" key from dict10:
del dict10["shark"]
print (dict10)

# remove the corresponding key of "singe" value from dict10 dictionary.
print(dict10)
print("*****************************")
for key,value in dict10.items():
    if value == "singe":
        print (key, "->",value)
        keydeleted = key
print("*****************************")
del dict10[keydeleted]
print(dict10)

# popitem() method
# The popitem() metod deletes the last key of a dictionary
# delete the last one of the keys stored in the dict10 dictionary
print("*****************************")
dict10.popitem()
print(dict10)