class Calculator(object):
    
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b
    
    def addition(self):
        return self.num1 + self.num2 
    
    def subtraction(self):
        return self.num1 - self.num2 
    
    def multiplication(self):
        return self.num1 * self.num2 
    
    def division (self):
        return self.num1 / self.num2 
    
print("Select one of them : \n1-)ADDITION\n2-)SUBTRACTION\n3-)MULTIPLICATION\n4-)DIVISION")
selection = int(input("select number in range of (1-4) : "))

while selection < 1 or selection > 4:
    print("invalid selection value please try again later")
    selection = int(input("select number in range of (1-4) : "))
        
number1 = int(input("enter first value : "))
number2 = int(input("enter second value : "))

object1 = Calculator(number1,number2)

if selection == 1: 
    print("number 1 + number2 = {}".format(object1.addition()))
elif selection == 2:
    print("number 1 - number2 = {}".format(object1.subtraction()))
elif selection == 3:
    print("number 1 * number2 = {}".format(object1.multiplication()))
elif selection == 4:
    print("number 1 / number2 = {}".format(object1.division()))

