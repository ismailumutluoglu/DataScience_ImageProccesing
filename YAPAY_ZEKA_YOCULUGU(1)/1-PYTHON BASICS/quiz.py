# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 12:24:07 2024

@author: pc
"""

# QUIZ
    
# int variable yas
# string name isim
# fonksiyonu olacak
# fonksiyon print(type(),len,float()) 
# *args soyisim
# default parametre ayakkabi numarasi

age = 5 
name = "ismail"
surname = "umut"

def function_quiz(age,name,*args,foot_num = 28): #default degerler en sona yazılır...
    print("\nmusternin adi : ",name,"\nmusternin yasi : ",age,"\nmusternin ayakkabi numarasi : ",foot_num)
    print(type(name))
    print(float(age))
    
    output = args[0]*age
    return output

result = function_quiz(age,name,surname)

print("args[0]*age =",result)