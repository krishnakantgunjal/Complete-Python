# 🔁 4. Recursion in Python
# Q:
# Write a recursive function sum_digits(n) to sum the digits of a number.

# 📥 Input: 1234
# 📤 Output: 10

# (1 + 2 + 3 + 4)

while True :
    x=int(input("enter number "))
    def sum(i):
      if i<10 :
        return i
      else:
        return i%10 + sum(i//10)
    print(sum(x))