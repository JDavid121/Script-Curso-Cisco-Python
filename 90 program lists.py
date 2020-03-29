# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:50:17 2020

Now let's find the location of a given element inside a list:

@author: David
"""
# Enter a list
print("Program List")
a = int(input("Enter the number of elements in the list\t"))
mlists =[]
for i in range(1,a+1,1):
    b = int(input("Enter the {} value\t".format(i)))
    mlists.append(b)
pass
print("\nNumbers that has been set...")
print(mlists)

#Evaluate if a element is on the list

a = int(input("Enter an element...\t"))
if (a in mlists):
    print("Yes, the ",a,"element is on the list")
    # If the element is on the list:
    for i in range(len(mlists)): #Evaluate all the list
        if a == mlists[i]:    
            print ("The ",a,"element is on the",i,"location")

else:
    print("Sorry, the ",a,"element isn't in the list")


# **********************************************
    # A short program
    # Only you need more practique, that´s all.
    
myList = mlists[:]# Copy the list
toFind = a #Copy the element to find
found = False # A flag that indicates a match.

for i in range(len(myList)):
    found = (myList[i] == toFind) # If we have a match
    if found:
        break # We leave the for loop if we had a match

if found:
    print("Element found at index", i)
else:
    print("absent")
