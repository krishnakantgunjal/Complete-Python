# 🧰 2. List Methods
# Q:
# You are given the list:

# fruits = ['apple', 'banana', 'orange', 'apple', 'kiwi']
# Write code that:

# Counts how many times 'apple' appears

# Removes all instances of 'apple' without using a loop

# Inserts 'mango' at index 1

# Reverses the list and prints it

fruits = ['apple', 'banana', 'orange', 'apple', 'kiwi']
print(fruits.count('apple'))
fruits = [fruit for fruit in fruits if fruit != 'apple']
print(fruits)
for x in fruits:
    if x=='apple':
        fruits.remove(x)
print(fruits)

fruits.insert(1, "mango") 
print(fruits)
fruits.reverse()
print("reverse:-",fruits)