# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:00:41 2020
Use a program to find the greatest value in a list.
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
# To evaluate the elements in mlists
# Sort the elements in the list
swapped = True
while (swapped):
    swapped = False
    for i in range (len(mlists)-1):
        if mlists[i]>mlists[i+1]: #Do the swap
            swapped = True 
            mlists[i],mlists[i+1] = mlists[i+1],mlists[i]
print ("\nElements sorted...")
print (mlists)
# Print the greatest element in the list
print("\nThe greatest value is...")
print(mlists[len(mlists)-1])

#**************************************

# copy list
myList = mlists[:] #Total slice to copy the list
#myList = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = myList[0] # We assume the first value is the greatest one of the 
                    # list
for i in range(1, len(myList)):
    if myList[i] > largest: # a) evaluate if this is true.
        largest = myList[i] #do the change if a) is true

print(largest)

#*************************************

# A short program to find the greatest value in a list

myList = mlists[:] #Total slice to copy the list
#myList = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = myList[0]

for i in myList[1:]: #Evaluate the entire list with slices
    if i > largest:
        largest = i

print(largest)
    
    