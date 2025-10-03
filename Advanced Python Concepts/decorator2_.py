# 🔹 2) Decorators – Real-World

# Write a decorator login_required that:

# Prints "Access granted" if user="admin"

# Prints "Access denied" otherwise

# Apply it on a function view_dashboard().

def login_required(func):
    def wrapper():
        user = input("User: ")
        if user == "admin" :
         print("Access granted")
         func()
        else :
         print("Access denied")

    return wrapper

@login_required
def view_dashboard():
    print("Welcome to the dashboard!") 
view_dashboard()