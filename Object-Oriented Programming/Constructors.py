# 3) Constructors in Python
# Create a class Rectangle with a constructor that initializes length and width.
# Add a method area() to return area.
# Add a method perimeter() to return perimeter.
# Create an object and test both methods.

class Rectangle :
    def __init__(self,length,width):
        self.length = length 
        self.width  = width
    def Area(self):
        a = self.length * self.width 
        print("Area : -",a)
    def Perimeter(self):
        p = 2*( self.length + self.width )
        print("parimeter : -",p)
obj1 = Rectangle(5,6)
obj1.Area() 
obj1.Perimeter()