# =====================================================
# PYTHON LISTS – COMPLETE NOTES + EXECUTABLE CODE
# =====================================================

# Lists are used to store multiple items in a single variable
# Lists are ordered, changeable, and allow duplicates

# =====================================================
# CREATE A LIST
# =====================================================
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Lists can have duplicate items
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# List length
print(len(thislist))

# List items can be of any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(list1, list2, list3, list4)

# Check type
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# Using list() constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)

# =====================================================
# ACCESS LIST ITEMS
# =====================================================
thislist = ["apple", "banana", "cherry"]
print(thislist[1])    # Access second item
print(thislist[-1])   # Access last item

# Range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  # Index 2 to 4
print(thislist[:4])    # Start to index 3
print(thislist[2:])    # Index 2 to end
print(thislist[-4:-1]) # Negative indexing

# Check if item exists
if "apple" in thislist:
    print("Yes, 'apple' is in the list")


# =====================================================
# CHANGE LIST ITEMS
# =====================================================
# Change single item
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change range of items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Replace one with two items
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Replace two with one item
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Insert items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


# =====================================================
# ADD LIST ITEMS
# =====================================================
# Append
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert at specific index
thislist.insert(1, "orange")
print(thislist)

# Extend with another list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Extend with tuple
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


# =====================================================
# REMOVE LIST ITEMS
# =====================================================
# Remove by value
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove first occurrence
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Remove by index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Remove last item
thislist.pop()
print(thislist)

# Delete index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Delete entire list
thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist) # This will give an error

# Clear list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# =====================================================
# LOOP THROUGH LISTS
# =====================================================
thislist = ["apple", "banana", "cherry"]

# For loop
for x in thislist:
    print(x)

# Loop by index
for i in range(len(thislist)):
    print(thislist[i])

# While loop
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

# List comprehension
[print(x) for x in thislist]


# =====================================================
# LIST COMPREHENSION
# =====================================================
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# Filter example
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Exclude "apple"
newlist = [x for x in fruits if x != "apple"]
print(newlist)

# No condition
newlist = [x for x in fruits]
print(newlist)

# Using range
newlist = [x for x in range(10)]
print(newlist)

# Condition example
newlist = [x for x in range(10) if x < 5]
print(newlist)

# Expression example
newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


# =====================================================
# SORT LISTS
# =====================================================
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() # Ascending
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Descending
thislist.sort(reverse=True)
print(thislist)

# Custom sort
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# Case-insensitive sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

# Reverse order
thislist.reverse()
print(thislist)


# =====================================================
# COPY LISTS
# =====================================================
thislist = ["apple", "banana", "cherry"]

# copy() method
mylist = thislist.copy()
print(mylist)

# list() method
mylist = list(thislist)
print(mylist)

# slice operator
mylist = thislist[:]
print(mylist)


# =====================================================
# JOIN LISTS
# =====================================================
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# Using +
list3 = list1 + list2
print(list3)

# Using loop
for x in list2:
    list1.append(x)
print(list1)

# Using extend()
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)


# =====================================================
# LIST METHODS SUMMARY
# =====================================================
# append() - add element at end
# clear() - remove all elements
# copy() - copy list
# count() - count element occurrences
# extend() - add elements from iterable
# index() - get index of element
# insert() - add element at position
# pop() - remove element at position
# remove() - remove element by value
# reverse() - reverse list
# sort() - sort list


# =====================================================
# PRACTICE QUESTIONS
# =====================================================
# Q1. Print the first and last item of a list
# Q2. Replace the second item with "pear"
# Q3. Append "grape" to the list
# Q4. Remove "banana" from the list
# Q5. Print all items using a for loop
# Q6. Create a new list using list comprehension with only fruits containing "i"
# Q7. Sort the list alphabetically
# Q8. Copy a list using slice operator
# Q9. Join two lists using extend()
# Q10. Reverse the list


# =====================================================
# ANSWERS
# =====================================================
# A1. print(mylist[0], mylist[-1])
# A2. mylist[1] = "pear"
# A3. mylist.append("grape")
# A4. mylist.remove("banana")
# A5. for x in mylist: print(x)
# A6. newlist = [x for x in mylist if "i" in x]
# A7. mylist.sort()
# A8. newlist = mylist[:]
# A9. mylist.extend(anotherlist)
# A10. mylist.reverse()
