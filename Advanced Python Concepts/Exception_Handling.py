# 🔹 1) Exception Handling & Custom Errors

# Create a class NegativeNumberError(Exception) for a custom error.

# Write a function square_root(n) that:

# Raises NegativeNumberError if n < 0.

# Otherwise returns the square root.

# Test it with n = -9 and n = 25.

import math
class NegativeNumberError(Exception):
    pass

def square_root(n):
    if n < 0 :
        raise NegativeNumberError(" NegativeNumberError")
    else:
        print(math.sqrt(n))
try :
    x = int(input("Enter the a number for square :-"))
    result = square_root(x)

except Exception as e :
    print("Error:-",e)