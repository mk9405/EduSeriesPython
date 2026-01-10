# =====================================================
# PYTHON TUPLES – COMPLETE NOTES + EXECUTABLE CODE
# =====================================================

# Tuples are used to store multiple items in a single variable
# Tuples are ordered and unchangeable (immutable)
# Tuples allow duplicate values
# Tuples are written with round brackets ()

# =====================================================
# CREATE TUPLES
# =====================================================
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuples can have duplicate values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple length
print(len(thistuple))

# Tuple with one item (comma required)
thistuple = ("apple",)
print(type(thistuple))

# Not a tuple
thistuple = ("apple")
print(type(thistuple))

# Tuple with different data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")
print(tuple1, tuple2, tuple3, tuple4)

# Check type
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# Using tuple() constructor
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)


# =====================================================
# ACCESS TUPLE ITEMS
# =====================================================
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])    # second item
print(thistuple[-1])   # last item

# Range of indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])  # Index 2 to 4
print(thistuple[:4])    # start to index 3
print(thistuple[2:])    # index 2 to end
print(thistuple[-4:-1]) # negative index

# Check if item exists
if "apple" in thistuple:
    print("Yes, 'apple' is in the tuple")


# =====================================================
# UPDATE TUPLES (Workarounds)
# =====================================================
x = ("apple", "banana", "cherry")
y = list(x)       # convert to list
y[1] = "kiwi"
x = tuple(y)      # convert back to tuple
print(x)

# Add items by converting to list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# Add tuples to tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

# Remove items by converting to list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# Delete entire tuple
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple)  # will raise error


# =====================================================
# UNPACK TUPLES
# =====================================================
fruits = ("apple", "banana", "cherry")

# Unpack
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Using asterisk *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)


# =====================================================
# LOOP TUPLES
# =====================================================
thistuple = ("apple", "banana", "cherry")

# For loop
for x in thistuple:
    print(x)

# Loop by index
for i in range(len(thistuple)):
    print(thistuple[i])

# While loop
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1


# =====================================================
# JOIN & MULTIPLY TUPLES
# =====================================================
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

# Join tuples
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)


# =====================================================
# TUPLE METHODS
# =====================================================
# count() - returns number of times a value occurs
# index() - returns first index of a value

thistuple = ("apple", "banana", "cherry", "apple")
print(thistuple.count("apple"))  # 2
print(thistuple.index("banana"))  # 1


# =====================================================
# PRACTICE QUESTIONS
# =====================================================
# Q1. Print the first and last item of a tuple
# Q2. Try changing the second item (should show workaround)
# Q3. Add "grape" to the tuple
# Q4. Remove "apple" from the tuple
# Q5. Unpack the tuple into variables
# Q6. Loop through the tuple using for loop
# Q7. Loop through the tuple using while loop
# Q8. Join two tuples
# Q9. Multiply a tuple by 3
# Q10. Use count() and index() methods


# =====================================================
# ANSWERS / HINTS
# =====================================================
# A1. print(mytuple[0], mytuple[-1])
# A2. Convert tuple to list, update, convert back to tuple
# A3. Use tuple addition or convert to list and append
# A4. Convert to list, remove, convert back
# A5. (a, b, c) = mytuple
# A6. for x in mytuple: print(x)
# A7. i = 0; while i < len(mytuple): print(mytuple[i]); i += 1
# A8. tuple1 + tuple2
# A9. mytuple * 3
# A10. mytuple.count("apple"); mytuple.index("banana")
