class Employee(object):
    age = 20 
    salary = 1000
    
    def ageSalaryRatio(self):
        print(self.age / self.salary)
#function
def ageSalaryRatio(age,salary):
    print(age /salary)
    
    
employee1 = Employee()
employee1.ageSalaryRatio()
ageSalaryRatio(30,3000)