class Shoe:
    def __init__ (self, brand, color):
        self.brand = brand
        self.color = color
    
    def Wearer (self):
        print ("I am wearing a ", self.brand, " ", self.color, " shoe")
        
# Shoe = Wearer ("Nike", "Black")
    
# Shoe.Wearer()

class Soal (Shoe):
    def __init__(self, brand, color, make, size):
        super().__init__(brand, color)
        self.size = size
        self.make = make
            
    def Wearer (self):
        print(f"i am wearing a shoe of {self.brand}, it is color {self.color} and of make {self.make}, and it is number {self.size} in size")
    
# Shoe =  ("Nike", "Blue", "Air Force", 4)
# Shoe.Soal()