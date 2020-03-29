# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 23:00:00 2020

COMPUTER LOGIC

@author: David
"""
#make the truth table of AND cojuntion
c = "   "
A = False
B = False
C = A and B
print("A",c,"B",c,"(A) AND (B)")
print("-----------------------")
print(A,c,B,C) 
A = False
B = True
C = A and B
print(A,c,B,C)
A = True
B = False
C = A and B
print(A,c,B,C)
A = True
B = True
C = A and B
print(A,c,B,C)
print("***********************")
#make the truth table of OR cojuntion
c = "   "
A = False
B = False
C = A or B
print("A",c,"B",c,"(A) OR (B)")
print("-----------------------")
print(A,c,B,C) 
A = False
B = True
C = A or B
print(A,c,B,C)
A = True
B = False
C = A or B
print(A,c,B,C)
A = True
B = True
C = A or B
print(A,c,B,C)

# bitwise operators:

# from this byte b = 127 (eight bits)
print("****************")
b = 127
print(b)
# ******************************
# a) which is the state of the 5th bit?
# create a mask of the 5th bit:
print("****************")
b = 127
mask = 16 # 0001 0000 = 16 (decimal) 
state_bit = b & mask # & to determinate the state of a bit
print(state_bit) #the bit is set to 1
# b) Reset the 5th bit
print("******************")
remask = 239 # 1110 1111 = 239
reset_bit = b & remask
areset_bit = b & (~mask) # do this method
print(reset_bit)
print(areset_bit)
# c) Toogle the 5th bit
print("******************")
mask = 16
toggle_bit = b^mask
print(toggle_bit)  