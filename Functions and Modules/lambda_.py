# ⚡ 3. Lambda Functions in Python
# Q:
# Write a lambda function that:

# Accepts a number and returns "Even" or "Odd"

#list: [3, 6, 9, 12]

# Expected Output:
# ['Odd', 'Even', 'Odd', 'Even']

list = [3,6,9,12]
for x in list:
 result = lambda x:"even" if x%2==0 else "odd"
 print(result(x))