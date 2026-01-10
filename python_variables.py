"""
=========================================================
PYTHON VARIABLES – COMPLETE DOCUMENTATION
=========================================================

Author  : Manish Kumar
Purpose : Understanding Variables in Python
Format  : .py (Docs + Executable Examples)
"""

# =========================================================
# 1. VARIABLES IN PYTHON
# =========================================================

"""
Variables are containers for storing data values.

In Python:
- No need to declare variables
- Variable is created when a value is assigned
"""

x = 5
y = "John"

print(x)
print(y)

# =========================================================
# 2. DYNAMIC TYPING IN PYTHON
# =========================================================

"""
Python is dynamically typed.
A variable can change its data type.
"""

x = 4        # x is int
x = "Sally"  # x is now string

print(x)

# =========================================================
# 3. CASTING VARIABLES
# =========================================================

"""
Casting is used to specify the data type of a variable.
"""

x = str(3)      # '3'
y = int(3)      # 3
z = float(3)    # 3.0

print(x)
print(y)
print(z)

# =========================================================
# 4. VARIABLE NAMES
# =========================================================

"""
A variable name can be:
- Short (x, y)
- Descriptive (age, car_name, total_amount)
"""

# Legal variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# =========================================================
# 5. VARIABLE NAMING RULES
# =========================================================

"""
Rules:
- Must start with a letter or underscore
- Cannot start with a number
- Can contain letters, numbers, underscore
- Case-sensitive
- Cannot be a Python keyword
"""

age = 20
Age = 30
AGE = 40

print(age)
print(Age)
print(AGE)

# =========================================================
# 6. ILLEGAL VARIABLE NAMES (DO NOT RUN)
# =========================================================

"""
2myvar = "John"
my-var = "John"
my var = "John"
"""

# =========================================================
# 7. MULTI-WORD VARIABLE NAMES
# =========================================================

"""
Common naming styles:
"""

# Camel Case
myVariableName = "John"

# Pascal Case
MyVariableName = "John"

# Snake Case (Most Recommended)
my_variable_name = "John"

# =========================================================
# 8. ASSIGN MULTIPLE VALUES
# =========================================================

"""
Python allows assigning multiple values in one line.
"""

x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

# =========================================================
# 9. ONE VALUE TO MULTIPLE VARIABLES
# =========================================================

x = y = z = "Orange"

print(x)
print(y)
print(z)

# =========================================================
# 10. UNPACK A COLLECTION
# =========================================================

"""
Unpacking allows assigning list/tuple values to variables.
"""

fruits = ["apple", "banana", "cherry"]

x, y, z = fruits

print(x)
print(y)
print(z)

# =========================================================
# 11. GLOBAL VARIABLES
# =========================================================

"""
Variables created outside a function are global variables.
They can be used inside and outside functions.
"""

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

# =========================================================
# 12. LOCAL VS GLOBAL VARIABLE
# =========================================================

x = "awesome"

def myfunc():
    x = "fantastic"   # local variable
    print("Python is " + x)

myfunc()
print("Python is " + x)

# =========================================================
# 13. GLOBAL KEYWORD
# =========================================================

"""
Use the global keyword to create or modify
a global variable inside a function.
"""

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)
