# Print the following pattern using a for loop:
# *
# **
# ***
# ****
x = int(input("enter num for star pattern:-"))
for m in range(0,x+1):
    for n in range(0,m):
        print("*",end="")
    print("")
    