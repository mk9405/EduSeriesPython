# =====================================================
# PYTHON NONE
# =====================================================
# None is a special constant in Python that represents the absence of a value.
# Its data type is NoneType, and None is the only instance of NoneType.

# =====================================================
# ASSIGNING NONE
# =====================================================
x = None
print(x)  # Output: None

# =====================================================
# CHECKING THE TYPE OF NONE
# =====================================================
print(type(x))  # Output: <class 'NoneType'>

# =====================================================
# COMPARING TO NONE
# =====================================================
# To compare a variable with None, use the identity operator 'is' or 'is not'

result = None
if result is None:
    print("No result yet")  # This will be printed
else:
    print("Result is ready")

# Using 'is not' operator
result = None
if result is not None:
    print("Result is ready")
else:
    print("No result yet")  # This will be printed

# =====================================================
# NONE EVALUATES TO FALSE
# =====================================================
# In a boolean context, None is treated as False
print(bool(None))  # Output: False

# =====================================================
# FUNCTIONS RETURNING NONE
# =====================================================
# Functions that do not explicitly return a value return None by default

def myfunc():
    x = 5  # No return statement

x = myfunc()
print(x)  # Output: None

# Example with explicit return None
def myfunc2():
    return None

y = myfunc2()
print(y)  # Output: None
