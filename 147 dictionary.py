# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 09:21:21 2020

DICTIONARY

@author: David
"""

# keys() method is a way to acces at the keys and values from a list.
print("*****************************")
print("keys() method")

dict1 = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"} 

for key in dict1.keys(): # to access a whole dictionary
    print(key, "->", dict1[key]) # key It is the dictionary keys
                                 # dict1[key] It is the corresponding key value
                                 # from dict1 dictionary.

# How to sort a dictionary
# We can use sorted() function
# sorted() function works with keys() method.

dict2 = {"delta":5,"alpha":1,"eco":4,"bravo":2,"charlie":3} #list is n't sorted
print("************************")
print("sorted() function")
for key in sorted(dict2.keys()):
    print(key,"->",dict2[key]) # print sorted keys and their values.

# more examples:
# 1.0 From the dict3 dictionary:
    
print("************************")
dict3 = {1:"beta",2:"gamma",4:"iota",3:"theta",9:"zeta",5:"eta"} #dictionary codes
# 1.0.1 print the dictionary codes in an ascending way
for key in sorted(dict3.keys()):
    print(key,"->",dict3[key])
print("************************")
# 1.0.2 print the dict3 dictionary in a desending way:
for key in sorted(dict3.keys(),reverse = True):
    print(key,"->",dict3[key])
# 2.0 From the dict4 dictionary:
dict4 = {"Ana":123,"Laura":321,"Belen":421,"Carla":367,"Ibeth":957}
# 2.0.1 Print their keys and their corresponding values in an ascending form
for key in sorted(dict4.keys()):
    print(key,"->",dict4[key])
# 2.0.1 Print their keys and their corresponding values in a desending form
print("***********************")
for key in sorted(dict4.keys(),reverse = True):
    print(key,"->",dict4[key])
    
