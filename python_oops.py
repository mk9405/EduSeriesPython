"""
Python Object-Oriented Programming (OOP)
========================================

This file covers:
- Classes & Objects
- __init__() method
- self parameter
- Class properties & methods
- Inheritance
- Polymorphism
- Encapsulation
- Inner classes
"""

# =========================
# 1. Classes and Objects
# =========================
# Classes are blueprints for creating objects. Objects are instances of classes.

# Example: Create a class with a property
class MyClass:
    x = 5

# Create objects from the class
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print("Object properties:")
print(p1.x)
print(p2.x)
print(p3.x)

# Delete an object
del p1
# print(p1.x) # This will cause an error

# Empty class with pass
class Person:
    pass

# =========================
# 2. The __init__() Method
# =========================
# __init__() is called automatically when an object is created
class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(f"{p1.name} is {p1.age} years old")
print(f"{p2.name} is {p2.age} years old")

# Multiple parameters
class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")
print(p1.name, p1.age, p1.city, p1.country)

# =========================
# 3. self Parameter
# =========================
# self refers to the instance of the class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()

# Access multiple properties
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

# Call one method from another
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, " + self.name

    def welcome(self):
        message = self.greet()
        print(message + "! Welcome!")

p1 = Person("Tobias")
p1.welcome()

# =========================
# 4. Class Properties
# =========================
# Instance vs Class properties
class Person:
    species = "Human"  # Class property

    def __init__(self, name):
        self.name = name  # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")
print(p1.name, p1.species)
print(p2.name, p2.species)

# Modify class property
Person.species = "Homo sapiens"
print(p1.species)
print(p2.species)

# Add new property to object
p1.age = 25
p1.city = "Oslo"
print(p1.name, p1.age, p1.city)

# =========================
# 5. Class Methods
# =========================
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old"

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()

# __str__ method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)

# Playlist example with multiple methods
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed: {song}")

    def show_songs(self):
        print(f"Playlist '{self.name}':")
        for song in self.songs:
            print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()

# =========================
# 6. Inheritance
# =========================
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

# Child class
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

student = Student("Mike", "Olsen", 2019)
student.welcome()

# =========================
# 7. Polymorphism
# =========================
# Same method name, different classes
class Car:
    def move(self):
        print("Drive!")

class Boat:
    def move(self):
        print("Sail!")

class Plane:
    def move(self):
        print("Fly!")

for vehicle in (Car(), Boat(), Plane()):
    vehicle.move()

# =========================
# 8. Encapsulation
# =========================
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

p1 = Person("Tobias", 25)
print(p1.get_age())
p1.set_age(26)
print(p1.get_age())

# =========================
# 9. Inner Classes
# =========================
class Outer:
    def __init__(self):
        self.name = "Outer"

    class Inner:
        def __init__(self, outer):
            self.outer = outer

        def display(self):
            print(f"Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()

# Car engine example
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()

    class Engine:
        def __init__(self):
            self.status = "Off"

        def start(self):
            self.status = "Running"
            print("Engine started")

        def stop(self):
            self.status = "Off"
            print("Engine stopped")

    def drive(self):
        if self.engine.status == "Running":
            print(f"Driving the {self.brand} {self.model}")
        else:
            print("Start the engine first!")

car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive()
