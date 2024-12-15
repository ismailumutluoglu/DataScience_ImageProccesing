# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 22:03:53 2024

@author: pc
"""

import numpy as np 

#stacking arrays

array1 = np.array([[1,2],[2,3],[4,5]])
array2 = np.array([[6,7],[8,9],[10,11]])
arr = np.vstack((array1, array2)) ##BİRLESTİRME
print(arr)
arr = np.hstack((array1, array2)) ##BİRLESTİRME
print(arr)
arr = arr.ravel()
print(arr)

