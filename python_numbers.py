# ================================
# PYTHON NUMBERS
# ================================

# Python has three numeric data types:
# 1. int
# 2. float
# 3. complex


# ================================
# NUMERIC TYPES EXAMPLES
# ================================

x = 1        # int
y = 2.8      # float
z = 1j       # complex

print(type(x))
print(type(y))
print(type(z))


# ================================
# INT (INTEGER)
# ================================

# Int is a whole number (positive or negative)
# without decimals and unlimited length

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


# ================================
# FLOAT
# ================================

# Float numbers contain decimal points

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


# Float can also be scientific numbers using 'e'

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


# ================================
# COMPLEX
# ================================

# Complex numbers use 'j' as imaginary part

x = 3 + 5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


# ================================
# TYPE CONVERSION
# ================================

x = 1        # int
y = 2.8      # float
z = 1j       # complex

# int to float
a = float(x)

# float to int
b = int(y)

# int to complex
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Note:
# Complex number cannot be converted to int or float


# ================================
# RANDOM NUMBER
# ================================

# Python uses 'random' module for random numbers

import random

print(random.randrange(1, 10))
