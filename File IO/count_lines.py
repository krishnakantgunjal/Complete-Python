# 4. Creating Command Line Utilities
# Write a small script count_lines.py that takes a 
# filename as input and prints how many lines are in the file.Example usage:

# python count_lines.py tasks.txt
# # Output: Number of lines: 4
 
 


import sys 

def count_lines(filename):
    with open (filename)as f:
        return len(f.readlines())
    
if __name__=="__main__":
    filename = sys.argv[1]
    num_lines = count_lines(filename)
    print(f"there are {num_lines} lines in {filename}")

