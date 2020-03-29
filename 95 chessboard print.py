# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 10:14:38 2020

@author: David
"""

row = ["**  " for i in range(8)]
print(row)
board = [row for i in range(8)]
print(board)

board = []
for i in range(8):
    row = ["EMPTY" for i in range (8)]
    board.append(row)
print (board)