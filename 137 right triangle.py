# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 23:30:30 2020

RIGHT TRIANGLE

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

# function It is a right triangle
def isaRightriangle(a,b,c):
    # right trinagle c^2 = a^2 + b^2
    sidetri = [] # empty list we use to store triangle sides
    sidetri.append(a)
    sidetri.append(b)
    sidetri.append(c)
    sidetri.sort() #sort the sides of the triangle (ascending order)
    #hypotenuse = sidetri[2]
    # catets = sidetri[1],sidetri[0]
    if ((sidetri[2])**2 == (sidetri[1])**2 + (sidetri[0])**2):
        print("The triangle is a right triangle")
        return True
    else:
        print("It is n't a right triangle")
        return False
    
# main program:
a = float(input("Enter the first triangle side\t"))
b = float(input("Enter the second triangle side\t"))
c = float(input("Enter the third triangle side\t"))

if isaTriangle(a,b,c):
    print("Congratulations! It is a Triangle")
else:
    print("Sorry, It won't be a Triangle")

if isaTriangle(a,b,c):    
    isaRightriangle(a,b,c)