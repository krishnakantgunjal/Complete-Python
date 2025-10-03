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