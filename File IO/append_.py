# 🧩 2) File Append – User Notes Logger
# Task:
# Write a Python script that:
# Continuously asks the user for notes (until they type "exit")
# Appends each note to a file user_notes.txt
# After exit, display how many notes were saved
# (Hint: use with open(filename, 'a') and count entries.)

count = 0

with open("File IO/user_notes.txt", "a+") as file:
    while True:
        word = input("Enter a note (type 'exit' to stop): ")
        if word.lower() == "exit":
            file.seek(0)
            print("\nfile:",file.read())
            print("Total notes added:", count)
            break
        file.write(word + "\n")
        count += 1


        