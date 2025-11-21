# 🔢 1. Introduction to Lists
# Q:
# Write a program that:

# Accepts 5 numbers from the user and stores them in a list

# Sorts the list in descending order

# Prints the second-largest number

# Then removes all elements greater than 50 from the list


number =[]

for i in range(5):
    num=int(input(f"enter a number {i+1}:-"))
    number.append(num)
print(number)
number.sort()
number.reverse()
print("2nd largest number :-",number[1])
print("Descending :-",number)
new_num=[]
for x in number :
    if(x<=50):
        new_num.append(x)
print(new_num)
number = [x for x in number if x <= 50]
print(number)

