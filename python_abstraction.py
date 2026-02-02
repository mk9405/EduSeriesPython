"""
----------------------------------------------------------------------
ABSTRACTION (ENFORCING RULES)
----------------------------------------------------------------------

Definition:
Abstraction means hiding implementation details and showing only
essential features to the user.

In Python, abstraction is achieved using:
- abc module
- ABC (Abstract Base Class)
- @abstractmethod decorator

Key Rules:
1. Abstract class cannot be instantiated.
2. Child classes MUST implement all abstract methods.
3. Abstract class acts like a blueprint or contract.

Real-life analogy:
ATM machine – you know what it does, not how it works.
"""

# Importing Abstract Base Class tools
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract Class: Shape

    Purpose:
    This class defines a RULE that every shape must have
    a method called calculate_area().

    Note:
    This class cannot be used to create objects directly.
    """

    @abstractmethod  # decorator
    def calculate_area(self):
        """
        Abstract Method

        This method has no body.
        Any class inheriting Shape MUST define this method.
        """
        pass


class Square(Shape):
    """
    Concrete Class: Square

    Inherits from Shape abstract class
    Implements calculate_area() method
    """

    def __init__(self, side):
        """
        Constructor

        Parameters:
        side (int or float): length of one side of square
        """
        self.side = side

    def calculate_area(self):
        """
        Calculates area of square

        Formula:
        area = side * side
        """
        return self.side * self.side


class Circle(Shape):
    """
    Concrete Class: Circle

    Implements calculate_area() differently
    """

    def __init__(self, radius):
        """
        Constructor

        Parameters:
        radius (int or float): radius of the circle
        """
        self.radius = radius

    def calculate_area(self):
        """
        Calculates area of circle

        Formula:
        area = π * r * r
        """
        return 3.14 * self.radius * self.radius


# Creating object of child class (Allowed)
sq = Square(4)
print("Square Area:", sq.calculate_area())


"""
Common Abstraction Mistakes:
1. Trying to create object of abstract class
2. Forgetting to implement abstract methods
3. Missing @abstractmethod decorator
"""
from abc import ABC, abstractmethod


class Employee(ABC):
    """
    Abstract Class: Employee
    """

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


emp1 = FullTimeEmployee(5000)
emp2 = PartTimeEmployee(20, 80)

print(emp1.calculate_salary())
print(emp2.calculate_salary())

from abc import ABC, abstractmethod


class Demo(ABC):

    # 1️⃣ Abstract Method
    @abstractmethod
    def calculate(self):
        pass

    # 2️⃣ Normal (Concrete) Method
    def show(self):
        print("This is a normal method")

    # 3️⃣ Instance Method
    def set_value(self, value):
        self.value = value

    # 4️⃣ Class Method
    @classmethod
    def class_info(cls):
        print("This is a class method")

    # 5️⃣ Static Method
    @staticmethod
    def add(a, b):
        return a + b

    # 6️⃣ Abstract + Class Method
    @classmethod
    @abstractmethod
    def create(cls):
        pass

    # 7️⃣ Abstract + Static Method
    @staticmethod
    @abstractmethod
    def validate(data):
        pass

    # 8️⃣ Protected Method
    def _protected_method(self):
        print("Protected method")

    # 9️⃣ Private Method
    def __private_method(self):
        print("Private method")

    # 🔟 Magic / Dunder Method
    def __str__(self):
        return "Demo class object"
    
"""

This file contains 10 different method type examples in Python:
1. Abstract Method
2. Normal Method
3. Instance Method
4. Class Method
5. Static Method
6. Abstract + Class Method
7. Abstract + Static Method
8. Protected Method
9. Private Method
10. Magic / Dunder Method
"""

# ------------------------------
# 1️⃣ Abstract Method
# ------------------------------
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side

sq = Square(5)
print("1️⃣ Abstract Method Example:", sq.calculate_area())


# ------------------------------
# 2️⃣ Normal Method
# ------------------------------
class DemoNormal:
    def greet(self):
        print("2️⃣ Normal Method Example: Hello! I am a normal method")

obj_normal = DemoNormal()
obj_normal.greet()


# ------------------------------
# 3️⃣ Instance Method
# ------------------------------
class Person:
    def set_name(self, name):
        self.name = name

    def show_name(self):
        print(f"3️⃣ Instance Method Example: My name is {self.name}")

p = Person()
p.set_name("Alice")
p.show_name()


# ------------------------------
# 4️⃣ Class Method
# ------------------------------
class DemoClass:
    count = 10

    @classmethod
    def show_count(cls):
        print(f"4️⃣ Class Method Example: Count = {cls.count}")

DemoClass.show_count()


# ------------------------------
# 5️⃣ Static Method
# ------------------------------
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print("5️⃣ Static Method Example:", Math.add(5, 3))


# ------------------------------
# 6️⃣ Abstract + Class Method
# ------------------------------
class Machine(ABC):
    @classmethod
    @abstractmethod
    def create(cls):
        pass

class Car(Machine):
    @classmethod
    def create(cls):
        return cls()

c = Car.create()
print("6️⃣ Abstract + Class Method Example:", type(c))


# ------------------------------
# 7️⃣ Abstract + Static Method
# ------------------------------
class Validator(ABC):
    @staticmethod
    @abstractmethod
    def validate(data):
        pass

class MyValidator(Validator):
    @staticmethod
    def validate(data):
        return data is not None

print("7️⃣ Abstract + Static Method Example:", MyValidator.validate("Hello"))


# ------------------------------
# 8️⃣ Protected Method
# ------------------------------
class DemoProtected:
    def _protected(self):
        print("8️⃣ Protected Method Example: This is a protected method")

obj_prot = DemoProtected()
obj_prot._protected()


# ------------------------------
# 9️⃣ Private Method
# ------------------------------
class DemoPrivate:
    def __private(self):
        print("9️⃣ Private Method Example: This is a private method")

obj_priv = DemoPrivate()
obj_priv._DemoPrivate__private()  # Access via name mangling


# ------------------------------
# 🔟 Magic / Dunder Method
# ------------------------------
class DemoMagic:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"🔟 Magic Method Example: Demo object: {self.name}"

obj_magic = DemoMagic("Alice")
print(obj_magic)


# =====================================================================

