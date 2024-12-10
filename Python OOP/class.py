class car:
    def __init__(self,color,fuel_type,namecar):
        self.color = color
        self.fuel_type = fuel_type
        self.namecar = namecar
    def getdata(self):
        print(f"Color car : {self.color} fuel type : {self.fuel_type} name : {self.namecar}")
car1 = car("red","electric","sedan")
car1.getdata()