# =====================================================
# PYTHON MATH
# =====================================================
# Python has built-in mathematical functions and a math module
# that allows performing advanced mathematical operations.

# =====================================================
# BUILT-IN MATH FUNCTIONS
# =====================================================

# 1. min() - returns the smallest value
x = min(5, 10, 25)
print("Minimum value:", x)  # Output: 5

# 2. max() - returns the largest value
y = max(5, 10, 25)
print("Maximum value:", y)  # Output: 25

# 3. abs() - returns the absolute value (always positive)
z = abs(-7.25)
print("Absolute value:", z)  # Output: 7.25

# 4. pow(x, y) - returns x raised to the power of y (x^y)
p = pow(4, 3)  # 4^3 = 64
print("4 to the power of 3:", p)  # Output: 64

# =====================================================
# MATH MODULE
# =====================================================
# Python has a built-in 'math' module for advanced math operations
import math

# 1. math.sqrt() - returns the square root of a number
sqrt_val = math.sqrt(64)
print("Square root of 64:", sqrt_val)  # Output: 8.0

# 2. math.ceil() - rounds a number upwards to the nearest integer
ceil_val = math.ceil(1.4)
print("Ceiling of 1.4:", ceil_val)  # Output: 2

# 3. math.floor() - rounds a number downwards to the nearest integer
floor_val = math.floor(1.4)
print("Floor of 1.4:", floor_val)  # Output: 1

# 4. math.pi - constant value of π
pi_val = math.pi
print("Value of PI:", pi_val)  # Output: 3.141592653589793

# 5. Other commonly used math module functions:
"""
math.pow(x, y)     - x raised to the power y (similar to built-in pow)
math.factorial(x)  - factorial of x
math.exp(x)        - returns e^x
math.log(x[, base]) - natural log or log with specific base
math.sin(x), math.cos(x), math.tan(x) - trigonometric functions
math.radians(x)    - convert degrees to radians
math.degrees(x)    - convert radians to degrees
math.fabs(x)       - absolute value (float)
math.fmod(x, y)    - modulus of x / y
math.sqrt(x)       - square root of x
math.isqrt(x)      - integer square root
"""

# Example: factorial
fact = math.factorial(5)  # 5! = 120
print("Factorial of 5:", fact)

# Example: logarithm
log_val = math.log(100, 10)  # log base 10 of 100
print("Log base 10 of 100:", log_val)

# Example: trigonometry
angle_deg = 90
angle_rad = math.radians(angle_deg)  # convert to radians
sin_val = math.sin(angle_rad)
print("sin(90°) =", sin_val)
