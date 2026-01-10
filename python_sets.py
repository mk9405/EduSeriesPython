# =====================================================
# PYTHON SETS – COMPLETE NOTES + EXECUTABLE CODE
# =====================================================

# Sets are used to store multiple items in a single variable
# Sets are unordered, unchangeable*, and unindexed
# Sets do not allow duplicates
# Sets are written with curly brackets {}

# =====================================================
# CREATE SETS
# =====================================================
myset = {"apple", "banana", "cherry"}
print(myset)

# Duplicate values will be ignored
myset = {"apple", "banana", "cherry", "apple"}
print(myset)

# True and 1 are considered the same, False and 0 same
myset = {"apple", "banana", True, 1, 2}
print(myset)
myset = {"apple", "banana", False, 0, True}
print(myset)

# Set length
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Set items can be of any data type
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}
print(set1, set2, set3, set4)

# Check type
print(type(myset))

# Using set() constructor
thisset = set(("apple", "banana", "cherry"))  # double round brackets
print(thisset)


# =====================================================
# ACCESS SET ITEMS
# =====================================================
thisset = {"apple", "banana", "cherry"}

# Loop through set
for x in thisset:
    print(x)

# Check presence
print("banana" in thisset)
print("banana" not in thisset)


# =====================================================
# ADD SET ITEMS
# =====================================================
thisset = {"apple", "banana", "cherry"}

# Add single item
thisset.add("orange")
print(thisset)

# Add items from another set
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Add items from any iterable
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


# =====================================================
# REMOVE SET ITEMS
# =====================================================
thisset = {"apple", "banana", "cherry"}

# remove() - raises error if not exists
thisset.remove("banana")
print(thisset)

# discard() - no error if not exists
thisset.discard("apple")
print(thisset)

# pop() - removes random item
x = thisset.pop()
print("Removed:", x)
print(thisset)

# clear() - empties the set
thisset.clear()
print(thisset)

# del - deletes the set completely
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset)  # will raise error


# =====================================================
# LOOP SETS
# =====================================================
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)


# =====================================================
# JOIN SETS
# =====================================================
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

# union() - returns new set
set3 = set1.union(set2)
print(set3)

# | operator - same as union()
set3 = set1 | set2
print(set3)

# join multiple sets
set3 = set1.union(set2, {"John", "Elena"}, {"apple", "bananas", "cherry"})
print(set3)

# update() - changes original set
set1.update(set2)
print(set1)

# intersection() - only duplicates
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

# & operator - same as intersection()
set3 = set1 & set2
print(set3)

# intersection_update() - changes original set
set1.intersection_update(set2)
print(set1)

# difference() - items in first set but not in second
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

# - operator - same as difference()
set3 = set1 - set2
print(set3)

# difference_update() - changes original set
set1.difference_update(set2)
print(set1)

# symmetric_difference() - items not in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

# ^ operator - same as symmetric_difference()
set3 = set1 ^ set2
print(set3)

# symmetric_difference_update() - changes original set
set1.symmetric_difference_update(set2)
print(set1)


# =====================================================
# FROZENSET
# =====================================================
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

# Frozenset supports non-mutating set operations
print(x.union({"mango"}))
print(x.intersection({"banana", "cherry"}))
print(x.isdisjoint({"apple", "mango"}))
print(x.issubset({"apple", "banana", "cherry", "mango"}))
print(x.issuperset({"banana"}))


# =====================================================
# PRACTICE QUESTIONS
# =====================================================
# Q1. Create a set with 5 fruits and print it
# Q2. Add "kiwi" to the set
# Q3. Remove "apple" from the set using discard()
# Q4. Remove a random item using pop()
# Q5. Join two sets using union()
# Q6. Update a set with a list of new fruits
# Q7. Find intersection of two sets
# Q8. Find difference of two sets
# Q9. Find symmetric_difference of two sets
# Q10. Create a frozenset and check union with another set

# =====================================================
# HINTS / ANSWERS
# =====================================================
# A1. myset = {"apple","banana","cherry","mango","orange"}
# A2. myset.add("kiwi")
# A3. myset.discard("apple")
# A4. myset.pop()
# A5. set1.union(set2)
# A6. myset.update(["kiwi","grape"])
# A7. set1.intersection(set2)
# A8. set1.difference(set2)
# A9. set1.symmetric_difference(set2)
# A10. fs = frozenset({"apple","banana"}); fs.union({"kiwi"})
