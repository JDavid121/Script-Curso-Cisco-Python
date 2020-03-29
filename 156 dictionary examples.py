# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 00:15:25 2020

DICTIONARY EXAMPLES

@author: David
"""

# 1.0 Creating a dictionary
myDictionary = {
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3",
    }
print(myDictionary)

# 2.0 To access a dictionary item

polEngDict = {
    "kwiat" : "flower",
    "woda"  : "water",
    "gleba" : "soil"
    }

item1 = polEngDict["gleba"]    # ex. 1
print(item1)    # outputs: soil

item2 = polEngDict.get("woda")
print(item2)    # outputs: water

# 3.0 To change the value associated with a specific key
polEngDict = {
    "zamek" : "castle",
    "woda"  : "water",
    "gleba" : "soil"
    }

polEngDict["zamek"] = "lock"
item = polEngDict["zamek"]    # outputs: lock
print(item)

# 4.0 To add or remove a key (and the associated value)
myPhonebook = {}    # an empty dictionary

myPhonebook["Adam"] = 3456783958    # create/add a key-value pair
print(myPhonebook)    # outputs: {'Adam': 3456783958}

del myPhonebook["Adam"]
print(myPhonebook)    # outputs: {}

# to use update() method to add keys and the corresponding values to a dictionary
polEngDict = {"kwiat" : "flower"}

polEngDict.update({"gleba" : "soil"})
print(polEngDict)    # outputs: {'kwiat' : 'flower', 'gleba' : 'soil'}

polEngDict.popitem()
print(polEngDict)    # outputs: {'kwiat' : 'flower'}

# 5.0 You can use the for loop to loop through a dictionary, e.g.:

polEngDict = {
    "zamek" : "castle",
    "woda"  : "water",
    "gleba" : "soil"
    }

for item in polEngDict:
    print(item)    # outputs: zamek
                   #          woda
                   #          gleba
                   
# 6.0 If you want to loop through a dictionary's keys and values, 
# you can use the items() method, e.g.:
polEngDict = {
    "zamek" : "castle",
    "woda"  : "water",
    "gleba" : "soil"
    }

for key, value in polEngDict.items():
    print("Pol/Eng ->", key, ":", value)

# To check if a given key exists in a dictionary, you can use the in keyword:

polEngDict = {
    "zamek" : "castle",
    "woda"  : "water",
    "gleba" : "soil"
    }

if "zamek" in polEngDict:
    print("Yes")
else:
    print("No")

# You can use the del keyword to remove a specific item, 
# or delete a dictionary. To remove all the dictionary's items, 
# you need to use the clear() method:

polEngDict = {
    "zamek" : "castle",
    "woda"  : "water",
    "gleba" : "soil"
    }

print(len(polEngDict))    # outputs: 3
del polEngDict["zamek"]    # remove an item
print(len(polEngDict))    # outputs: 2

polEngDict.clear()   # removes all the items
print(len(polEngDict))    # outputs: 0

del polEngDict    # removes the dictionary

#  To copy a dictionary, use the copy() method:
polEngDict = {
    "zamek" : "castle",
    "woda"  : "water",
    "gleba" : "soil"
    }

copyDict = polEngDict.copy()
print(copyDict)