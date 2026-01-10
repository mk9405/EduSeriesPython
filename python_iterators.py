# =====================================================
# PYTHON ITERATORS
# =====================================================
# An iterator is an object that can be iterated upon (traversed),
# meaning you can move through all its values one by one.

# =====================================================
# ITERABLE VS ITERATOR
# =====================================================
# Iterable objects: Lists, Tuples, Dictionaries, Sets, Strings
# They have an __iter__() method that returns an iterator.

# Example: iterator from a tuple
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)  # get iterator

print(next(myit))  # apple
print(next(myit))  # banana
print(next(myit))  # cherry

# Example: iterator from a string
mystr = "banana"
myit = iter(mystr)

print(next(myit))  # b
print(next(myit))  # a
print(next(myit))  # n
print(next(myit))  # a
print(next(myit))  # n
print(next(myit))  # a

# =====================================================
# LOOPING THROUGH ITERABLES
# =====================================================
# The for loop automatically creates an iterator and uses next()

# Loop through tuple
for x in mytuple:
    print(x)

# Loop through string
for ch in mystr:
    print(ch)

# =====================================================
# CREATING CUSTOM ITERATORS
# =====================================================
# A class becomes an iterator by implementing __iter__() and __next__()

class MyNumbers:
    def __iter__(self):
        self.a = 1  # initialize starting number
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

# Using the custom iterator
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))  # 1
print(next(myiter))  # 2
print(next(myiter))  # 3
print(next(myiter))  # 4
print(next(myiter))  # 5

# =====================================================
# USING StopIteration
# =====================================================
# StopIteration prevents infinite loops by defining a termination condition

class MyNumbersLimited:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:  # stop after 20 iterations
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration  # stop iteration

# Using custom iterator with stop condition
myclass = MyNumbersLimited()
myiter = iter(myclass)

for x in myiter:
    print(x)

# =====================================================
# NOTES:
# 1. Iterables can be converted into iterators using iter()
# 2. Iterators keep track of their current state and use next() to return items
# 3. Custom iterators require __iter__() to return self and __next__() to return the next value
# 4. StopIteration is used to end iteration gracefully
