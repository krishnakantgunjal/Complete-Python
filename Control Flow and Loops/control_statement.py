# 🚫 5. Break, Continue, and Pass
# Q:
# You have a list of numbers.

# Print only positive numbers

# If a number is 0, skip it using continue

# If a number is -99, stop the loop using break


# Edit
# numbers = [4, -1, 0, 3, 0, -99, 5, 6]
# Expected Output:

# 4
# 3

num = [4,-1,0,3,0,-99,5,6]

for i in num:
    if i==0 :
        continue
    elif i==-99:
        break
    if i<0 :
        continue
    else:
        print(i)



