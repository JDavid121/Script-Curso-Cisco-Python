# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 13:26:37 2020

LABORATORY

Level of difficulty: Easy

Objectives:
Familiarize the student with:
    °projecting and writing parameterized functions;
    °utilizing the return statement;
    °testing the functions.
Scenario
Your task is to write and test a function which takes one argument (a year) 
and returns True if the year is a leap year, or False otherwise.

The seed of the function is already sown in the skeleton code in the editor.

Note: we've also prepared a short testing code, which you can use to test your
function.

The code uses two lists - one with the test data, and the other containing 
the expected results. The code will tell you if any of your results 
are invalid.

@author: David
"""

def isYearLeap(year):
    # Program that identifies if a year is leap or common
    # Reference: 45 laboratory.py

    #if the year number isn't divisible by four, it's a common year;
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
        return False             #print(year," not within the Gregorian calendar period")
# end of function

# Test of function
        
testData = [1900, 2000, 2016, 1987]      # Data Test of function
testResults = [False, True, True, False] #Test result
for i in range(len(testData)): # evaluate testData
	yr = testData[i]           # take data test from testData
	print(yr,"->",end="")
	result = isYearLeap(yr)   # take a result form isYearLeap function
	if result == testResults[i]: # compare results
		print("OK")
	else:
		print("Failed")
