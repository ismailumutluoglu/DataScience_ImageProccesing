# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 14:03:59 2024

@author: pc
"""

#LIST FUTURES
#C arrays 
#C ye nazaran baya kolay 


list1 = [2,254,435,63,"ismail"]

list2 = ["monday","tuesday","wednasday"]

print(list1[1:3])
print(list1[-1])

list1.append("ahmet")
print(list1)
list1.remove("ismail")
print(list1)
list1.reverse()
print(list1)
list1.append(0)
list1.reverse()
print(list1)
list1.append("ismail")

liste3 = [4,5,7,3,9,8,1,58]
liste3.sort()
print(liste3)
liste3.insert(5,10)
print(liste3)
liste3.sort()
print(liste3)