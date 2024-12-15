#Polymorphism

class Employee:
    
    def raisee(self):
        raise_rate = 0.1
        result =  100 + 100*raise_rate
        print(result)
        
class CompEng(Employee):
    
    def raisee(self):
        raise_rate = 0.2
        result =  100 + 100*raise_rate
        print(result)
        
class EEE(Employee):
    
    def raisee(self):
        raise_rate = 0.3
        result =  100 + 100*raise_rate
        print(result)
        
employee1 = Employee()
employee2 = CompEng()
employee3 = EEE()

employee_list = [employee1,employee2,employee3]

for employee in employee_list : 
    employee.raisee()