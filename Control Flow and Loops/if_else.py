# If-Else Conditional Statements
# Q:
# Write a program that takes a number from the user and prints:

# "Even and divisible by 4" if it's even and divisible by 4

# "Even but not divisible by 4" if only even

# "Odd" otherwise

# Use nested if-else for full logic.
while True:
   x = int(input("enter a number "))
   print(x)
   if x % 2==0 and x % 4==0 :
       print("Even and divisible by 4")
   elif x % 2==0 :
       print("Even but not divisible by 4")    
   else :
       print("odd")    
