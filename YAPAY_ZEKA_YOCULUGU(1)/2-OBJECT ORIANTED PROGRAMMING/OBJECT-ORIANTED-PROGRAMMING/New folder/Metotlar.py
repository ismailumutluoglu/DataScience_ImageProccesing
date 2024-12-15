#METOTLAR

class Square(object):
    edge = 10  #meter
    area = 0 
    def area1(self):  #self !! self yapmak için tanımlamak gerekiy
        self.area = self.edge * self.edge 
        return self.area
    
s1 = Square()
print(s1)
print(s1.edge)
print("area : ",s1.area1())

s1.edge = 7 
print(s1.edge)
print("area : ",s1.area1())