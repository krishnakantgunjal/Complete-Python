# 🔹 1) Decorators in Python

# Write a decorator timer_decorator that:

# Measures how long a function takes to execute

# Prints the execution time

# Apply it to a function that calculates the factorial of a number.
import time

def timer_decorator(func):
    def wrapper(n):
        start_time = time.time()
        result = func(n)  
        end_time   = time.time()
        execution_time = end_time - start_time
        print("Execution time:", execution_time, "seconds")
        return result   
    return wrapper

@timer_decorator
def fact(n):
    result = 1
    for i in range(1, n + 1):  
        result *= i
    return result
            

f = int(input("Enter a number for factorial :- "))
print("Factorial:", fact(f))
