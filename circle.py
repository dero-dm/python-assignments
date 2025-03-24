class circle:
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return 3.14 *(self.radius*self.radius)
    def circumfrence(self):
        return 3.14*(self.radius+self.radius)
circ = circle(9)
print(f"Area:{circ.area()}")
print(f"circumfrence:{circ.circumfrence()}")
 input()

