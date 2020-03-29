# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:15:32 2020

@author: David
"""
EMPTY = "-"
ROOK = "Rook"
PAWN = "Pawn"
KNIGHT = "Knight"
BISHOP = "Bishop"
KING = "King"
QUEEN = "Queen"

board = [[EMPTY for i in range(8)] for j in range (8)] # Matrix 8 x 8

# set the rooks

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

# Set white pawns in row 6:
for i in range(8):
    board[6][i]=PAWN
#Set black pawns in row 1:
for i in range(8):
    board[1][i]=PAWN
# Set the knights:
board[0][1]=KNIGHT
board[0][6]=KNIGHT
board[7][1]=KNIGHT
board[7][6]=KNIGHT

# Set the bishops:
board[0][2]=BISHOP
board[0][5]=BISHOP
board[7][2]=BISHOP
board[7][5]=BISHOP

# Set the KINGS AND QUEEN
board[0][3]=KING
board[0][4]=QUEEN
board[7][3]=KING
board[7][4]=QUEEN

print(board)

# PAWN = 1, KNIGHT = 3, BISHOP = 3, ROOK = 5, QUEEN = 9 KING = 11

ROOK = 5
PAWN = 1
KNIGHT = 3
BISHOP = 3
KING = 11
QUEEN = 9

# Set white pawns in row 6:
for i in range(8):
    board[6][i]=PAWN
#Set black pawns in row 1:
for i in range(8):
    board[1][i]=PAWN
# set the rooks
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

# Set the knights:
board[0][1]=KNIGHT
board[0][6]=KNIGHT
board[7][1]=KNIGHT
board[7][6]=KNIGHT

# Set the bishops:
board[0][2]=BISHOP
board[0][5]=BISHOP
board[7][2]=BISHOP
board[7][5]=BISHOP

# Set the KINGS AND QUEEN
board[0][3]=KING
board[0][4]=QUEEN
board[7][3]=KING
board[7][4]=QUEEN
    
print(board)