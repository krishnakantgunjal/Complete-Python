# 6) Method Overriding and Operator Overloading

# a) Method overriding:
# Create a parent class Shape with a method area().
# Create subclass Circle that overrides area() and calculates area using radius.


class Shape :
     def __init__(self,radius):
          self.radius = radius
          pass

class Circle(Shape):
     
     def area(self):
          print("Area :- ", 3.14 * self.radius * self.radius)

c = Circle(5)
c.area()

