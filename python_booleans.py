# ======================================
# PYTHON BOOLEANS (True / False)
# ======================================

# Boolean values represent True or False
print(10 > 9)     # True
print(10 == 9)    # False
print(10 < 9)     # False


# ======================================
# BOOLEAN WITH IF-ELSE
# ======================================

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


# ======================================
# bool() FUNCTION
# ======================================

# Evaluating values
print(bool("Hello"))   # True
print(bool(15))        # True

# Evaluating variables
x = "Hello"
y = 15

print(bool(x))         # True
print(bool(y))         # True


# ======================================
# MOST VALUES ARE TRUE
# ======================================

print(bool("abc"))
print(bool(123))
print(bool(["apple", "banana", "cherry"]))
print(bool((1, 2)))
print(bool({"name": "Manish"}))


# ======================================
# SOME VALUES ARE FALSE
# ======================================

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


# ======================================
# CUSTOM CLASS BOOLEAN BEHAVIOR
# ======================================

class MyClass:
    def __len__(self):
        return 0

obj = MyClass()
print(bool(obj))   # False


# ======================================
# FUNCTIONS RETURNING BOOLEAN
# ======================================

def myFunction():
    return True

print(myFunction())

if myFunction():
    print("YES!")
else:
    print("NO!")


# ======================================
# BUILT-IN BOOLEAN FUNCTION
# ======================================

x = 200
print(isinstance(x, int))   # True
print(isinstance(x, str))   # False


# ======================================
# PRACTICE QUESTIONS
# ======================================

# Q1. Output kya hoga?
# print(bool(""))

# Q2. Output kya hoga?
# print(bool(0.0))

# Q3. Output kya hoga?
# print(bool([1, 2, 3]))

# Q4. Output kya hoga?
# a = 10
# b = 20
# print(a > b)

# Q5. Output kya hoga?
# def test():
#     return False
# if test():
#     print("YES")
# else:
#     print("NO")

# Q6. Output kya hoga?
# print(isinstance(True, bool))

# Q7. Output kya hoga?
# print(bool(None))

# Q8. Output kya hoga?
# print(bool("False"))


# ======================================
# ANSWERS
# ======================================

# A1. False
# A2. False
# A3. True
# A4. False
# A5. NO
# A6. True
# A7. False
# A8. True
