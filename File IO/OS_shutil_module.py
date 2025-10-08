
# 3. OS and Shutil Modules

# Use the os module to:
# Print the current working directory
# List all files and folders in the current directory
# Create a new folder my_folder

# Use the shutil module to:
# Copy a file from one folder to another
# Move a file to a new folder
# Delete a file (careful: irreversible!)
import os
print("current working directory",os.getcwd())
print(os.listdir())
# os.mkdir("File IO/ My_floder")

import shutil
#shutil.copy("File IO/tasks.txt","File IO/ My_floder/tasks.txt")
#shutil.move("File IO/tasks.txt","File IO/ My_floder/tasks.txt")
os.remove("File IO\delete.txt")