# =====================================================
# PYTHON F-STRINGS & STRING FORMATTING
# =====================================================
# Python f-strings (formatted string literals) allow
# you to embed expressions inside string literals using {}
# Introduced in Python 3.6, they are faster and more readable
# than the older format() method.

# =====================================================
# BASIC F-STRING WITH OPERATIONS
# =====================================================
# You can perform math operations directly inside the placeholders

txt = f"The price is {20 * 59} dollars"
print(txt)  # Output: The price is 1180 dollars

# =====================================================
# USING VARIABLES IN OPERATIONS
# =====================================================
price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)  # Output: The price is 73.75 dollars

# =====================================================
# IF ... ELSE INSIDE PLACEHOLDER
# =====================================================
price = 49
txt = f"It is very {'Expensive' if price > 50 else 'Cheap'}"
print(txt)  # Output: It is very Cheap

# =====================================================
# EXECUTE FUNCTIONS IN PLACEHOLDER
# =====================================================
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)  # Output: I love APPLES

# Custom function example
def myconverter(x):
    """Convert feet to meters"""
    return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)  # Output: The plane is flying at a 9144.0 meter altitude

# =====================================================
# MORE MODIFIERS
# =====================================================
# Format numbers in f-strings
price = 59000
txt = f"The price is {price:,} dollars"  # Comma as thousand separator
print(txt)  # Output: The price is 59,000 dollars

# =====================================================
# FORMATTING TYPES
# =====================================================
# Some useful formatting inside placeholders:
num = 1234.567

print(f"Left align: {num:<10}")
print(f"Right align: {num:>10}")
print(f"Center align: {num:^10}")
print(f"Two decimals: {num:.2f}")
print(f"With plus sign: {num:+.2f}")
print(f"Percentage: {num:.2%}")
print(f"Binary: {255:b}")
print(f"Hex: {255:X}")

# =====================================================
# STRING FORMAT() METHOD
# =====================================================
# Before Python 3.6, we used format() for string formatting
price = 49
txt = "The price is {} dollars"
print(txt.format(price))  # Output: The price is 49 dollars

# Format with 2 decimals
txt = "The price is {:.2f} dollars"
print(txt.format(price))  # Output: The price is 49.00 dollars

# =====================================================
# MULTIPLE VALUES
# =====================================================
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
# Output: I want 3 pieces of item number 567 for 49.00 dollars.

# =====================================================
# INDEX NUMBERS
# =====================================================
# Specify index of arguments to reuse or order them
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
# Output: I want 3 pieces of item number 567 for 49.00 dollars.

# Reuse same value more than once
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
# Output: His name is John. John is 36 years old.

# =====================================================
# NAMED INDEXES
# =====================================================
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))
# Output: I have a Ford, it is a Mustang.
