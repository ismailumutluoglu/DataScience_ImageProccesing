#overriding

class Animal: 
    
    def toString(self):
        print("ANIMAL cretead")

class Monkey(Animal):
    def toString(self):
        print("MONKEY createad")
        
animal1 = Animal()
monkey1 = Monkey()
animal1.toString()
monkey1.toString() 
#her iki classtada toString olmasına ragmen Monkey classı
#Animal classındaki toString methodunu override etti.