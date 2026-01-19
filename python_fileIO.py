"""
Python File Handling - Complete Notes
====================================

Definition:
-----------
File handling in Python is the process of creating, opening, reading,
writing, and deleting files stored on disk. It allows programs to store
data permanently.

This file covers:
1. Opening files
2. Reading files
3. Writing files
4. Creating new files
5. Deleting files and folders
"""

import os

# =====================================================
# 1. OPENING FILES
# =====================================================

"""
open() Function:
----------------
The open() function is used to open a file and returns a file object.

Syntax:
    open(filename, mode)

Common Modes:
-------------
"r"  - Read (default), error if file does not exist
"a"  - Append, creates file if it does not exist
"w"  - Write, overwrites existing content
"x"  - Create, error if file already exists
"t"  - Text mode (default)
"b"  - Binary mode
"""

# Open file in read mode
f = open("demofile.txt", "r")
print("Reading full file:")
print(f.read())
f.close()  # Always close the file

# Using 'with' statement (recommended)
# Automatically closes the file
with open("demofile.txt", "r") as f:
    print("\nUsing with statement:")
    print(f.read())

# =====================================================
# 2. READING PARTS OF A FILE
# =====================================================

"""
Reading Methods:
----------------
read(n)      -> Reads n characters
readline()   -> Reads one line
for loop     -> Reads file line by line
"""

# Read first 5 characters
with open("demofile.txt", "r") as f:
    print("\nFirst 5 characters:")
    print(f.read(5))

# Read first line
with open("demofile.txt", "r") as f:
    print("\nFirst line:")
    print(f.readline())

# Read first two lines
with open("demofile.txt", "r") as f:
    print("\nFirst two lines:")
    print(f.readline())
    print(f.readline())

# Loop through file line by line
with open("demofile.txt", "r") as f:
    print("\nAll lines:")
    for line in f:
        print(line, end="")

# =====================================================
# 3. WRITING TO FILES
# =====================================================

"""
Writing Modes:
--------------
"a" - Append content to the end of file
"w" - Write content (overwrites existing data)
"""

# Append to file
with open("demofile.txt", "a") as f:
    f.write("\nNow the file has more content!")

# Read after appending
with open("demofile.txt", "r") as f:
    print("\nAfter appending:")
    print(f.read())

# Overwrite file content
with open("demofile.txt", "w") as f:
    f.write("Woops! I have deleted the content!")

# Read after overwriting
with open("demofile.txt", "r") as f:
    print("\nAfter overwriting:")
    print(f.read())

# =====================================================
# 4. CREATING NEW FILES
# =====================================================

"""
File Creation Modes:
--------------------
"x" - Creates file, error if file exists
"w" - Creates file if it does not exist
"a" - Creates file if it does not exist
"""

# Create file using "x" mode
try:
    f = open("myfile.txt", "x")
    print("\nFile myfile.txt created successfully")
except FileExistsError:
    print("\nFile already exists")
finally:
    if 'f' in locals():
        f.close()

# Create file using "w" mode
with open("anotherfile.txt", "w") as f:
    f.write("This file was created using 'w' mode")

# =====================================================
# 5. DELETING FILES AND FOLDERS
# =====================================================

"""
os Module:
----------
Used to interact with the operating system.
"""

# Delete a file safely
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
    print("\ndemofile.txt deleted successfully")
else:
    print("\ndemofile.txt does not exist")

# Delete a folder (must be empty)
folder_name = "myfolder"
if os.path.exists(folder_name):
    os.rmdir(folder_name)
    print(f"Folder '{folder_name}' deleted successfully")
else:
    print(f"Folder '{folder_name}' does not exist")

# =====================================================
# IMPORTANT POINTS
# =====================================================

"""
Key Takeaways:
--------------
1. Always close files or use 'with' statement
2. Use 'r' for reading, 'a' for appending, 'w' for writing
3. 'x' mode is safest for creating new files
4. Check existence before deleting files
5. Reading line by line is memory efficient
"""
