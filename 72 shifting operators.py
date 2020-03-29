# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 17:23:27 2020

@author: David
"""

var = 17
var_right = var >> 1
var_left = var << 1
print(var,var_right,var_left)
print("Programa para transformar un número de decimal a binario")
number = int(input("Ingrese un numero\t"))
a = ""
d = ""
for i in range(8):
    b = str((number//(2**i)) % 2)
    #b = str(b)
    a = a + b
b = list(a)
for i in range(7,0,-1):
    c = b[i]
    d = d + c
    if i == 1:   
        i = 0
        c = b[i]
        d = d + c
print(d)
    