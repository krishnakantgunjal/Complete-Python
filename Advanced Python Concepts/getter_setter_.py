# 🔹 3) Getters and Setters

# Create a class BankAccount with a private attribute __balance.

# Add a getter method to read balance

# Add a setter method to update balance (only if amount > 0)

# Try to withdraw -500 and see if setter prevents it.

class BankAccount :
    def __init__(self,balance):
        self.__balance =balance 
    
    def get_read(self):
        print("balnce :-",self.__balance)
    
    def set_update(self,amount):
        if amount > 0 :
            self.__balance = amount
        elif amount == 0 :
            self.__balance = self.__balance
        else :
            print("Cannot update balance with negative amount!")

b1 = BankAccount(10)
b1.get_read()
b1.set_update(0)
b1.set_update(-500)
b1.get_read()