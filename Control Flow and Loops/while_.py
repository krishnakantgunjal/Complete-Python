# . While Loops in Python
# Q:
# Write a program to reverse a number using a while loop.

# Input: 1234
# Output: 4321

# 📌 Hint: Use % 10 to get last digit, // 10 to remove last digit.
x=int(input("enter a more than three number "))
revers_num=0
while x>0 :
    digit= x%10 #last digit 
    revers_num =revers_num*10+digit 
    x=x//10 # 2 
print(revers_num)


# Input: 45

# Take last digit: 45 % 10 = 5 → revers_num = 0*10 + 5 = 5

# Remove last digit: 45 // 10 = 4

# Next digit: 4 % 10 = 4 → revers_num = 5*10 + 4 = 54

# Remove last digit: 4 // 10 = 0 → stop

# Output: 54 