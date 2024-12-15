# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 12:09:04 2024

@author: pc
"""

#cemberin cevre uzunlugu = 2*PI*R

#DEFAULT FUNCTİON
r = 2 
def cember_cevresi_hesapla(r , PI = 3.14) : 
    """
    cember cevresi hesapla 
    input = parametre = r 
    output = cemberin cevresi 
    """
    return 2*r*PI

print(cember_cevresi_hesapla(r)),

#FLEXIBLE FUNCTİON

def hesapla(boy,kilo,*args): #tuble konusuna gelince buraya geri dönülecek
    return boy+kilo


#ctrl + 1 ile toplu yorum satırı in speyder

# def hesapla(boy,kilo,yas):
    
#     return (boy+kilo)*yas