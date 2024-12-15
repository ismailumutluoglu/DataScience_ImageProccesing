# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:50:22 2024

@author: pc
"""

#EXAMPLE

class Employee: 
    
    counter = 0 #class variable
    def __init__(self,name,surname,maas):
        self.name = name 
        self.surname = surname 
        self.maas = maas 
        Employee.counter = Employee.counter + 1 
    
    def giveNameSurname(self):
        return self.name + " " + self.surname
    

employee1 = Employee("ISMAIL","UMUTLUOGLU",1000)
employee2 = Employee("HASAN","GUMUS",1500)
employee3 = Employee("FARUK","GEYVE",750)
employee4 = Employee("MINE","KILIC",5000)
employee5 = Employee("AYSE","AYSEOGLU",1235)
employee6 = Employee("UMUT","HASANOGLU",5421)
employee7 = Employee("IHSAN","TAYMAS",89787)
employee8 = Employee("OMER","CEM",56732)
employee9 = Employee("T0LGA","TURKOGLU",456)
employee10 = Employee("CAFER","KAZIM",14213)

liste = [employee1,employee2,employee3,employee4,employee5,employee6,employee7,employee8,employee9,employee10]

max_maas = -1 
for each in liste : 
    if (each.maas > max_maas ):
        max_maas = each.maas
        index = each 
        
print(index.giveNameSurname(),max_maas)

