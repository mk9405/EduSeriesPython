# =====================================================
# PYTHON MODULES - DETAILED EXPLANATION (IN .PY FILE)
# =====================================================

# -----------------------------------------------------
# WHAT IS A MODULE?
# -----------------------------------------------------
# A module is a Python file (.py) that contains
# functions, variables, classes, or executable code.
# Modules help in code reusability and better organization.
#
# Example:
# If a file name is mymodule.py, then "mymodule" is the module name.


# -----------------------------------------------------
# CREATING A MODULE
# -----------------------------------------------------
# Save the below code in a separate file named: mymodule.py

# ---------- mymodule.py ----------
def greeting(name):
    """
    This function prints a greeting message.
    """
    print("Hello, " + name)


# Dictionary variable inside module
person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}
# ---------------------------------


# -----------------------------------------------------
# USING A MODULE
# -----------------------------------------------------
# To use a module, import it using the import keyword

import mymodule

# Calling function from module
mymodule.greeting("Jonathan")

# Accessing dictionary value from module
print(mymodule.person1["age"])   # Output: 36


# -----------------------------------------------------
# HOW MODULE ACCESS WORKS
# -----------------------------------------------------
# Syntax:
# module_name.function_name()
# module_name.variable_name


# -----------------------------------------------------
# MODULE ALIASING
# -----------------------------------------------------
# Aliasing is used to give a short name to a module

import mymodule as mx

mx.greeting("Alice")
print(mx.person1["country"])


# -----------------------------------------------------
# BUILT-IN MODULES
# -----------------------------------------------------
# Python provides many built-in modules

import platform

# Returns operating system name
system_name = platform.system()
print(system_name)


# -----------------------------------------------------
# USING dir() FUNCTION
# -----------------------------------------------------
# dir() returns all attributes and functions of a module

print(dir(platform))


# -----------------------------------------------------
# IMPORTING SPECIFIC ELEMENTS
# -----------------------------------------------------
# Import only required members from a module

from mymodule import greeting, person1

greeting("Michael")
print(person1["name"])


# -----------------------------------------------------
# ADVANTAGES OF MODULES
# -----------------------------------------------------
# 1. Code reusability
# 2. Better readability
# 3. Easy maintenance
# 4. Faster development
# 5. Organized code structure


# -----------------------------------------------------
# IMPORTANT NOTES (EXAM POINTS)
# -----------------------------------------------------
# 1. Module file extension must be .py
# 2. One module = one Python file
# 3. import loads entire module
# 4. from module import item loads specific items
# 5. as keyword is used for aliasing
# 6. Built-in modules do not need installation


# -----------------------------------------------------
# END OF PYTHON MODULE NOTES
# -----------------------------------------------------



#Question 1

marks = [45, 67, 89, 34, 76, 90]

# (a) Total
total = 0
for m in marks:
    total = total + m
print("Total Marks:", total)

# (b) Highest & Lowest
highest = marks[0]
lowest = marks[0]

for m in marks:
    if m > highest:
        highest = m
    if m < lowest:
        lowest = m

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

# (c) Passing Marks (>=40)
passing = []
for m in marks:
    if m >= 40:
        passing.append(m)

print("Passing Marks:", passing)


#Question 2 - String Program 
s = "Python Programming Language"

# (a) Length
length = 0
for ch in s:
    length += 1
print("Length of String:", length)

# (b) Vowel Count
vowels = "aeiouAEIOU"
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print("Total Vowels:", count)

# (c) Reverse each word
words = s.split()
for w in words:
    print(w[::-1], end=" ")


# Question 3 - dictionary Program 

student = {
    "name": "Rahul",
    "math": 78,
    "science": 85,
    "english": 74
}

# (a) Total Marks
total = 0
count = 0

for key in student:
    if key != "name":
        total += student[key]
        count += 1

print("Total Marks:", total)

# (b) Average
average = total / count
print("Average Marks:", average)

# (c) Grade
if average >= 75:
    print("Grade A")
else:
    print("Grade B")




