# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 12:20:08 2020

python version

@author: David
"""

from platform import python_implementation,python_version_tuple

print(python_implementation())
# returns a string denoting the Python implementation
# (expect CPython here, unless you decide to use any non-canonical Python branch)
print("***************************")
print(python_version_tuple())
# returns a three-element tuple filled with:
# the major part of Python's version;
# the minor part;
# the patch level number.
