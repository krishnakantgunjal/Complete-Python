def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return x* fact(x-1)
a=int(input("enter a number for fact"))
print(fact(a))