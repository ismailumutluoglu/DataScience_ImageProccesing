# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 14:29:24 2024

@author: pc
"""

#if-else c ile aynı 

num1 = int(input("birinci sayiyi giriniz : "))
num2 = int(input("ikinici sayiyi giriniz : "))
num3 = int(input("ucuncu sayiyi giriniz : "))

if num1>num2 and num1>num3:
    print("max value is  : ",num1)
elif num2>num1 and num2>num3:
    print("max value is  : ",num2)
else : 
    print("max value is  : ",num3)
    

liste = [1,2,3,4,5]
value = 3 

if value in liste : 
    print("evet {} listede var".format(value))
else : 
    print("hayir {} listede yok".format(value))
     