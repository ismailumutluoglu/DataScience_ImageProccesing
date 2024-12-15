# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 21:45:24 2024

@author: pc
"""

import numpy as np 

array = np.array([[1,2,3],[4,5,6],[7,8,9]])

array1 = array.ravel() #deep learningte kullanıyor önemli bir method

array2 = array1.reshape(3,3)

arrayT = array2.T

print(arrayT.shape)


array5 = np.array([[1,2],[3,4],[5,6]])

print(array5.reshape(2,3))
print(array5)
print(array5.ravel())