# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 00:03:33 2020

TRIANGLE FIELD

@author: David
"""
# function It is a triangle?
def isaTriangle(a,b,c):
    if (a+b) > c:
        if (b+c) > a:
            if (a+c) > b:        
                return True
            else:
                return False
        else:
            return False
    else:
        return False
# ************************************************

def areaTriangle(a,b,c):
    s = (a+b+c)/2 #Heron's formula
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    return area

# main program:
a = float(input("Enter the first triangle side\t"))
b = float(input("Enter the second triangle side\t"))
c = float(input("Enter the third triangle side\t"))

if isaTriangle(a,b,c):
    print("Congratulations! It is a Triangle")
else:
    print("Sorry, It won't be a Triangle")

if isaTriangle(a,b,c):    
    print("The area of the triangle is",areaTriangle(a,b,c),"U^2")
