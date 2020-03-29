# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:26:49 2020

How many numbers have you hit in a lotery game?

@author: David
"""
# Enter the lottery numbers list
print("Lottery Number List")
a = int(input("How many lottery numbers we have?\t"))
mlists =[]
for i in range(1,a+1,1):
    b = int(input("Enter the {} lottery number\t".format(i)))
    mlists.append(b)
pass
print("\nLottery numbers sets...")
print(mlists)

# Enter the lottery numbers buyed
print("Lottery Number Buyed")
a = int(input("How many lottery numbers buyed?\t"))
nlst =[]
for i in range(1,a+1,1):
    b = int(input("Enter the {} lottery number buyed\t".format(i)))
    nlst.append(b)
pass
print("\nLottery numbers buyed...")
print(nlst)



#Compare each list:
a = 0 # match counter
# mlists lottery number list
# nlst lottery numbers buyed
#len(nlst) > len(mlists)
for i in range(len(nlst)): #evaluate each element in the list nlst
    for j in range(len(mlists)): # evaluate each element in the mlists
        if (nlst[i] == mlists[j]):
            a = a + 1 #match founded increase the counter
print ("Matchs founded...",a)

# ****************************

# Second program way (using one for loop)

#drawn = [5, 11, 9, 42, 3, 49]
#bets = [3, 7, 11, 42, 34, 49]

bets = nlst[:]
drawn = mlists[:]
hits = 0
for number in bets:
    if number in drawn:
        hits += 1

print(hits)
