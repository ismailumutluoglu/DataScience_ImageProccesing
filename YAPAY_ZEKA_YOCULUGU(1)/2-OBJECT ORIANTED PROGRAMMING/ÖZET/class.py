# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:58:57 2024

@author: pc
"""

# PYTHON OOP CONCEPTS CREATEA A CLASS AND OBJECTS


class Employee : 
    
    def __init__(self,name,surname,age):
        self.name = name 
        self.surname = surname
        self.age = age 
        self.email = name + surname + "@gmail.com"
    def giveNameSurname(self):
        return self.name + " " + self.surname
    
employee1 = Employee("ismail","umutluoglu","20")
print(employee1.name)
print(employee1.surname)
print(employee1.age)
print(employee1.email)

print(employee1.giveNameSurname())