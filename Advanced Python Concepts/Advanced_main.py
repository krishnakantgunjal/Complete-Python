# 🔹 6) Interview Style (Mix of All)

# Design a class Employee:

# Store name and salary

# Use a property decorator for salary (getter & setter)

# Ensure salary can’t be set to negative

# Use __str__ to print employee info nicely

# Add a class method from_string("Krishna-60000") to create an employee from a string

# Add operator overloading (__gt__) to compare employees by salary (emp1 > emp2)

class Employee:
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary
    
    def __str__(self):
        return f"Emplyee(name:-{self.name} salary:-{self.salary})"
    
    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split("-")  
        salary = int(salary)               
        return cls(name, salary)
 
    
    @property
    def display(self):
        return self.salary
        
    @display.setter
    def display(self,new_salary):
        if new_salary > 0:
            self.salary == new_salary
        else:
            print("salary can’t be set to negative")
    
    def __gt__(self, other):
      return other.salary < self.salary

emp1 = Employee("Krishna", 60000)
print(emp1)
emp1.salary = -10000
print("upadted salary :-",emp1.salary)

emp2 = Employee.from_string("Riya-50000")
print(emp2)

print(emp1 > emp2)
