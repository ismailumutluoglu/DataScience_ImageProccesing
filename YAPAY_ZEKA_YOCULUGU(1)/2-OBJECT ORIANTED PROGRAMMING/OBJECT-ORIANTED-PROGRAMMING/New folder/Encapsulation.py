#ENCAPSULATION
class BankAccount(object):
    def __init__(self,name , money , address):
        self.name = name #global 
        self.__money = money #Private oldu __ böyle yapınca 
        self.address = address
        #Encapsulatinoda get and set metotlarını kullanacağız 
    
    def getMoney(self):
        return self.__money 
    
    def setMoney(self,amount):
        self.__money = amount
        
    def __increaseMoney(self): #metotuda private yaptık  dışarıdan erişim engellendi
        self.__money = self.__money + 300 
        
        
        
        
        
Person1 = BankAccount("Ismail" , 2000 , "SAFRANBOLU")
Person2 = BankAccount("DANIEAL" , 1500 , "NEWYORK")

print(Person1.getMoney())
Person1.setMoney(5000)
Person1.increaseMoney()
print(Person1.getMoney())