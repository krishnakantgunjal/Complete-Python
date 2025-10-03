# 3) Walrus Operator (:=)

# Write a program that repeatedly asks for input numbers until the user enters 0.

# Use the walrus operator (:=) inside a while loop.

# Print the running sum of numbers entered.

# Example:
# Enter number: 5  
# Running Sum: 5  
# Enter number: 3  
# Running Sum: 8  
# Enter number: 0  
# Stopped

total = 0
while (n := int(input("Enter number: "))):
    total += n
    print("Running sum:", total)
print("Stopped")