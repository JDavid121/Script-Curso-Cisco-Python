# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:17:05 2020

Imagine a hotel. It's a huge hotel consisting of three buildings, 
15 floors each. There are 20 rooms on each floor. 
For this, you need an array which can collect and process information 
on the occupied/free rooms.

@author: David
"""
# Create the variable

# first variable type: occupied/free rooms a boolean variable is choosen

# Second: Evaluate the problem:
# 3 building x 15 floors in each building x 20 rooms on each floor
# total = 3 x 15 x 20 = 900 elements

# Variable:

state = False

rooms = [[[state for r in range(20)]for f in range(15)]for b in range(3)]
#print(rooms)

# Now you can book a room for two newlyweds: in the second building, on the ten floor, room 14:
rooms[1][9][13]=True # rooms[b][f][r] b: building, f: floor, r: room
                     # b = 1 building 2
                     # f = 9 floor 10
                     # r = 13 room 14
                     
# Release the second room on the fifth floor located in the first building:
rooms[0][4][1] = False

# Check if there are any vacancies on the 15th floor of the third building:

A = rooms[2][14][:]
print(A)

#print any vacancies on the 15th floor of the third building
v = 0 #number of vacancy
for r in range(20):
    if (not rooms[2][14][r]):
        v = v +1
print ("Total vacancy in building 3, flooor 15 are...\t",v)
    
