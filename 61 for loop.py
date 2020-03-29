# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 23:02:20 2020

@author: David
"""
print("\nEATING VOWELS PROGRAM")
userword = input("set a word\t")
userword =userword.upper()
print(userword)

for i in userword: #con i apuntamos a cada letra de la palabra almacenada
    if (i=="A"):   #en la variable userword
        print("*",end="")
        continue
    elif (i=="E"):
        print("*",end="")
        continue
    elif (i=="I"):
        print("*",end="")
        continue
    elif (i=="O"):
        print("*",end="")
        continue
    elif (i=="U"):
        print("*",end="")
        continue
    print (i,end="")