# =====================================================
# PYTHON ARRAYS (LISTS)
# =====================================================
# Note: Python does not have built-in arrays, but lists can be used as arrays.

# -----------------------------------------------------
# CREATING ARRAYS (LISTS)
# -----------------------------------------------------
cars = ["Ford", "Volvo", "BMW"]
print("Cars array:", cars)

# -----------------------------------------------------
# ACCESSING ELEMENTS
# -----------------------------------------------------
x = cars[0]  # First element
print("First car:", x)

# Modify the first element
cars[0] = "Toyota"
print("After modification:", cars)

# -----------------------------------------------------
# LENGTH OF AN ARRAY
# -----------------------------------------------------
length = len(cars)
print("Number of cars:", length)

# -----------------------------------------------------
# LOOPING THROUGH ARRAYS
# -----------------------------------------------------
print("Looping through cars:")
for car in cars:
    print(car)

# Using index
print("Loop using index:")
for i in range(len(cars)):
    print(cars[i])

# -----------------------------------------------------
# ADDING ELEMENTS
# -----------------------------------------------------
# Add one element at the end
cars.append("Honda")
print("After append:", cars)

# Add multiple elements
cars.extend(["Mercedes", "Audi"])
print("After extend:", cars)

# Insert element at a specific position
cars.insert(1, "Chevrolet")
print("After insert at index 1:", cars)

# -----------------------------------------------------
# REMOVING ELEMENTS
# -----------------------------------------------------
# Remove by index
cars.pop(1)  # removes "Chevrolet"
print("After pop index 1:", cars)

# Remove by value
cars.remove("Volvo")  # removes first occurrence
print("After removing 'Volvo':", cars)

# Clear all elements
# cars.clear()
# print("After clear:", cars)

# -----------------------------------------------------
# OTHER LIST METHODS
# -----------------------------------------------------
# Copy a list
cars_copy = cars.copy()
print("Copy of cars:", cars_copy)

# Count occurrences
count_bmw = cars.count("BMW")
print("Count of BMW:", count_bmw)

# Find index of a value
index_bmw = cars.index("BMW")
print("Index of BMW:", index_bmw)

# Reverse list
cars.reverse()
print("Reversed cars:", cars)

# Sort list (ascending)
cars.sort()
print("Sorted cars:", cars)

# Sort list (descending)
cars.sort(reverse=True)
print("Sorted cars descending:", cars)

# -----------------------------------------------------
# NOTES:
# 1. Lists in Python are dynamic, mutable, and can store mixed data types.
# 2. For large-scale numerical arrays, consider using NumPy arrays:
#    import numpy as np
#    arr = np.array([1, 2, 3])
