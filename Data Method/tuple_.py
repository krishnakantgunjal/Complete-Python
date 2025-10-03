# 🎯 3. Tuples and Operations on Tuples
# Q:
# You are given a tuple:

# data = (4, 7, 2, 7, 9, 7, 3)
# Do the following:

# Count how many times 7 appears

# Convert the tuple to a list

# Replace the first occurrence of 7 with 70 :- 'tuple' object does not support item assignment

# Convert it back to a tuple and print it

data = (4, 7, 2, 7, 9, 7, 3)
print("7 appear :-" ,data.count(7))
x=list(data)
print(x)
index = x.index(7)
x[index] = 70
data2=tuple(x)
print(data2)