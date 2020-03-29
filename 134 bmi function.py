# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 12:24:02 2020

Some simple functions: evaluating the BMI
Let's get started on a function to evaluate the Body Mass Index (BMI).

BMI = weight[kg]/(height[m])^2

As you can see, the formula gets two values:

weight (originally in kilograms)
height (originally in meters)

It seems that this new function will have two parameters. 
Its name will be bmi, but if you prefer any other name, use it instead.

The function fulfils our expectations, but it's a bit simple - 
it assumes that the values of both parameters are always meaningful. 
It's definitely worth checking if they're trustworthy.

Let's check them both and return None if any of them looks suspicious.

@author: David
"""
def bmi(weight,height):
    #restrictions:
    if weight <= 20:
        print("weight is less than I have spected")
        return None
    if weight >= 200:
        print("weight is bigger than I have spected")
        return None
    if height <= 1.0:
        print("height is less than I have spected")
    if height >= 2.50:
        print("height is bigger than I have spected")
        return None
    return weight/(height**2)

print(bmi(57.0,1.45))
