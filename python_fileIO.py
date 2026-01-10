"""
Python File Handling
===================

This file covers:
- Opening files
- Reading files
- Writing files
- Creating new files
- Deleting files and folders
"""

import os

# =========================
# 1. Opening Files
# =========================
# open(filename, mode)
# Modes:
# "r" - Read (default), error if file doesn't exist
# "a" - Append, creates file if not exists
# "w" - Write, creates file if not exists
# "x" - Create, error if file exists
# "t" - Text (default)
# "b" - Binary

# Open a file for reading (default)
f = open("demofile.txt", "r")  # or "rt"
print("Read full file:")
print(f.read())
f.close()

# Using with statement (automatically closes the file)
with open("demofile.txt") as f:
    print("Using with statement:")
    print(f.read())

# Open file from a different path
# with open("D:\\myfiles\\welcome.txt") as f:
#     print(f.read())

# =========================
# 2. Reading Parts of a File
# =========================
with open("demofile.txt") as f:
    print("First 5 characters:")
    print(f.read(5))

# Read one line
with open("demofile.txt") as f:
    print("First line:")
    print(f.readline())

# Read two lines
with open("demofile.txt") as f:
    print("First two lines:")
    print(f.readline())
    print(f.readline())

# Loop through file line by line
with open("demofile.txt") as f:
    print("All lines:")
    for line in f:
        print(line, end="")  # avoid extra newlines

# =========================
# 3. Writing to Files
# =========================
# Append content to existing file
with open("demofile.txt", "a") as f:
    f.write("\nNow the file has more content!")

# Read after appending
with open("demofile.txt") as f:
    print("\nAfter appending:")
    print(f.read())

# Overwrite existing content
with open("demofile.txt", "w") as f:
    f.write("Woops! I have deleted the content!")

# Read after overwriting
with open("demofile.txt") as f:
    print("\nAfter overwriting:")
    print(f.read())

# =========================
# 4. Creating New Files
# =========================
# "x" - create, error if exists
try:
    f = open("myfile.txt", "x")
    print("File myfile.txt created successfully")
except FileExistsError:
    print("File already exists")
finally:
    f.close() if 'f' in locals() else None

# "w" or "a" can also create file if not exists
with open("anotherfile.txt", "w") as f:
    f.write("This file was created using 'w' mode")

# =========================
# 5. Deleting Files
# =========================
# Delete file using os.remove()
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
    print("demofile.txt deleted successfully")
else:
    print("demofile.txt does not exist")

# Delete folder using os.rmdir()
# Note: Only empty folders can be deleted
folder_name = "myfolder"
if os.path.exists(folder_name):
    os.rmdir(folder_name)
    print(f"Folder '{folder_name}' deleted successfully")
else:
    print(f"Folder '{folder_name}' does not exist")
