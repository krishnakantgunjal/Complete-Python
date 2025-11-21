# 🔤 1. Strings in Python
# Q:
# Write a program that:

# Takes a user's full name (first + last) as input

# Prints the number of characters (excluding spaces)

# Converts the full name to UPPERCASE and title case

# 📥 Sample input:
# krishna Gunjal
# 📤 Sample output:

# Total characters 
# UPPERCASE: KRISHNA GUNJAL
# Title Case: Krishna Gunjal

x=input("enter your name ")
count=0
for i in x :
    if i==" ":
        continue
    else:
        count+=1
print("number of character :-",count)
print("uppercase:-",x.upper())
print("title case :-",x.title())
