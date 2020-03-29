# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 15:46:48 2020



@author: David
"""

# import libraries
from random import randrange
print("Welcome to TIC TAC TOE game")
# Define board vaiable:
board = [[0 for i in range(3)] for j in range(3)]
allowedboard = [[0 for i in range(3)] for j in range(3)]
i,j = 0,0
#print(board)

# Fill board variable with initial value:
initvalu = [1,2,3,4,5,6,7,8,9]
for i in range(3):
        board[0][i] = initvalu[i]
for i in range(3):
        board[1][i] = initvalu[i+3]
for i in range(3):
        board[2][i] = initvalu[i+6]
#print(board)

# we could use a dictionary variable to access the board variable

# this dict1 variable will useful to access to the value of board
dict1 = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}
dict2 = {(0,0):1,(0,1):2,(0,2):3,(1,0):4,(1,1):5,(1,2):6,(2,0):7,(2,1):8,(2,2):9}

# which piece must use each player?
def piece(player): # if player = True then is a user player
    if player == True: # if player = False then is a cpu player
        return "O"
    else:
        return "X"
        
# where will be  do the movements?
def move(square,player):
    a,b = 0,0
    for key in dict1.keys():
        if key == square:
            A = dict1[key]
            a,b = A[0],A[1]
            board[a][b] = piece(player)
            return board

def cpumove(): # cpumove function
    square = randrange(8)
    return square

def user_mov(): # user movement function
    square = int(input("User,enter your move\t"))
    return square 

# function that checks a valid cpu movement:
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
def boardcheck():
    allowedmov=[]
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X" or board[i][j] == "O":
                continue
            else:
                allowedmov.append((i,j))
    return allowedmov

def movecheck(alist):
    mcheck=[]
    for element in alist:
        if (element in dict2.keys()):
            mcheck.append(dict2[element])
    return mcheck

    
# Cpu makes the firs move on board[1][1]
#print(move(5,False)) #Cpu target movement
#boardcheck()

# User makes the second movement:
for i in range(3):    
    print(move(user_mov(),True))
    print(boardcheck())
    print(movecheck(boardcheck()))

#randomic cpu third movement
#print(move(cpumove(),False))
#boardcheck()

# User makes the fourth movement:
#print(move(user_mov(),True))
#boardcheck()

                   
                
    
