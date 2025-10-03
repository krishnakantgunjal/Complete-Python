# 5) Inheritance and Polymorphism
# Create a base class Animal with a method sound().
# Create 2 subclasses: Dog and Cat.
# Override sound() to print "Bark" and "Meow" respectively.
# Create objects of both and call sound().

class Animal:
    def Sound(self):
        print("Animal Sound")
        pass
class Dog(Animal):
        def Sound(self):
              super().Sound()
              print("Bark..........")
class Cat(Animal):
        def Sound(self):
              print("meow..........")

d = Dog()
d.Sound()
c = Cat()
c.Sound()
a = Animal()
a.Sound()
