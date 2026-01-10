# =====================================================
# PYTHON FUNCTIONS AND ADVANCED TOPICS
# =====================================================

# -----------------------------------------------------
# FUNCTIONS BASICS
# -----------------------------------------------------
# A function is a block of code executed when called
def my_function():
    print("Hello from a function")

# Calling a function
my_function()
my_function()
my_function()

# Function with arguments
def greet(name):
    print("Hello", name)

greet("Emil")  # Argument

# Default parameter
def greet(name="friend"):
    print("Hello", name)

greet()
greet("Tobias")

# Function returning values
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

# -----------------------------------------------------
# *args AND **kwargs
# -----------------------------------------------------
# Accept any number of positional arguments
def print_kids(*kids):
    print("Kids:", kids)

print_kids("Emil", "Tobias", "Linus")

# Accept any number of keyword arguments
def print_person(**person):
    print("Person:", person)

print_person(name="Emil", age=25, city="Oslo")

# Combining *args and **kwargs
def func(title, *args, **kwargs):
    print("Title:", title)
    print("Args:", args)
    print("Kwargs:", kwargs)

func("Info", 1, 2, 3, name="Emil", age=25)

# -----------------------------------------------------
# SCOPE
# -----------------------------------------------------
# Local scope
def local_func():
    x = 300
    print("Local x:", x)

local_func()

# Global scope
x = 500
def global_func():
    print("Global x:", x)

global_func()

# Changing global variable
def change_global():
    global x
    x = 1000

change_global()
print("Modified global x:", x)

# Nonlocal keyword (nested functions)
def outer_func():
    x = "outer"
    def inner_func():
        nonlocal x
        x = "inner"
    inner_func()
    print("Nonlocal x:", x)

outer_func()

# -----------------------------------------------------
# DECORATORS
# -----------------------------------------------------
import functools

# Basic decorator
def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase
def say_hello(name):
    return f"Hello {name}"

print(say_hello("John"))

# Multiple decorators
def add_greeting(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return "Hello! " + func(*args, **kwargs)
    return wrapper

@uppercase
@add_greeting
def greet_person(name):
    return name

print(greet_person("Alice"))

# -----------------------------------------------------
# LAMBDA FUNCTIONS
# -----------------------------------------------------
# Anonymous function
double = lambda x: x * 2
print(double(5))

# Multiple arguments
add_three = lambda a, b, c: a + b + c
print(add_three(5, 6, 2))

# Lambda with map/filter/sorted
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x*2, numbers))
print("Doubled:", doubled)

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd numbers:", odd_numbers)

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print("Sorted by age:", sorted_students)

# Lambda closure
def multiplier(n):
    return lambda x: x * n

doubler = multiplier(2)
tripler = multiplier(3)
print(doubler(11))
print(tripler(11))

# -----------------------------------------------------
# RECURSION
# -----------------------------------------------------
# Factorial using recursion
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print("Factorial 5:", factorial(5))

# Fibonacci using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("7th Fibonacci:", fibonacci(7))

# Sum of list using recursion
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

my_list = [1,2,3,4,5]
print("Sum of list:", sum_list(my_list))

# Max of list using recursion
def max_list(lst):
    if len(lst) == 1:
        return lst[0]
    rest_max = max_list(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max

print("Max of list:", max_list([3,7,2,9,1]))

# -----------------------------------------------------
# GENERATORS
# -----------------------------------------------------
# Basic generator
def my_generator():
    yield 1
    yield 2
    yield 3

for val in my_generator():
    print("Generator value:", val)

# Fibonacci generator
def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

gen = fibonacci_gen()
for _ in range(10):
    print("Fibo:", next(gen))

# Generator expression
gen_exp = (x*x for x in range(5))
print("Generator expression:", list(gen_exp))

# next() and StopIteration
def simple_gen():
    yield "Emil"
    yield "Tobias"

gen = simple_gen()
print(next(gen))
print(next(gen))
# print(next(gen))  # Uncommenting raises StopIteration

# Generator send()
def echo_gen():
    while True:
        received = yield
        print("Received:", received)

g = echo_gen()
next(g)  # prime generator
g.send("Hello")
g.send("World")
