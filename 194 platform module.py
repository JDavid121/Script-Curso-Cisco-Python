# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 11:56:59 2020

platform module

@author: David
"""
from platform import platform
print(platform()) # platform returns the name, version of OS
print(platform(1)) # returns alternative names instead of common OS names
print(platform(0,1)) #returs a small view (if it is possible) from the OS name
