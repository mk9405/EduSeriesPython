# =========================================================
# 1. PYTHON SYNTAX
# =========================================================

"""
Python syntax refers to the rules that define how a Python
program is written and executed.

Python code can be executed in two ways:
1. Directly in the Command Line (Interactive Mode)
2. By creating a .py file and running it
"""

# Example: Python syntax in command line
# >>> print("Hello, World!")

print("Hello, World!")

# =========================================================
# 2. EXECUTE PYTHON USING A FILE
# =========================================================

"""
You can also execute Python code by creating a file
with .py extension and running it from the command line.

Example:
C:\\Users\\Your Name> python myfile.py
"""

print("This code is running from a .py file")

# =========================================================
# 3. PYTHON INDENTATION
# =========================================================

"""
Indentation refers to the spaces at the beginning of a line.

IMPORTANT:
- In Python, indentation is not optional
- It is used to define blocks of code
- Other languages use {} but Python uses indentation
"""

# Correct Indentation Example
if 5 > 2:
    print("Five is greater than two!")

# =========================================================
# 4. INDENTATION ERROR EXAMPLE
# =========================================================

"""
If you skip indentation, Python will give a SyntaxError.
"""

# ❌ Wrong (Do NOT run – for explanation only)
# if 5 > 2:
# print("Five is greater than two!")

# =========================================================
# 5. NUMBER OF SPACES IN INDENTATION
# =========================================================

"""
- You can use any number of spaces (minimum 1)
- Most common and recommended is 4 spaces
- Consistency is very important
"""

# Valid indentation (1 space)
if 10 > 5:
 print("Using 1 space indentation")

# Valid indentation (8 spaces)
if 10 > 5:
        print("Using 8 spaces indentation")

# =========================================================
# 6. INCONSISTENT INDENTATION (ERROR)
# =========================================================

"""
Using different number of spaces in the same block
will cause IndentationError.
"""

# ❌ Wrong (example only)
# if 5 > 2:
#     print("Correct indentation")
#         print("Wrong indentation")

# =========================================================
# 7. PYTHON VARIABLES
# =========================================================

"""
Variables are used to store data.

In Python:
- Variables are created automatically
- No need to declare variable type
"""

# Variable Examples
x = 5
y = "Hello, World!"
z = 3.14

print(x)
print(y)
print(z)

# =========================================================
# 8. VARIABLE RULES (IMPORTANT)
# =========================================================

"""
Variable names:
- Must start with a letter or underscore
- Cannot start with a number
- Are case-sensitive
"""

age = 20
Age = 30  # Different variable

print(age)
print(Age)

# =========================================================
# 9. PYTHON COMMENTS
# =========================================================

"""
Comments are used for documentation.
Python ignores comments during execution.
"""

# This is a single-line comment
print("Comments example")

# =========================================================
# 10. WHY COMMENTS ARE IMPORTANT
# =========================================================

"""
Comments help to:
- Understand code easily
- Explain logic to others
- Debug and maintain code
"""

# =========================================================
# 11. SUMMARY
# =========================================================

"""
- Python syntax is simple and readable
- Indentation is mandatory in Python
- Variables are created automatically
- Comments start with #

"""
