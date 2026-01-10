# ================================
# PYTHON CASTING
# ================================

# Casting ka matlab hota hai:
# kisi value ko ek data type se doosre data type me convert karna

# Python ek object-oriented language hai
# isliye data type conversion constructor functions se hota hai


# ================================
# CASTING FUNCTIONS
# ================================

# int()   -> integer banata hai
# float() -> float number banata hai
# str()   -> string banata hai


# ================================
# INTEGER CASTING
# ================================

x = int(1)       # integer se integer
y = int(2.8)     # float se integer (decimal remove ho jata hai)
z = int("3")     # string se integer (string number hona chahiye)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))


# ================================
# FLOAT CASTING
# ================================

x = float(1)       # integer se float
y = float(2.8)     # float hi rahega
z = float("3")     # string se float
w = float("4.2")   # string decimal se float

print(x)
print(y)
print(z)
print(w)

print(type(x))
print(type(y))
print(type(z))
print(type(w))


# ================================
# STRING CASTING
# ================================

x = str("s1")   # string hi rahega
y = str(2)      # integer se string
z = str(3.0)    # float se string

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))


# ================================
# IMPORTANT NOTES
# ================================

# Agar string number nahi hui:
# int("abc")  -> error aayega
# float("xyz") -> error aayega

# Example (commented to avoid error):
# a = int("hello")
