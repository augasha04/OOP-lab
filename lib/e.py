class Vehicle:
    def __init__ (self, brand, color):
        self.brand = brand
        self.color = color
    
    def drive (self):
        print ("I am driving a ", self.brand, " ", self.color, " vehicle")
        
# car = vehicle ("Toyota", "Black")
    
# car.drive()

class Car (Vehicle):
    def __init__(self, brand, color, make, number_of_wheels):
        super().__init__(brand, color)
        self.number_of_wheels = number_of_wheels
        self.make = make
            
    def drive (self):
        print(f"i am driving a car of {self.brand}, it is color {self.color} and of make {self.make}, and it has {self.number_of_wheels} wheels")
    
car = Car ("Toyota", "Blue", "Audi", 4)
car.drive()