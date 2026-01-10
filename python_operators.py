# =====================================================
# PYTHON OPERATORS – COMPLETE NOTES + EXECUTABLE CODE
# =====================================================

# Operators are used to perform operations on values and variables


# =====================================================
# BASIC OPERATOR EXAMPLE
# =====================================================

print(10 + 5)

sum1 = 100 + 50
sum2 = sum1 + 250
sum3 = sum2 + sum2

print(sum1)
print(sum2)
print(sum3)


# =====================================================
# ARITHMETIC OPERATORS
# =====================================================

x = 15
y = 4

print(x + y)    # Addition
print(x - y)    # Subtraction
print(x * y)    # Multiplication
print(x / y)    # Division (float)
print(x % y)    # Modulus
print(x ** y)   # Exponentiation
print(x // y)   # Floor division


# Division examples
a = 12
b = 5

print(a / b)    # Always float
print(a // b)   # Floor division (integer)


# =====================================================
# ASSIGNMENT OPERATORS
# =====================================================

x = 10
x += 5
print(x)

x -= 3
print(x)

x *= 2
print(x)

x /= 4
print(x)

x %= 3
print(x)

x **= 2
print(x)

x //= 2
print(x)


# Walrus Operator (:=)
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")


# =====================================================
# COMPARISON OPERATORS
# =====================================================

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Chaining comparison
x = 5
print(1 < x < 10)
print(1 < x and x < 10)


# =====================================================
# LOGICAL OPERATORS
# =====================================================

x = 5

print(x > 0 and x < 10)
print(x < 5 or x > 10)
print(not(x > 3 and x < 10))


# =====================================================
# IDENTITY OPERATORS
# =====================================================

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

print(x is not y)

# Difference between is and ==
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)


# =====================================================
# MEMBERSHIP OPERATORS
# =====================================================

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("pineapple" not in fruits)

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)


# =====================================================
# BITWISE OPERATORS
# =====================================================

print(6 & 3)    # AND
print(6 | 3)    # OR
print(6 ^ 3)    # XOR
print(~6)       # NOT
print(6 << 2)   # Left shift
print(6 >> 2)   # Right shift


# =====================================================
# OPERATOR PRECEDENCE
# =====================================================

print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
print(5 + 4 - 7 + 3)


# =====================================================
# PRACTICE QUESTIONS
# =====================================================

# Q1. Output kya hoga?
# print(10 + 5 * 2)

# Q2. Output kya hoga?
# print(20 // 3)

# Q3. Output kya hoga?
# print(5 > 3 and 5 < 10)

# Q4. Output kya hoga?
# print(5 == 5 or 5 == 10)

# Q5. Output kya hoga?
# x = [1, 2, 3]
# y = x
# print(x is y)

# Q6. Output kya hoga?
# print("a" in "banana")

# Q7. Output kya hoga?
# print(6 & 2)

# Q8. Output kya hoga?
# print(not(10 > 5))

# Q9. Output kya hoga?
# print(2 ** 3 ** 2)

# Q10. Output kya hoga?
# print(100 + 10 / 5)


# =====================================================
# ANSWERS
# =====================================================

# A1. 20
# A2. 6
# A3. True
# A4. True
# A5. True
# A6. True
# A7. 2
# A8. False
# A9. 512
# A10. 102.0
