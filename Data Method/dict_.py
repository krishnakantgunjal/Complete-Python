# 🗂️ 5. Dictionaries and Dictionary Methods
# Q:
# Create a dictionary that stores student names as keys and their marks as values.

# Then:

# Add a new student

# Update marks of one existing student

# Print all keys and values

# Delete the lowest-scoring student

# 📥 Example input:

# {"Krishna": 90, "Anu": 80, "Jay": 70}

d ={"Krishna": 90, "Anu": 80, "Jay": 50}
d["xyz"]=60
print(d)

d["Krishna"]=99
print(d)
print(d.keys())
print(d.values())

low_mark = min(d, key=d.get)
print(low_mark)
d.pop(low_mark)
print(d)