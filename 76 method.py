# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 09:40:03 2020

@author: David
"""

#Example for using append() and insert() methods:

# Look at the following list:

market_list = ["sugar","rice","soda","fish","tomatoes","onions","soap"]

# lenght of the list
print (len(market_list))

# print list
print(market_list)

# Add the element: apples to the end of the list

market_list.append("apples")

print(market_list)

# Add the element: chesse at the beginning of the list

market_list.insert(0,"chesse")

print(market_list)

# Add the element: wine atl the 3rth position of the list.
# Look what happens

market_list.insert(2,"wine")

# wine becomes the 3rth element, rice hass been shifted to the 4rth, 
# "soda" becomes the 5th, etc

print(market_list)