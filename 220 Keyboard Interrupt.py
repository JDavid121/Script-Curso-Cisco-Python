# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 00:02:42 2020

Keyboard Interrupt

@author: David
"""

# this code cannot be terminated
# by pressing Ctrl-C

from time import sleep
seconds = 0
for i in range (100):
    try:
        print(seconds)
        seconds = seconds + 1
        sleep(1) # second count
        
    except KeyboardInterrupt:
        print("Don't do that!")
        break # ends the for loop