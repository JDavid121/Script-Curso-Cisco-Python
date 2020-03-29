# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:29:53 2020

MULTIVARIABLE ARRAY

@author: David
"""
import numpy as np
# Make a multiarray variable to load the following:
# 5 samples of tmperature every day, for 20 days
TEMP = 0.0

airtemp1 = [[TEMP for h in range(5)]for d in range(20)]
print (airtemp1) 

# Fill the airtemp multiarray with random values



#airtemp = [["{0:.2f}".format((100*np.random.rand())) for h in range(5)] for d in range(20)]

# we comment the line airtemp because numpy function random.rand() calculates a new random matrix with every exceution (F5)
print (airtemp)

airtemp1 = airtemp[:]
print("********************")
print(airtemp1)

# take the samples on the 10th day:
print("**************************")
print("samples on the 10th day")
print(airtemp1[9])

# Take the samples at 3 hour each day (20 samples)
print("samples at 3 hour each day")
for day in airtemp1:
    print(day[2])

#determinate the average of the samples at 3 hours
print(" **********  Average  **************")
varsum = 0
for day in airtemp1:
    
    varsum = varsum + float(day[2])
print ("The average is..",(varsum/20))
    
#determinate the highest temperature in the whole mont
print("**************************************")
highest = -100.00
for day in airtemp1:
    
    for temp in day:
        if float(temp) > highest :
            highest = float(temp)
print(highest)

# count the days when the temperature at 3 hours was a least 20°C
a = 0 #counter
for day in airtemp:
    if float(day[3]) >= 20: # day[3] : sample taken at 3 hour per day in airtemp.
        a = a +1
print("The number of days when")
print("the temperature at 3 hour was a least 20°C")
print("is...\t",a)

