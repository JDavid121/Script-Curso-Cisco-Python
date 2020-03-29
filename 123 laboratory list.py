# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 22:04:52 2020

LABORATORY

Estimated time: 20-30 minutes

Level of difficulty: Medium

Prerequisites
LAB 4.1.3.6
LAB 4.1.3.7

Objectives
Familiarize the student with:

projecting and writing parameterized functions;
utilizing the return statement;
building a set of utility functions;
utilizing the student's own functions.

Scenario
Your task is to write and test a function which takes three arguments
(a year, a month, and a day of the month) and returns the corresponding 
day of the year, or returns None if any of the arguments is invalid.

Use the previously written and tested functions. Add some test cases 
to the code. This test is only a beginning.

@author: David
"""

def isYearLeap(year):
    if (year >= 1582):
        if ((year % 4) != 0):    
            return False     #print (year," is a common year")
        elif ((year % 100) != 0):
            return True      #print(year," is a leap year")
        elif ((year % 400) != 0):
            return False     #print (year," is a common year")
        else:
            return True      #print(year," is a leap year")
    else:    
        return False         #print (year," is a common year")

def daysInMonth(year, month):
    monthdays = [31,28,30] # days that has each month
    numbermonth = [1,3,5,7,8,10,12] #january,march,may,july, etc
    number2month = [4,6,9,11] #april,june,etc
    for number in numbermonth:
        if month == number:
            return monthdays[0] # january,may,july,august,october,december
            break
    for number in number2month:
        if month == number:
            return monthdays[2]
            break
    if ((month == 2)and isYearLeap(year)):
        return (monthdays[1]+1)
    if (month == 2) and (not(isYearLeap(year))):
        return (monthdays[1])
    if (month < 1) or (month > 12):
        print ("Error Month must be between 1 and 12")
        return None
    
def dayOfYear(year, month, day):
    cumulativedays = 0 # days that has to be sum
    # year: to indicate if a year is leap or not.
    #month: to indicate the number of days per month
    # restrictions:
    # General restrictions:
    if (day > daysInMonth(year,month)):
        print("Error, days must be no more than",daysInMonth(year,month))
        return None
    if isYearLeap(year):
        if (month == 2):
            if (day > 29):
                print("Error, leap year, days must be less than 29")
                return None
    else:
        if (month == 2):
            if (day > 28):
                print("Error, no leap year, days must be less than 28")
                return None
                
    for i in range (1,month):    
        cumulativedays = cumulativedays + daysInMonth(year,i)
    cumulativedays = cumulativedays + day
    return cumulativedays

print(dayOfYear(2000,12,32))
#print(daysInMonth(2001,3))