# ================================
# PYTHON STRINGS
# ================================

# String text hota hai jo single (' ') ya double (" ") quotes me likha jata hai
# 'hello' aur "hello" dono same hote hain


# ================================
# PRINTING STRINGS
# ================================

print("Hello")
print('Hello')


# ================================
# QUOTES INSIDE QUOTES
# ================================

# Agar string ke andar quotes chahiye,
# to outer quotes alag type ke hone chahiye

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


# ================================
# ASSIGN STRING TO VARIABLE
# ================================

a = "Hello"
print(a)


# ================================
# MULTILINE STRINGS
# ================================

# Triple double quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Triple single quotes
b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b)

# Note:
# Line breaks output me waise hi aate hain jaise code me likhe gaye hain


# ================================
# STRINGS ARE ARRAYS
# ================================

# Python me string characters ka collection hoti hai
# Indexing 0 se start hoti hai

a = "Hello, World!"
print(a[1])   # e print karega


# ================================
# LOOP THROUGH STRING
# ================================

# String ke har character ko loop me access kar sakte hain

for x in "banana":
    print(x)


# ================================
# STRING LENGTH
# ================================

# len() function string ki length deta hai

a = "Hello, World!"
print(len(a))


# ================================
# CHECK STRING (in)
# ================================

txt = "The best things in life are free!"
print("free" in txt)   # True ya False return karega

# in ko if ke sath bhi use kar sakte hain
if "free" in txt:
    print("Yes, 'free' is present.")


# ================================
# CHECK STRING (not in)
# ================================

print("expensive" not in txt)

# not in ko if ke sath use karna
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")


# ======================================
# PYTHON STRING SLICING
# ======================================

b = "Hello, World!"

# Index 2 se 5 tak (5 include nahi hota)
print(b[2:5])     # llo

# Start se slice
print(b[:5])      # Hello

# End tak slice
print(b[2:])      # llo, World!

# Negative indexing
print(b[-5:-2])   # orl


# ======================================
# MODIFY STRINGS
# ======================================

a = " Hello, World! "

# Upper case
print(a.upper())

# Lower case
print(a.lower())

# Remove extra spaces
print(a.strip())

# Replace characters
print(a.replace("H", "J"))

# Split string
print(a.split(","))


# ======================================
# STRING CONCATENATION
# ======================================

a = "Hello"
b = "World"

# Simple concatenation
c = a + b
print(c)

# With space
c = a + " " + b
print(c)


# ======================================
# STRING FORMATTING
# ======================================

# ❌ This will cause error
# age = 36
# txt = "My age is " + age

# ✅ Using f-string
age = 36
txt = f"My age is {age}"
print(txt)

# Price formatting
price = 59
txt = f"The price is {price} dollars"
print(txt)

# 2 decimal places
txt = f"The price is {price:.2f} dollars"
print(txt)

# Math inside f-string
txt = f"Total price is {20 * 59} dollars"
print(txt)


# ======================================
# ESCAPE CHARACTERS
# ======================================

# Double quote inside string
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# New line
print("Hello\nWorld")

# Tab space
print("Hello\tWorld")

# Backslash
print("This is a backslash \\")


# ======================================
# IMPORTANT STRING METHODS (EXAMPLES)
# ======================================

s = "python programming"

print(s.capitalize())
print(s.title())
print(s.count("p"))
print(s.find("program"))
print(s.startswith("python"))
print(s.endswith("ing"))
print(s.islower())
print(s.upper())
print("-".join(["Python", "is", "awesome"]))


# ======================================
# PRACTICE QUESTIONS
# ======================================

# Q1. Output kya hoga?
# a = "HelloWorld"
# print(a[1:8])

# Q2. Output kya hoga?
# txt = "  Python  "
# print(txt.strip().upper())

# Q3. Output kya hoga?
# a = "Hello"
# b = "123"
# print(a + b)

# Q4. Output kya hoga?
# price = 99
# print(f"Price is {price:.1f}")

# Q5. Output kya hoga?
# txt = "Python"
# print(txt[-4:-1])

# Q6. Output kya hoga?
# print("Hello\nPython")

# Q7. Output kya hoga?
# s = "apple,banana,orange"
# print(s.split(","))

# Q8. Output kya hoga?
# s = "python"
# print(s.isupper())


# ======================================
# ANSWERS
# ======================================

# A1. elloWor
# A2. PYTHON
# A3. Hello123
# A4. Price is 99.0
# A5. hon
# A6.
# Hello
# Python
# A7. ['apple', 'banana', 'orange']
# A8. False
