# 1) Introduction to OOP
# Create a class Car with attributes brand, model, and year. Add a method display_info() to print all details.
# Create 2 car objects and call the method for each.

class Car:
    def __init__(self,brand,model,year):
        self.brand = brand 
        self.model = model
        self.year  = year
    def display_info(self):
        return f"brand:-{self.brand} \nmodel:-{self.model} \nyear:-{self.year}\n"

car1 = Car("BMW","M5",2000)
print(car1.display_info())
car2 = Car("Porche","911",2003)
print(car2.display_info())