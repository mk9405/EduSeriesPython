# =====================================================
# PYTHON FOR LOOPS
# =====================================================

# -----------------------------------------------------
# BASIC FOR LOOP
# -----------------------------------------------------
# Iterating over a sequence (list, tuple, set, string, dictionary)
fruits = ["apple", "banana", "cherry"]
print("Basic for loop over a list:")
for x in fruits:
    print(x)

# Looping through a string
print("\nLooping through a string:")
for letter in "banana":
    print(letter)

# -----------------------------------------------------
# BREAK STATEMENT
# -----------------------------------------------------
# Stop the loop before it has looped through all items
print("\nUsing break in for loop:")
for x in fruits:
    print(x)
    if x == "banana":
        print("Breaking loop at:", x)
        break

# Break before the print
print("\nBreak before print:")
for x in fruits:
    if x == "banana":
        break
    print(x)

# -----------------------------------------------------
# CONTINUE STATEMENT
# -----------------------------------------------------
# Skip the current iteration
print("\nUsing continue in for loop:")
for x in fruits:
    if x == "banana":
        continue
    print(x)

# -----------------------------------------------------
# RANGE FUNCTION
# -----------------------------------------------------
# Loop through a sequence of numbers
print("\nUsing range() function:")
for x in range(6):  # 0 to 5
    print(x)

# Using start parameter
print("\nRange with start parameter (2 to 5):")
for x in range(2, 6):
    print(x)

# Using step parameter
print("\nRange with step parameter (2 to 29, step 3):")
for x in range(2, 30, 3):
    print(x)

# -----------------------------------------------------
# ELSE IN FOR LOOP
# -----------------------------------------------------
# Executed when loop finishes normally (not with break)
print("\nFor loop with else:")
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Else skipped due to break
print("\nFor loop with break skips else:")
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("This will NOT be printed")

# -----------------------------------------------------
# NESTED LOOPS
# -----------------------------------------------------
# Loop inside a loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

print("\nNested loops example:")
for a in adj:
    for f in fruits:
        print(a, f)

# -----------------------------------------------------
# PASS STATEMENT
# -----------------------------------------------------
# Placeholder for empty loops
print("\nUsing pass in for loop:")
for x in [0, 1, 2]:
    pass  # Loop exists but does nothing
print("Loop executed but did nothing due to pass")

# -----------------------------------------------------
# PRACTICAL EXAMPLES
# -----------------------------------------------------

# Example 1: Sum numbers 1 to 5
total = 0
for i in range(1, 6):
    total += i
print("\nSum of 1 to 5:", total)

# Example 2: Print even numbers less than 10
print("\nEven numbers less than 10:")
for i in range(10):
    if i % 2 != 0:
        continue
    print(i)

# Example 3: Multiplication table of 5
print("\nMultiplication table of 5:")
for i in range(1, 11):
    print("5 x", i, "=", 5*i)

# Example 4: Nested loop - coordinate points
print("\nCoordinate points (x, y) for 0-2:")
for x in range(3):
    for y in range(3):
        print(f"({x},{y})")

# Example 5: Count characters in a string
word = "python"
count = 0
for letter in word:
    count += 1
print("\nNumber of letters in 'python':", count)

# -----------------------------------------------------
# PRACTICE QUESTIONS
# -----------------------------------------------------
# Q1. Print numbers from 10 to 1 using a for loop
# Q2. Print all vowels in the string "education"
# Q3. Create a nested loop to print a 3x3 grid
# Q4. Use range to print all multiples of 4 less than 50
# Q5. Use break to stop printing numbers when number > 7
