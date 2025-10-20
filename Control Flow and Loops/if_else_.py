# Write a program that asks the user for a number and 
# prints whether it is positive, negative, or zero.

while True:   
    x = int(input("Enter a nuber :- "))

    if x>0 :
        print("you enter positive number ",x)
    elif x<0:
        print("you enter negative number ",x)
    else :
        print("you enter a zero ")