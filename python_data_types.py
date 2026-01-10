"""
=========================================================
PYTHON DATA TYPES – COMPLETE DOCUMENTATION
=========================================================

Author  : Manish Kumar
Purpose : Understanding Built-in Data Types in Python
Format  : .py (Docs + Executable Examples)
"""

# =========================================================
# 1. WHAT ARE DATA TYPES?
# =========================================================

"""
In programming, data type is an important concept.

Data types define:
- What type of data a variable can store
- What operations can be performed on that data

Python supports multiple built-in data types.
"""

# =========================================================
# 2. BUILT-IN DATA TYPES IN PYTHON
# =========================================================

"""
Python has the following built-in data types:

Text Type:
- str

Numeric Types:
- int
- float
- complex

Sequence Types:
- list
- tuple
- range

Mapping Type:
- dict

Set Types:
- set
- frozenset

Boolean Type:
- bool

Binary Types:
- bytes
- bytearray
- memoryview

None Type:
- NoneType
"""

# =========================================================
# 3. GETTING THE DATA TYPE
# =========================================================

"""
You can check the data type of any variable
using the type() function.
"""

x = 5
print(type(x))

# =========================================================
# 4. SETTING DATA TYPES (AUTOMATIC)
# =========================================================

"""
In Python, data type is automatically assigned
when you assign a value to a variable.
"""

x = "Hello World"
print(type(x))

x = 20
print(type(x))

x = 20.5
print(type(x))

x = 1j
print(type(x))

# =========================================================
# 5. SEQUENCE DATA TYPES
# =========================================================

x = ["apple", "banana", "cherry"]   # list
print(type(x))

x = ("apple", "banana", "cherry")   # tuple
print(type(x))

x = range(6)                        # range
print(type(x))

# =========================================================
# 6. MAPPING & SET DATA TYPES
# =========================================================

x = {"name": "John", "age": 36}     # dict
print(type(x))

x = {"apple", "banana", "cherry"}  # set
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
print(type(x))

# =========================================================
# 7. BOOLEAN & NONE DATA TYPES
# =========================================================

x = True
print(type(x))

x = None
print(type(x))

# =========================================================
# 8. BINARY DATA TYPES
# =========================================================

x = b"Hello"            # bytes
print(type(x))

x = bytearray(5)        # bytearray
print(type(x))

x = memoryview(bytes(5))  # memoryview
print(type(x))

# =========================================================
# 9. SETTING SPECIFIC DATA TYPES (CASTING)
# =========================================================

"""
You can explicitly specify data types
using constructor functions.
"""

x = str("Hello World")
print(type(x))

x = int(20)
print(type(x))

x = float(20.5)
print(type(x))

x = complex(1j)
print(type(x))

x = list(("apple", "banana", "cherry"))
print(type(x))

x = tuple(("apple", "banana", "cherry"))
print(type(x))

x = dict(name="John", age=36)
print(type(x))

x = set(("apple", "banana", "cherry"))
print(type(x))

x = frozenset(("apple", "banana", "cherry"))
print(type(x))

x = bool(5)
print(type(x))

x = bytes(5)
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))
