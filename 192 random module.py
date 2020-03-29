# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 10:23:14 2020

@author: David
"""

from random import randrange, randint

print(randrange(0,10,1))

# randrange(begin,end,step)
# takes one pseudorandomly integer value from begin, to end, 
# in the steps

print(randrange(0,10))

# randrange(begin,end)
# takes one pseudorandomly integer value from begin, to end.

print(randrange(10))
# randrange(end)
# takes one pseudorandomly integer value from 0, to end.

print(randint(0,10))
# randint(left,right) euqls to randrange(left,right+1)
# generates one pseudorandomly integer value from left to right +1
