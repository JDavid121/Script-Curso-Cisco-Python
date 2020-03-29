# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 11:59:56 2020

@author: David
"""
# Exercise 1:
# What is the output of the following snippet?
print ("**************************************")
print(" EXERCISE 1")
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)
print (lst)

# Exercise 2:
# What is the output of the following snippet?
print ("**************************************")
print(" EXERCISE 2")

lst = [1, 2, 3, 4, 5]
lst2 = []
add = 0

for number in lst:
    add += number
    lst2.append(add)

print(lst2)

# Exercise 3:
# What is the output of the following snippet?
print ("**************************************")
print(" EXERCISE 3")

print(lst)
alist = []
#del alist
print(alist)

# Exercise 4:
# What is the output of the following snippet?
print ("**************************************")
print(" EXERCISE 4")

lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))
