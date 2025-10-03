# b) Operator overloading:
# Create a class Book with attribute pages.
# Overload + operator so that adding two Book objects returns the total number of pages.

class Book:
    def __init__(self, pages):
        self.pages = pages

    def Add(self):
        return self.pages

b1 = Book(150)
b2 = Book(200)

x1 = b1.Add()  
x2 = b2.Add()  
total_pages = x1 + x2

print("Total pages:", total_pages)