# 🧩 2. Match Case Statements (Python 3.10+)
# Q:
# Write a program that takes a number 1–7 and prints the day of the week using match-case.

# Input: 3
# Output: Wednesday

# Also handle any invalid number with a default case:

# Output: Invalid day number  
while True:

 x=int(input("enter any number between 1-7 for week :-"))
 
 match x:
    case 1:
        print("monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday") 
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("Sunday")                   
    case _: 
         print("Invalid day number")