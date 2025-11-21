# 4) Args & Kwargs
# Create a function order_summary(*items, **details) that:
# Accepts multiple food items (*args).
# Accepts details like table=5, waiter="Rahul" (**kwargs).
# Prints a formatted summary of the order.
# Example call:
# order_summary("Pizza", "Burger", "Pasta", table=12, waiter="Anita")
# Output:
# Order Items: Pizza, Burger, Pasta
# Details: table=12, waiter=Anita


def order_summary(*items , **details):
    print("Order Items:", ", ".join(items))
    for x in details:
        print(f"{x}={details[x]} ",end=",")

order_summary("Pizza", "Burger", "Pasta", table=12, waiter="Anita")