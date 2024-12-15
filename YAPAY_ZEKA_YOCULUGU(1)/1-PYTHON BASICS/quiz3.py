# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:42:38 2024

@author: pc
"""

#listedeki en kucuk sayiyi bulan fonksiyonu yazalim : 
    
liste = [7,5,8,984,5,1,4,3,46,2]

min = liste[0]

for i in liste:
    if i < min : 
        min = liste[i]

print("listedeki min value is : ",min)