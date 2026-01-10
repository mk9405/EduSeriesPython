# =====================================================
# PYTHON RANGE
# =====================================================
# The built-in range() function returns an immutable sequence of numbers.
# Syntax: range(start, stop, step)

# -----------------------------------------------------
# RANGE WITH ONE ARGUMENT
# -----------------------------------------------------
# Only stop is provided; start defaults to 0
r1 = range(10)  # 0 to 9
print("Range 0-9:", list(r1))

# -----------------------------------------------------
# RANGE WITH TWO ARGUMENTS
# -----------------------------------------------------
# Start and stop are provided
r2 = range(3, 10)  # 3 to 9
print("Range 3-9:", list(r2))

# -----------------------------------------------------
# RANGE WITH THREE ARGUMENTS
# -----------------------------------------------------
# Start, stop, and step
r3 = range(3, 10, 2)  # 3,5,7,9
print("Range 3-10 step 2:", list(r3))

# Negative step
r4 = range(10, 0, -2)  # 10,8,6,4,2
print("Range 10-0 step -2:", list(r4))

# -----------------------------------------------------
# USING RANGES IN FOR LOOPS
# -----------------------------------------------------
print("Iterating with range:")
for i in range(5):
    print(i, end=" ")
print("\n")

# -----------------------------------------------------
# SLICING RANGES
# -----------------------------------------------------
r = range(10)
print("Value at index 2:", r[2])  # 2
print("Slice 0-3:", list(r[:3]))  # 0,1,2
print("Slice 3-8 step 2:", list(r[3:8:2]))  # 3,5,7

# -----------------------------------------------------
# MEMBERSHIP TESTING
# -----------------------------------------------------
r = range(0, 10, 2)  # 0,2,4,6,8
print("6 in r:", 6 in r)  # True
print("7 in r:", 7 in r)  # False

# -----------------------------------------------------
# LENGTH OF RANGE
# -----------------------------------------------------
print("Length of range(0,10,2):", len(r))  # 5

# -----------------------------------------------------
# CONVERT RANGE TO LIST
# -----------------------------------------------------
print("List from range(5):", list(range(5)))  # [0,1,2,3,4]
print("List from range(1,6):", list(range(1,6)))  # [1,2,3,4,5]
print("List from range(5,20,3):", list(range(5,20,3)))  # [5,8,11,14,17]
