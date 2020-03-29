# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 21:50:05 2020

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
        return False         #print (year," is a common year")

def daysInMonth(year, month):
    monthdays = [31,28,30] # days that has each month
    numbermonth = [1,3,5,7,8,10,12] #january,may,july, etc
    number2month = [4,6,9,11] #march,april,june,etc
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

#print(daysInMonth(1987,11))

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
