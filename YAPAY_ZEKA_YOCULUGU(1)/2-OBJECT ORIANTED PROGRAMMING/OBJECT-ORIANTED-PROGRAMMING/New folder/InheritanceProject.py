class Website:
    
    def __init__(self,name,surname):
        self.name = name 
        self.surname = surname 
    
    def loginInfo(self):
        print(self.name + " " + self.surname)
    
class Website1:
    
    def __init__(self,name, surname,ids):
        Website.__init__(self, name, surname)
        self.ids = ids 
    
    def loginInfo(self):
        print(self.name + " " + self.surname + " " + self.ids)

class Website2:
    
    def __init__(self, name, surname, email):
        Website.__init__(self, name, surname)
        self.email = email 
    
    def loginInfo(self):
        print(self.name + " " + self.surname + " " + self.email)

website = Website("Ismail","Umutluoglu")
website1 = Website1("Ismail","Umutluoglu","0000000x88888")
website2 = Website2("Ismail","Umutluoglu","ismailumutluoglu10@gmail.com")
website.loginInfo()
website1.loginInfo()
website2.loginInfo()