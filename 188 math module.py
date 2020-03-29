# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 09:45:16 2020

@author: David
"""

from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

# write a function that calculates the sin value for a dregree angle
def sinfnc():
    a = float(input("Enter an angle in degrees from 0° to 360°\t"))
    if a < 0:
        print("Angle must be greather than 0°")
        return None
    if a > 360:
        print("Angle must be less than 360°")
        return None
    print(sin(radians(a)))
    # radians(a) trnasform a from degre angle to radian angle
    #sin() sin function from a radian angle
    
    return sin(radians(a))

# write a function that returns a dregree angle from a arc sin value

def arcsinfnc():
    a = float(input("Enter a arc sin value\t"))
    b = degrees(asin(a))
    if b > 0: # I and II cuadrant
        print(b)
        return b
    else: # III and IV cuadrant
        print(180-b)
        return b

sinfnc()
arcsinfnc()


        
    