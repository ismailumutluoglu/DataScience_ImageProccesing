# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:30:34 2024

@author: pc
"""
#%% for loop
for i in range(1,12):
    print(i)

for j in "ankara istanbul":
    print(j)

for k in "ankara istanbul".split():
    print(k)

liste = [1,2,3,4,5,6,7,8,9,10]


sum = 0
for i in liste :
    sum = sum + i 

print(sum)

#%% while loop


i = 0 
while i < 4 : 
    print(i)
    i = i + 1 
    
sinir = len(liste)
i = 0
sum = 0 
while i < sinir : 
    sum = sum + liste[i]
    i = i + 1 

print(sum)
