# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 18:42:56 2024

@author: pc
"""

#NUMPY -----1 


#importing 

import numpy as np 

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) # 1*4 lük vektör

print(array.shape)

a = array.reshape(5,3)
print(a)
print("shape", a.shape)
print("dimension",a.ndim)
print("data type ",a.dtype.name)
print("size : ", a.size)
print("type : ",type(a))

array1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(array1)
print(array1.shape)

zeros = np.zeros((3,4))
zeros[2,3]= 58
print(zeros)
np.ones((3,4))
np.empty((3,4))

a = np.arange(10,105,5)
print(a)
a = np.linspace(10,50,20)
print(a)