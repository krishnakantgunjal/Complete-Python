# 🔁 3. For Loops in Python
# Q:
# Print this pattern using a for loop:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# (Use nested for loops)

for i in range (1,6):
    for x in range (1,i+1):
       print(x,end="")
    print("")
    
    
   
