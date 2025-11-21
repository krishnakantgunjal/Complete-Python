# 🧩 1. Defining Functions in Python
# Q:
# Write a function is_prime(n) that:

# Returns True if n is a prime number

# Returns False otherwise

# Then test the function with 5 different numbers

def is_prime(n):
    if n <= 1:
        print("It is not a prime number.")
    else:
        for i in range(2, n):
            if n % i == 0:
                print("It is not a prime number.")
        print("It is a prime number:", n)

x = int(input("Enter number to check a prime number: "))
is_prime(x)
