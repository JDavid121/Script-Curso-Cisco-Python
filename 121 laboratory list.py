# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 21:11:07 2020

LABORATORY

Estimated time: 15-20 minutes

Level of difficulty: Medium

Prerequisites: LAB 4.1.3.6

Objectives
Familiarize the student with:

projecting and writing parameterized functions;
utilizing the return statement;
utilizing the student's own functions.
Scenario
Your task is to write and test a function which takes two arguments
(a year and a month) and returns the number of days for the given 
month/year pair (while only February is sensitive to the year value, 
your function should be universal).

The initial part of the function is ready. Now, convince the function 
to return None if its arguments don't make sense.

Of course, you can (and should) use the previously written and tested 
function (LAB 4.1.3.6). It may be very helpful. We encourage you to use a 
list filled with the months' lengths. You can create it inside the function 
- this trick will significantly shorten the code.

We've prepared a testing code. Expand it to include more test cases.

@author: David
"""

# Function that takes two arguments (a year and a month)

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
        return False

def daysInMonth(year, month):
    monthdays = [31,28,30] #table of days that has each month
    if ((month == 1) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12)):
        return monthdays[0] # january,may,july,august,october,december
    if ((month == 3)or(month == 4)or(month == 6)or(month == 9)or(month == 11)):
        # march, april,june,september,november
        return monthdays[2]
    if ((month == 2)and isYearLeap(year)):
        return (monthdays[1]+1)
    if (month == 2) and (not(isYearLeap(year))):
        return (monthdays[1])
    if (month < 1) or (month > 12):
        print ("Error Month must be between 1 and 12")
        return None
        
#print(daysInMonth(1987,0))

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")

