# 🔹 2) Map, Filter, Reduce

# Given a list of integers:
# nums = [2, 5, 8, 11, 14, 17, 20]

# Use map to create a list of squares.

# Use filter to extract only even numbers.

# Use reduce to calculate the product of all numbers.

# (Hint: import functools.reduce)

import math  
from functools import reduce
nums = [2, 5, 8, 11, 14, 17, 20]

square = list(map(lambda x : math.pow(x,2),nums))
print(square)

even = list(filter(lambda a : a%2== 0 , nums))
print(even)

product_of_numbers = reduce(lambda x, y: x * y, nums)
print(product_of_numbers)