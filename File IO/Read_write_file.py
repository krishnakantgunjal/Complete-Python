# 🧩 1) File Read & Write – Word Frequency Counter
# Task:
# Write a program that:
# Reads a file named notes.txt
# Counts how many times each word appears (ignore case)
# Writes the word-frequency report to a new file called report.txt
# Example Input (notes.txt):
# Python is easy to learn. Python is powerful.
# Expected Output (report.txt):
# python : 2
# is : 2
# easy : 1
# to : 1
# learn : 1
# powerful : 1
# (Hint: use .lower(), .split(), and a dictionary.)

# Simple Word Frequency Counter


with open("D:\Program Files\Python Language\Complete Python\File IO\ notes.txt", "r") as file:
  text = file.read().lower()   

for char in ".,!?":
    text = text.replace(char, "")

words = text.split()

word_count = {}
for word in words:
    if word in word_count:
      word_count[word] += 1
    else:
      word_count[word] = 1
 

for word, count in word_count.items():
    print(f"{word}:-{count}")
