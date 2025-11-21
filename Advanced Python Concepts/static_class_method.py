# 4) Static & Class Methods

# Create a class MathOperations with:

# A @staticmethod that checks if a number is even

# A @classmethod that counts how many objects of MathOperations were created

# Test both methods.

class MathOperation :
    count = 0
    def __init__(self):
        MathOperation.count +=1 

    @staticmethod
    def Even_num(x):
        if x % 2 == 0 :
            print("it is even")
        else:
           print("it is not even") 
    
    @classmethod
    def Total_count(cls):
        return cls.count

m = MathOperation()
m.Even_num(5)
print("Number of MathOperations objects:", m.Total_count())