"""
====================================================================
PYTHON OBJECT-ORIENTED PROGRAMMING (OOP) – DEEP & DETAILED EXPLANATION
====================================================================

WHAT IS OOP?
------------
Object-Oriented Programming (OOP) is a programming paradigm that
organizes code using "objects" and "classes", similar to real-world
entities.

OOP means writing programs using real-world things.

Real world example:
-------------------
Car
 - Properties: color, brand
 - Actions: drive(), stop()

In Python:
----------
Properties → variables
Actions    → methods

WHY OOP?
--------
✔ Models real-world problems easily
✔ Code reusability
✔ Better structure and maintenance
✔ Used in real frameworks (Django, Flask, FastAPI)

OOP HAS 4 MAIN PILLARS:
----------------------
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction (conceptual – not directly shown here)

This file covers concepts step-by-step with executable examples.
"""

print("=" * 70)
print("PYTHON OOP – DETAILED WALKTHROUGH")
print("=" * 70)


# ====================================================================
# 1. CLASSES AND OBJECTS
# ====================================================================
"""
CLASS:
------
A class is a blueprint or template that defines:
- Properties (variables)
- Behavior (methods)

OBJECT:
-------
An object is a real instance created from a class.

REAL-LIFE EXAMPLE:
------------------
Class   → Car
Object  → Toyota, Honda, BMW
"""

class Car:
    brand = "Generic"   # class variable

# Creating objects (instances)
car1 = Car()
car2 = Car()

print("\n1. Classes & Objects")
print("car1 brand:", car1.brand)
print("car2 brand:", car2.brand)


# -------- Example 1 --------
class Mobile:
    model = "Unknown"

m1 = Mobile()
m2 = Mobile()
print("\n1.2 Multiple Objects")
print(m1.model, m2.model)

# -------- Example 2 --------
class Fan:
    speed = 3

f = Fan()
print("\n1.3 Default Property")
print(f.speed)



# ====================================================================
# 2. __init__() METHOD (CONSTRUCTOR)
# ====================================================================
"""
__init__():
-----------
- Automatically called when object is created
- Used to initialize object data
- Each object can have different values

SYNTAX:
-------
def __init__(self, parameters):
"""

class Person:
    def __init__(self, name, age):
        self.name = name   # instance variable
        self.age = age

p1 = Person("Emil", 25)
p2 = Person("Tobias", 30)

print("\n2. Constructor (__init__)")
print(p1.name, p1.age)
print(p2.name, p2.age)

# -------- Example 1 --------
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Amit", 22)
print("\n2.2 Multiple values")
print(s.name, s.age)

# example 2

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

s1 = Student("Manish", 22, "Python")
print("\nExample 2:")
print(s1.name, s1.age, s1.course)

# example 3

class Employee:
    def __init__(self, name, salary=20000):
        self.name = name
        self.salary = salary

e1 = Employee("Amit")
e2 = Employee("Rohit", 30000)

print("\nExample 3:")
print(e1.name, e1.salary)
print(e2.name, e2.salary)

# EXAMPLE 4: CALCULATION INSIDE __init__()
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = length * width   # calculated value

r = Rectangle(10, 5)

print("\nExample 4:")
print("Length:", r.length)
print("Width:", r.width)
print("Area:", r.area)

# EXAMPLE 5: __init__() CALLING ANOTHER METHOD

class Greeting:
    def __init__(self, name):
        self.name = name
        self.say_hello()

    def say_hello(self):
        print("Hello", self.name)

print("\nExample 5:")
g = Greeting("Alex")

# ====================================================================
# 3. self KEYWORD (MOST IMPORTANT)
# ====================================================================
"""
self:
-----
- Refers to the current object
- Used to access object variables & methods
- Without self, Python cannot link variables to objects
"""

class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)

s1 = Student("Alex")
s1.greet()


# ====================================================================
# 4. INSTANCE VARIABLES vs CLASS VARIABLES
# ====================================================================
"""
INSTANCE VARIABLE:
------------------
- Belongs to object
- Different for each object

CLASS VARIABLE:
---------------
- Belongs to class
- Shared by all objects
"""

class Employee:
    company = "Google"   # class variable

    def __init__(self, name):
        self.name = name # instance variable

e1 = Employee("Amit")
e2 = Employee("Rohit")

print("\n4. Instance vs Class Variables")
print(e1.name, e1.company)
print(e2.name, e2.company)

# Changing class variable
Employee.company = "Microsoft"
print(e1.company)
print(e2.company)


# ====================================================================
# 5. METHODS IN CLASS
# ====================================================================
"""
METHOD:
-------
A function defined inside a class.
Used to perform actions using object data.
"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.balance)

account = BankAccount("Manish", 1000)
account.deposit(500)
account.withdraw(300)
account.show_balance()


# ====================================================================
# 6. __str__() METHOD
# ====================================================================
"""
__str__():
----------
- Controls how object is printed
- Makes output human-readable
"""

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"Book: {self.title}, Price: ₹{self.price}"

b1 = Book("Python Basics", 399)
print("\n6. __str__ Method")
print(b1)


# ====================================================================
# 7. INHERITANCE
# ====================================================================
"""
INHERITANCE:
------------
- One class acquires properties of another class
- Parent → Child

BENEFITS:
---------
✔ Code reuse
✔ Less duplication
"""

class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def show_details(self):
        print(self.name, "teaches", self.subject)

t = Teacher("Ravi", "Math")
print("\n7. Inheritance")
t.show_name()
t.show_details()


# ====================================================================
# 8. POLYMORPHISM
# ====================================================================
"""
POLYMORPHISM:
-------------
Same method name, different behavior.

REAL-LIFE:
----------
Same button → different actions in different apps
"""

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

class Cow:
    def sound(self):
        print("Moo")

print("\n8. Polymorphism")
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.sound()


# ====================================================================
# 9. ENCAPSULATION (DATA HIDING)
# ====================================================================
"""
ENCAPSULATION:
--------------
- Restrict direct access to variables
- Protect data from misuse
- Use double underscore (__)

PRIVATE VARIABLE:
-----------------
self.__variable
"""

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self, pwd):
        return pwd == self.__password

u = User("admin", "12345")
print("\n9. Encapsulation")
print(u.check_password("12345"))
# print(u.__password)  # ERROR


# ====================================================================
# 10. INNER CLASSES
# ====================================================================
"""
INNER CLASS:
------------
- A class inside another class
- Used when classes are tightly connected
"""

class Computer:
    def __init__(self):
        self.cpu = self.CPU()

    def start(self):
        self.cpu.execute()

    class CPU:
        def execute(self):
            print("CPU executing instructions")

print("\n10. Inner Class")
pc = Computer()
pc.start()


# ====================================================================
# FINAL SUMMARY
# ====================================================================
"""
KEY TAKEAWAYS:
--------------
✔ Class = Blueprint
✔ Object = Instance
✔ self = current object
✔ __init__ = constructor
✔ Inheritance = reuse
✔ Polymorphism = flexibility
✔ Encapsulation = security
✔ Inner class = strong relationship
"""

print("\nEND OF PYTHON OOP – DETAILED EXPLANATION")
print("=" * 70)
