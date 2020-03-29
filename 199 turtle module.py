# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 13:18:41 2020

@author: David
"""

from turtle import *
color('blue', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()