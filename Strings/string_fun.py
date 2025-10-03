# 🧰 3. String Methods and Functions
# Q:
# Given this string:
# data = "  Hello, Python learner! Welcome to strings.  "
# Do the following using string methods:

# Remove extra spaces from both sides

# Count how many times "e" appears

# Check if the string starts with "Hello"

# Replace "Python" with "JavaScript"

# Split the string into a list of words

data = "  Hello, Python learner! Welcome to strings.  "
print(data.strip())
print(data.find("e"))
print(data.strip().startswith("Hello"))
print(data.replace("Python","java"))
print(data.split())
