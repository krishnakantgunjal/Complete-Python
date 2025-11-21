# 0, 1, 1, 2, 3, 5, 8, 13, 21,
i=int(input("enter a number for fabonacci "))
def fab(x):
    if x==0 or x==1:
        return x
    else:
        return fab(x-2)+fab(x-1)

print(fab(i))


