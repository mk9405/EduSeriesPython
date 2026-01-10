"""
=========================================================
PYTHON OUTPUT / PRINT – COMPLETE DOCUMENTATION
=========================================================

NOTE:
- This file works as documentation + runnable code
- Easy to read in VS Code and Mobile
- Beginner friendly
"""

# =========================================================
# 1. PYTHON OUTPUT
# =========================================================

"""
In Python, output means displaying something on the screen.

Python provides a built-in function called print()
to display text or values as output.
"""

# Basic print example
print("Hello World!")

# =========================================================
# 2. PRINTING MULTIPLE LINES
# =========================================================

"""
You can use the print() function as many times as you want.
Each print() call prints output on a NEW LINE by default.
"""

print("Hello World!")
print("I am learning Python.")
print("It is awesome!")

# =========================================================
# 3. USING QUOTES IN PRINT
# =========================================================

"""
Text (string) in Python must be written inside quotes.

Python supports:
- Double quotes  ->  \" \"
- Single quotes  ->  ' '
"""

# Both are valid
print("This will work!")
print('This will also work!')

# =========================================================
# 4. SYNTAX ERROR WITHOUT QUOTES
# =========================================================

"""
If you forget to put text inside quotes,
Python will raise a SyntaxError.
"""

# ❌ Wrong example (Do NOT run)
# print(This will cause an error)

"""
Error:
SyntaxError: invalid syntax
"""

# =========================================================
# 5. PRINT WITHOUT A NEW LINE
# =========================================================

"""
By default, print() ends with a new line.

If you want to print on the SAME LINE,
you can use the 'end' parameter.
"""

print("Hello World!", end=" ")
print("I will print on the same line.")

# =========================================================
# 6. WHY end=\" \" IS USED
# =========================================================

"""
end=\" \" adds a space instead of a new line.
This improves readability of the output.
"""

print("Python", end=" ")
print("is", end=" ")
print("fun!")

# =========================================================
# 7. IMPORTANT POINTS ABOUT print()
# =========================================================

"""
- print() is used for output
- Each print() creates a new line by default
- Quotes are mandatory for text
- end parameter controls line ending
"""

# =========================================================
# 8. SUMMARY
# =========================================================

"""
KEY TAKEAWAYS:
- Use print() to display output
- Text must be inside single or double quotes
- Missing quotes cause SyntaxError
- Use end=\" \" to print on the same line

"""


# =========================================================
# 1. PRINTING NUMBERS IN PYTHON
# =========================================================

"""
The print() function can be used to display numbers.

IMPORTANT:
- Numbers are NOT written inside quotes
- Quotes are only for text (strings)
"""

# Printing numbers
print(3)
print(358)
print(50000)

# =========================================================
# 2. PRINTING MATH EXPRESSIONS
# =========================================================

"""
You can also perform mathematical operations
inside the print() function.
"""

print(3 + 3)    # Addition
print(2 * 5)    # Multiplication
print(10 - 4)   # Subtraction
print(20 / 5)   # Division

# =========================================================
# 3. WHY NUMBERS ARE NOT IN QUOTES
# =========================================================

"""
If numbers are inside quotes, Python treats them as text.
Without quotes, they are treated as numeric values.
"""

print("5")   # Text
print(5)     # Number

# =========================================================
# 4. MIXING TEXT AND NUMBERS
# =========================================================

"""
You can combine text and numbers in one output
by separating them with commas inside print().
"""

print("I am", 35, "years old.")
print("The result is", 10 + 5)

# =========================================================
# 5. MULTIPLE VALUES IN PRINT
# =========================================================

"""
print() can take multiple values separated by commas.
Python automatically adds space between them.
"""

print("Python", "is", "fun", 2026)

# =========================================================
# 6. COMMON BEGINNER MISTAKE
# =========================================================

"""
Wrong example:
print("3 + 3")   -> prints text
print(3 + 3)     -> prints result
"""

print("3 + 3")
print(3 + 3)

# =========================================================
# 7. SUMMARY
# =========================================================

"""
KEY POINTS:
- Numbers are printed without quotes
- print() supports math operations
- Commas allow mixing text and numbers
- Python adds spaces automatically

"""
