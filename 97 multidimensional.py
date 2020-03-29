# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:53:54 2020

Recording a mesure:
 1. Test air temperature 1hour, five times per day.
 2. Test air temperature 20 days per month
 3. design a multiarray variable to recording the air temperature test

@author: David
"""

#temps = [[0.0 for h in range(24)] for d in range(31)]

# Multidimension array:
TEMP = 0.0
# h means hour
# d means day
temperature = [[TEMP for h in range(24)] for d in range(31)]

#Fill the temperature multiarray variable with data
c = 0
for d in range(31):
    for h in range(24):
        temperature[d][h] = c
        c = c + 1
print(temperature)

#To sum all temperatures at 6 am:
s = 0 # sum of the temperatures
for day in temperature: # Day is checked in temperature
    s = s + day[5] # 5 indicates the hour at the day in temperature
                   # the sample was taken at 6 am every day of temperature
                   # multiarray
print (s)

#Average of the temerature:

avr = s/31
print("Average temperature at 6 am",avr)

#Print results:
print(temperature[0][0]) # Day [0], hour[0]
print(temperature[0][1]) #Day [0], hour[1]
# Take the sample at day 22, hour noon:
print(temperature[21][11])
# Take all the samples at day 22
print(temperature[21])
# take all the samples at 6 pm in the month (31 samples)
for day in temperature:
    print(day[17])
