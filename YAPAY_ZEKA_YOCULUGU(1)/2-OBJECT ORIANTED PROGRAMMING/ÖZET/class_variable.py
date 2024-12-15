# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:05:03 2024

@author: pc
"""

#class variable

class Employee : 
    
    zam_orani = 1.8 #class variable
    counter = 0 
    def __init__(self,name,surname,maas):
        self.name = name 
        self.surname = surname
        self.maas = maas 
        self.email = name + surname + "@gmail.com"
        Employee.counter = Employee.counter + 1 ##classın counteri ile objenin counteri aynı deil
    def giveNameSurname(self):
        return self.name + " " + self.surname 
    
    def zamYap(self): 
        self.maas = self.maas + self.maas * self.zam_orani
    
employee1 = Employee("ismail","umutluoglu",30000)
print(employee1.giveNameSurname())
print("zamsiz maas : ",employee1.maas)
employee1.zamYap()
print("zamli maas : ",employee1.maas)

employee2 = Employee("bayram","umutluoglu",60000)
print(employee2.counter)