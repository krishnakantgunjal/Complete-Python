# 4) Instance and Class Attributes
# Create a class Employee with:
# A class attribute company = "TCS"
# Instance attributes name and salary (from constructor)
# A method to display employee info
# Create 2 employees and show how class vs instance attributes behave


class Employee:
    company = "TCS"
    def __init__(self,name,salary,compay):
        self.name = name 
        self.salary = salary
        self.company =compay
        pass
    def employee_info(self):
        print(f"Name :- {self.name}\nSalary :- {self.salary}\nCompany :- {self.company}\n")
e1 = Employee("k",900000,"META")
e2 = Employee("M",60000,"APPLE")
print(e1.company)
print(Employee.company,"\n")

e1.employee_info()
e2.employee_info()