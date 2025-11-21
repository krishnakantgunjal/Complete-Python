# __add__, __sub__, __mul__, etc. – Operator Overloading
# These methods allow you to define how your objects behave 
# with standard arithmetic and comparison operator

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector( self.x + other.x , self.y + other.y)
    
    def __sub__(self,other):
        return Vector( self.x - other.x , self.y - other.y)
    
    def __truediv__(self,other):
        return Vector( self.x / other.x , self.y / other.y)
    
    def __mul__(self,other):
        return Vector( self.x * other.x , self.y * other.y)
    
    def __str__(self): 
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 3)
print(v1 + v2)
print(v1 - v2)
print(v1 / v2)
print(v1 * v2)
