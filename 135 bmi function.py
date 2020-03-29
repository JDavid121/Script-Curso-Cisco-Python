# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 22:17:09 2020

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

# The backslash (\) symbol. If you use it in Python code and end a line 
# with it, it will tell Python to continue the line of code in the next 
# line of code.

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
    
    # function
    return weight/(height**2)
    # function to transform pounds to kg
def pndstokg(pnds):
    return (0.453592*pnds)
    # function to transform feets to m
def feettom(feet,inch):
    return 0.3048*feet + 0.0254*inch
# Finally, the code is able to answer the question: 
# what is the BMI of a person 5'7" tall and weighing 176 lbs?
print(bmi(57.0,1.45))
print(pndstokg(176))
print(feettom(5,7))
print(bmi(pndstokg(176.0),feettom(5,7)))
print(bmi(weight = pndstokg(176),height = feettom(5,7)))

# write a function to introduce directly the weight in pounds and height in 
# feets and inches

def bmi2(weight,feet,inche): # bmi function in pounds and feets and inches
    height = feet + inche/12
    #restrictions:
    if weight <= 44: # less weight in pnds 
        print("weight is less than I have spected")
        return None
    if weight >= 440: # high weight in pnds
        print("weight is higher than I have spected")
        return None
    if height <= 3.28: # less height in feets
        print("height is less than I have spected")
    if height >= 8.20: # high height in feets
        print("height is higher than I have spected")
        return None
    
    return (weight*0.453592)/((height*0.3048)**2)

print(bmi2(176,5,7))