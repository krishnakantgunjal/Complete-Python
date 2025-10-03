def fact(x):
    if x==0 or x==1:
        return 1
    else:
        result=1
        for i in range(1,x+1):
            result=result*i
    return result
a=int(input("enter a number for fact"))
print(fact(a))