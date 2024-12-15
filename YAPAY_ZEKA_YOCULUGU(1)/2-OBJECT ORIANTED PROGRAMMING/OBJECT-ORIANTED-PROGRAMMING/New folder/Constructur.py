#Constructuer

class Dogs(object):
    
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def getAge(self):
        return self.age  
    
    def getName(self):
        return self.name
    
dog1 = Dogs("MORTAS",62)
dog2 = Dogs("CINE",31)
dog3 = Dogs("SMILEEE",20)
print(dog1.getAge())
print(dog2.getAge())
print(dog3.getAge())

print(dog1.getName())
print(dog2.getName())
print(dog3.getName())


    