"""
=========================================================
INHERITANCE IN PYTHON
Complete Notes with Types, Definitions & Examples
=========================================================

Inheritance allows one class (child) to acquire the
properties and methods of another class (parent).

Parent class  -> Base class
Child class   -> Derived class
"""

# =========================================================
# WHY INHERITANCE?
# =========================================================
# 1. Code Reusability
# 2. Better structure
# 3. Easy maintenance
# 4. Real-world relationship modeling


# =========================================================
# 1. SINGLE INHERITANCE
# =========================================================
# One child class inherits from one parent class


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):
    def bark(self):
        print(self.name, "is barking")


print("\n--- Single Inheritance Example ---")
d = Dog("Bruno")
d.eat()
d.bark()


# SECOND EXAMPLE 

class Student(Person):
    def __init__(self, name, phone, roll_no, grade):
        super().__init__(name, phone)
        self.roll_no = roll_no
        self.grade = grade
        self.subjects = []
        self.marks = {}

        # Encapsulation
        self.__fees_paid = 0
        self.__total_fees = 50000

    def add_subject(self, subject):
        self.subjects.append(subject)

    def set_marks(self, subject, marks):
        if subject in self.subjects:
            self.marks[subject] = marks
        else:
            print(f"{subject} not enrolled")

    def pay_fees(self, amount):
        self.__fees_paid += amount

    def student_profile(self):
        print("\n--- Student Profile ---")
        self.show_basic_info()
        print(f"Roll No: {self.roll_no}")
        print(f"Grade: {self.grade}")
        print(f"Subjects: {self.subjects}")
        print(f"Marks: {self.marks}")
        print(
            "Fees Status:",
            "Cleared" if self.__fees_paid >= self.__total_fees else "Pending"
        )


print("\n===== SINGLE INHERITANCE =====")
s1 = Student("Aryan Sharma", "98765-43210", 101, "12th")
s1.add_subject("Physics")
s1.add_subject()
s1.set_marks("Physics", 88)
s1.pay_fees(30000)
s1.student_profile()

sub = input("Enter ")

# =========================================================
# 2. MULTILEVEL INHERITANCE
# Person -> Student -> Monitor
# =========================================================
class Monitor(Student):
    def __init__(self, name, phone, roll_no, grade, responsibility):
        super().__init__(name, phone, roll_no, grade)
        self.responsibility = responsibility

    def monitor_duties(self):
        print(f"{self.name} handles: {self.responsibility}")


print("\n===== MULTILEVEL INHERITANCE =====")
m1 = Monitor("Rohit Verma", "99999-88888", 102, "12th", "Discipline")
m1.add_subject("Chemistry")
m1.monitor_duties()
m1.student_profile()


# EXAMPLE 2

class Sports:
    def __init__(self):
        self.sports_list = []

    def add_sport(self, sport):
        self.sports_list.append(sport)


class SportsStudent(Student, Sports):
    def __init__(self, name, phone, roll_no, grade):
        Student.__init__(self, name, phone, roll_no, grade)
        Sports.__init__(self)

    def sports_profile(self):
        print(f"Sports: {self.sports_list}")


print("\n===== MULTIPLE INHERITANCE =====")
ss1 = SportsStudent("Neha Singh", "88888-77777", 103, "11th")
ss1.add_subject("Biology")
ss1.add_sport("Basketball")
ss1.add_sport("Badminton")
ss1.student_profile()
ss1.sports_profile()

# =========================================================
# 2. MULTIPLE INHERITANCE
# =========================================================
# One child class inherits from multiple parent classes


class Father:
    def skills(self):
        print("Father skills: Driving, Business")


class Mother:
    def skills(self):
        print("Mother skills: Cooking, Teaching")


class Child(Father, Mother, Mother):
    def own_skills(self):
        print("Child skills: Coding")


print("\n--- Multiple Inheritance Example ---")
c = Child()
c.skills()        # Follows MRO (Father first)
c.own_skills()


# =========================================================
# 3. MULTILEVEL INHERITANCE
# =========================================================
# Inheritance in chain form


class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")


print("\n--- Multilevel Inheritance Example ---")
e = ElectricCar()
e.start()
e.drive()
e.charge()


# =========================================================
# 4. HIERARCHICAL INHERITANCE
# =========================================================
# Multiple child classes inherit from one parent class


class Shape:
    def area(self):
        print("Calculating area")


class Circle(Shape):
    def draw(self):
        print("Drawing circle")


class Square(Shape):
    def draw(self):
        print("Drawing square")


print("\n--- Hierarchical Inheritance Example ---")
circle = Circle()
square = Square()

circle.area()
circle.draw()

square.area()
square.draw()

#EXAMPLE 2

class Teacher(Person):
    def __init__(self, name, phone, subject):
        super().__init__(name, phone)
        self.subject = subject

    def teacher_profile(self):
        print("\n--- Teacher Profile ---")
        self.show_basic_info()
        print(f"Teaches: {self.subject}")


print("\n===== HIERARCHICAL INHERITANCE =====")
t1 = Teacher("Mr. Rajesh Kumar", "77777-66666", "Physics")
t1.teacher_profile()

# =========================================================
# 5. HYBRID INHERITANCE
# =========================================================
# Combination of more than one inheritance type


class A:
    def showA(self):
        print("Class A")


class B(A):
    def showB(self):
        print("Class B")


class C(A):
    def showC(self):
        print("Class C")


class D(B, C):
    def showD(self):
        print("Class D")


print("\n--- Hybrid Inheritance Example ---")
obj = D()
obj.showA()
obj.showB()
obj.showC()
obj.showD()

# EXAMPLE 2

class Captain(SportsStudent):
    def __init__(self, name, phone, roll_no, grade, team):
        super().__init__(name, phone, roll_no, grade)
        self.team = team

    def captain_profile(self):
        print("\n--- Captain Profile ---")
        self.student_profile()
        print(f"Team Captain of: {self.team}")
        print(f"Sports: {self.sports_list}")


print("\n===== HYBRID INHERITANCE =====")
c1 = Captain("Aditya Mehra", "66666-55555", 104, "12th", "Cricket")
c1.add_subject("Maths")
c1.add_sport("Cricket")
c1.pay_fees(50000)
c1.captain_profile()



# =========================================================
# SUPER() KEYWORD EXAMPLE
# =========================================================
# Used to call parent class constructor or methods


class Parent:
    def __init__(self):
        print("Parent constructor called")


class ChildWithSuper(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor called")


print("\n--- super() Example ---")
cs = ChildWithSuper()


# EXAMPLE 2

"""
=========================================================
SUPER() KEYWORD – REAL WORLD PYTHON EXAMPLE
Student Management System
=========================================================

This file explains how super() works step-by-step
using a real-world Student example.
"""

# =========================================================
# PARENT CLASS
# =========================================================
class Person:
    organization = "Global International School"

    def __init__(self, name, phone):
        print("Person __init__ started")

        self.name = name
        self.phone = phone

        print("Person __init__ completed")

    def display_basic_info(self):
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Organization: {Person.organization}")


# =========================================================
# CHILD CLASS (USES super())
# =========================================================
class Student(Person):
    def __init__(self, name, phone, roll_no, grade):
        print("Student __init__ started")

        # Calling Parent constructor using super()
        super().__init__(name, phone)

        # Student specific data
        self.roll_no = roll_no
        self.grade = grade
        self.subjects = []

        print("Student __init__ completed")

    def add_subject(self, subject):
        self.subjects.append(subject)

    def display_profile(self):
        print("\n--- Student Profile ---")
        self.display_basic_info()
        print(f"Roll No: {self.roll_no}")
        print(f"Grade: {self.grade}")
        print(f"Subjects: {', '.join(self.subjects)}")


# =========================================================
# PROGRAM EXECUTION
# =========================================================
print("\n===== super() KEYWORD EXAMPLE =====")

s1 = Student(
    name="Aryan Sharma",
    phone="98765-43210",
    roll_no=101,
    grade="12th"
)

s1.add_subject("Physics")
s1.add_subject("Maths")
s1.display_profile()



# =========================================================
# SUMMARY
# =========================================================
# - Inheritance helps in code reuse
# - Child class can access parent class members
# - Python supports 5 types of inheritance
# - Method Resolution Order (MRO) decides execution order
