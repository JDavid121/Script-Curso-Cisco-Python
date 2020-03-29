# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:49:32 2020

PROJECT TIC TAC TOE

@author: David
"""
# import libraries

from random import randrange

# Program to play TIc TAC TOE

# function to draw the board

def DisplayBoard(board):
    pass
    #board = [[0 for i in range(3)] for j in range (3)]
    #print(board)
    
DisplayBoard(1)

# Define board variable board[row][colum]
board = [[0 for i in range(3)] for j in range (3)]
print(board)

# Set initial values to board:
board[0][0] = "1"
board[0][1] = "2"
board[0][2] = "3"
board[1][0] = "4"
board[1][1] = "X"
board[1][2] = "6"
board[2][0] = "7"
board[2][1] = "8"
board[2][2] = "9"
print(board)

# Enter user move:
def move():
usermove = input("Enter your move\t")
move = "O"
if usermove == "1":
    board[0][0] = move
if usermove == "2":
    board[0][1] = "O"
if usermove == "3":
    board[0][2] = move
if usermove == "4":
    board[1][0] = move
if usermove == "6":
    board[1][2] = move
if usermove == "7":
    board[2][0] = move
if usermove == "8":
    board[2][1] = move
if usermove == "9":
    board[2][2] = move
print(board)

# Computer move:

cpumove = randrange(8)
if cpumove == str(usermove):
    
print(cpumove)


    

# the function accepts one parameter containing the board's current status
# and prints it out to the console

