# 🔘 4. Sets and Set Methods
# Q:

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# Write code to:

# Find elements common to both sets

# Find elements only in a (not in b)

# Add 7 to set a

# Remove an element from b using .discard() safely (e.g., 10)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c=a.intersection(b)
print(c)
d=a.difference(c)
print(d)
a.add(7)
print(a)

b.discard(10)
print(b)