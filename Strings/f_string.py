# 🧾 4. String Formatting and f-Strings
# Q:
# Write a program that:

# Takes name, age, and city as input

# Prints this formatted string using f-strings:

# "Hi Krishna, you are 22 years old and live in Pune."

x1=input("enter you name ")
x2=input("enter you age")
x3=input("enter you city ")
template= "Hi {}, you are {} years old and live in {}."
print(template.format(x1,x2,x3))

print(f"Hi {x1}, you are {x2} years old and live in {x3}.")
