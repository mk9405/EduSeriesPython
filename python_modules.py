# =====================================================
# PYTHON MODULES
# =====================================================
# A module is a file containing Python code (functions, variables, classes)
# that you want to include in your application.
# Essentially, a module is like a code library.

# =====================================================
# CREATING A MODULE
# =====================================================
# Save the following code in a file named mymodule.py:

# mymodule.py
def greeting(name):
    print("Hello, " + name)

person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

# =====================================================
# USING A MODULE
# =====================================================
# Import your module using the import statement:

import mymodule

mymodule.greeting("Jonathan")  # Output: Hello, Jonathan

# Access variables in the module
age = mymodule.person1["age"]
print(age)  # Output: 36

# =====================================================
# ALIASING A MODULE
# =====================================================
# You can create an alias for a module using 'as'

import mymodule as mx

print(mx.person1["age"])  # Output: 36
mx.greeting("Alice")      # Output: Hello, Alice

# =====================================================
# BUILT-IN MODULES
# =====================================================
# Python has many built-in modules you can use

import platform

system_name = platform.system()  # Returns OS name
print(system_name)

# =====================================================
# USING dir() FUNCTION
# =====================================================
# The dir() function lists all attributes (functions, variables, etc.) of a module

import platform

print(dir(platform))  # Lists all functions/variables in platform module

# =====================================================
# IMPORTING SPECIFIC ELEMENTS FROM MODULES
# =====================================================
# You can import only what you need using 'from'

from mymodule import person1, greeting

print(person1["age"])  # Output: 36
greeting("Michael")    # Output: Hello, Michael

# =====================================================
# NOTES:
# 1. Module file extension must be .py
# 2. Use module_name.function_name() to access functions
# 3. You can import multiple elements from a module using 'from ... import ...'
# 4. Aliasing helps shorten module names when used repeatedly
# 5. Built-in modules are always available without installation
