# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 00:05:25 2020

LABORATORY

Scenario
Listen to this story: a boy and his father, a computer programmer, 
are playing with wooden blocks. They are building a pyramid.

Their pyramid is a bit weird, as it is actually a pyramid-shaped wall 
- it's flat. The pyramid is stacked according to one simple principle: 
each lower layer contains one block more than the layer above.

Your task is to write a program which reads the number of blocks 
the builders have, and outputs the height of the pyramid that can be built 
using these blocks.

Note: the height is measured by the number of fully completed layers 
- if the builders don't have a sufficient number of blocks and cannot 
complete the next layer, they finish their work immediately.

Test your code using the data we've provided.

@author: David
"""

#Programa que evalúa la altura (en bloques) de una pirámide

nblocks = int(input("Ingrese el número de bloques\t"))
counter = 0
b = 0 #acumulador de número de bloques
a = 0 #Indicador número de piso
#for i in range (1,10):
while (True):
    a = a + 1             #contador de número de pisos
    b = b + a             #acumulador de número de bloques
    #print (a,end = " ")
    #print (b,end = " ")
    #print("\n")
    if (b-nblocks) == 0:
        print("número de bloques",nblocks)
        print ("The height of the pyramid is:",a)
        break
    if (b >= nblocks):
        c = a - 1         # recálculo del número de pisos
        print("número de bloques",nblocks)
        print ("The height of the pyramid is:",c)
        break

# Para resolver el problema se hizo:
# Una tabla comparativa n = 1,3,6,10,15,21,28 (número de bloques)
                      # p = 1,2,3,04,05,06,07 (altura de la pirámide)
# a = a + 1 es un contador interno al lazo while a = 1,2,3...
# b = b + a suma el número de bloque acorde con el contador a
# si b - nblocks == 0: el número de bloques ingresados sirve para hacer
                    #pisos enteros
# si b > nblocks: el número de bloques ingresados no es suficiente para
        # hacer un piso completo
        # num pisos c = a -1
    
    
