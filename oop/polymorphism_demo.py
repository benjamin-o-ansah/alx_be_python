import math
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Rectangle(Shape):
    def __init__(self, width: float, length: float):
        self.width = width
        self.length = length
        
    def area(self):
        return self.width * self.length
    
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2