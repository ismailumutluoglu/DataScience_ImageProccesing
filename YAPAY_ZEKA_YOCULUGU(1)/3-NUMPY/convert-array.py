# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 22:14:31 2024

@author: pc
"""

import numpy as np 

liste= [1,2,3,4] #list
array = np.array(liste) #np.array

liste2 = list(array)

arr = np.array([1,2,3,4])
b = arr 
b[0] = 5 #arr degisir otomatik a ve c de degisir memoryde ayni alana hitap ediyo
c = arr
#bunun önüne böyle geçebiliriz
d = np.array([7,8,9,4])
e = d.copy() 
e[0] = 5 #sadece e degisir 
f = d.copy()

