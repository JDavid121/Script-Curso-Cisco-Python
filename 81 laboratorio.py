# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 10:49:10 2020

LABORATORY

Level of difficulty: Easy

Objectives: Familiarize the student with:
creating and modifying simple lists;
using methods to modify lists.

Scenario

The Beatles were one of the most popular music group of the 1960s, 
and the best-selling band in history. Some people consider them to be 
the most influential act of the rock era. Indeed, they were included 
in Time magazine's compilation of the 20th Century's 100 most 
influential people.

The band underwent many line-up changes, culminating in 1962 with 
the line-up of John Lennon, Paul McCartney, George Harrison, and 
Richard Starkey (better known as Ringo Starr).

Write a program that reflects these changes and lets you practice 
with the concept of lists. Your task is to:

step 1: create an empty list named beatles;
step 2: use the append() method to add the following members 
of the band to the list: John Lennon, Paul McCartney, and George Harrison;
step 3: use the for loop and the append() method to prompt 
the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
step 5: use the insert() method to add Ringo Starr to the beginning of the list.
By the way, are you a Beatles fan?

@author: David
"""

#lABORATORY
# step 1
beatles = [] # Empty list

# Step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("****************************")
print ("Beatles List\n")
print(beatles)
print("\n")

# Step 3
for i in range (1):
    
    print ("Do you like to add the following names to the Beatles list?")
    a = input("Stu Sutcliffe\tY/N\t")
    if a == "Y":
        beatles.append("Stu Sutcliffe")
        print(beatles)
    a = input("Pete Best\tY/N\t")
    if a == "Y":
        beatles.append("Pete Best")
        #print(beatles)
print(beatles)

# Step 4

a = input("Do you like to remove 'Stu Sutcliffe' from the list? Y/N\t")
if a == "Y":
    a = 3
    del(beatles[3])
    print(beatles)
else:
    a = 4
b = input("Do you like to remove 'Pete Best' from the list? Y/N\t")
if b == "Y":
    del(beatles[a])
    print(beatles)

# Step 5

a = input("Do you like to add Ringo Star to the list? Y/N\t")
if a == "Y":
    beatles.insert(0,"Ringo Star")
print(beatles)

