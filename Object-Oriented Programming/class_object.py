# 2) Classes and Objects in Python
# Create a class Student with attributes name and marks.
# Add a method check_pass() that prints "Pass" if marks ≥ 40, otherwise "Fail".
# Take input for 3 students and display their results.


class Student:
    def check_pass(self,name,marks):
        if marks >= 40 :
            print(f"name :- {name} \nmarks :- {marks}\n PASS\n")
        else :
            print(f"name :- {name} \nmarks :- {marks}\n FAIL\n")

s1 = Student()
s2 = Student()
s3 = Student()
print(s1.check_pass("k",90),s2.check_pass("s",40),s3.check_pass("C",35))