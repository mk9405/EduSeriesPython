'''
===================================================================
Topic 1: The Foundation – Classes and Objects
===================================================================

Simple Explanation:- 
    In the real world, everything is an object. A Class is just a "Map" or "Blueprint" (Naksha). An Object is the "Actual Thing" built using that map. Example: "Car" is a concept (Class), but your "Red Maruti Swift" is a real object
'''

#syntax:
class ClassName:
    # class variables and methods

# Example: Creating a BankAccount Blueprint
class BankAccount:
    bank_name = "Global Trust Bank"  # Class Attribute (Same for everyone)

# Example 2: Creating real account objects
account_1 = BankAccount()
account_2 = BankAccount()

print(f"Account 1 belongs to: {account_1.bank_name}")
print(f"Account 2 belongs to: {account_2.bank_name}")

'''
#Common Mistakes:

    - Case Sensitivity: Beginners often name classes in lowercase. Use PascalCase (e.g., MyClass) so it’s easy to distinguish from variables.

    - Empty Classes: You cannot leave a class empty. Use the pass keyword if you aren't adding code yet
'''



'''
===================================================================
Topic 2: The __init__ Method and self (Constructor)
===================================================================

Explanation: 
    __init__ is a special method that runs automatically the moment you create an object. Think of it as a "setup" function. self is a pointer to the current object. Without self, Python won't know which object's data you are trying to change.

'''

#Syntax
def __init__(self, parameter1, parameter2):
    self.attribute = parameter1

# Example: Initializing unique data for each object
class Student:
    def __init__(self, name, roll_no):
        self.name = name       # Assigning name to the specific object
        self.roll_no = roll_no # Assigning roll no

# Multiple objects with different data
s1 = Student("Rahul", 101)
s2 = Student("Priya", 102)

print(f"Student 1: {s1.name}, Roll: {s1.roll_no}")
print(f"Student 2: {s2.name}, Roll: {s2.roll_no}")

'''
Common Mistakes:
    - Forgetting self: If you write def __init__(name):, Python will throw an error because the first argument must be self.

    - Misspelling: People often write _init_ (single underscore). It must be __init__ (double underscore on both sides).
'''


'''
===================================================================
Topic 3: Instance vs Class Variables
===================================================================
Explanation:
    Instance Variable: Data that belongs to a specific object (e.g., different names for different students).

    Class Variable: Data that is shared by every single object of that class (e.g., the School Name for all students).
'''
# Syntax
class MyClass:
    class_var = "Shared"       # Class variable
    def __init__(self, val):
        self.inst_var = val    # Instance variable

# Example: Global vs Specific data
class Employee:
    company = "Google"  # Shared by all employees

    def __init__(self, name):
        self.name = name  # Unique for each employee

# Changing Class Variables
e1 = Employee("Amit")
e2 = Employee("Suresh")

Employee.company = "Meta" # Changes for everyone
print(f"{e1.name} works at {e1.company}")
print(f"{e2.name} works at {e2.company}")


'''
Mistakes:
    Accidental Overriding: If you change e1.company = "Apple", it only changes for e1. To change it for everyone, use Employee.company
'''



'''
===================================================================
Topic 4: Inheritance (Single & Multilevel)
===================================================================
Explanation: 
    Inheritance allows one class to get properties from another class.
    Parent Class (Base): The one giving the features.
    Child Class (Derived): The one taking the features.
    super(): A function used to call the parent's methods inside the child class.
'''

#Syntax
class Child(Parent):
    # logic

# Example: Basic Inheritance
class Phone:
    def make_call(self):
        print("Calling...")

class SmartPhone(Phone): # Inheriting Phone
    def browse(self):
        print("Browsing Internet")


# Example 2: Multilevel (Grandparent -> Parent -> Child)
class Android(SmartPhone):
    def play_store(self):
        print("Opening PlayStore")

my_phone = Android()
my_phone.make_call() # From Phone
my_phone.browse()    # From SmartPhone
my_phone.play_store()# From Android

'''
Common Mistakes:

    - Circular Inheritance: Class A inheriting from B, and B inheriting from A. This will crash your code.

    - Not using super(): When overriding __init__ in a child class, beginners forget to call super().__init__(), which causes the parent's data to not initialize.
'''

'''
===================================================================
Topic 4: Inhertance (Reusability)
===================================================================

Definition: 
    Inheritance allows a Child Class to inherit all the features (data and methods) from a Parent Class. It’s like a child inheriting their parents' property. You don't have to rewrite the same code again
'''
# Syntax
class ChildClass(ParentClass):
    # Additional features or modified features


# EXAMPLE
# Parent Class (General)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def info(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}")

# Child Class (Specific)
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        # super() calls the Parent's __init__ to save time
        super().__init__(owner, balance) 
        self.interest = interest_rate

    def show_interest(self):
        print(f"Annual Interest Rate: {self.interest}%")

# Usage
my_savings = SavingsAccount("Aryan", 5000, 4.5)
my_savings.info()          # Using Parent's method
my_savings.show_interest() # Using Child's method


'''
Explanation in Simple Language:
    Yahan BankAccount ek general class hai. Par SavingsAccount ek special type ka account hai jisme "interest rate" bhi hota hai. super() use karne se hume owner aur balance ko phir se initialize nahi karna pada

'''

'''
Common Mistakes:
    - Forgetting super(): Agar aap child class mein __init__ likhte hain aur super() call nahi karte, toh parent class ke variables (like owner) create nahi honge.

    - Overwriting without care: If you name a child method the same as a parent method, the parent method will be hidden (this is actually another topic called Overriding).
'''

'''
===================================================================
Topic 5: Encapsulation (Data Privacy)
===================================================================
Definition: 
    Encapsulation is about hiding the internal details of an object and only showing what is necessary. It protects the data from being changed accidentally by code outside the class. In Python, we use a Double Underscore (__) to make a variable private.
'''

#Syntax
self.__private_variable = value

# Example
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private Variable (Cannot be accessed directly)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Added {amount}")

    def check_balance(self):
        # This is a 'Getter' method to safely show private data
        return f"Secret Balance is: {self.__balance}"

# Usage
acc = BankAccount("Rahul", 1000)
print(acc.owner)        # Works fine (Public)
# print(acc.__balance)  # Error! Direct access is blocked.
print(acc.check_balance()) # Works (Controlled access)


'''
Explanation in Simple Language: 
    Real world mein, koi bhi aapki jeb se paise nikal kar nahi gin sakta; aapko unhe batana padta hai. Waise hi, __balance ko private kar diya gaya hai taaki bahar ka koi bhi code acc.__balance = 0 na kar sake. Data ko change karne ke liye hume deposit() jaise methods use karne honge jo class ke rules follow karte hain.
'''

'''
Common Mistakes:
    - Thinking it's 100% secure: Python uses "Name Mangling." You can technically still access it via _BankAccount__balance, but it is strictly discouraged.

    - Using single underscore: _variable (single underscore) is just a suggestion to keep it private. __variable (double) is what Python actually restricts.
'''

'''
===================================================================
Topic 6: Polymorphism (Flexibility)
===================================================================

Simple Definition: 
    Polymorphism means "many forms." In programming, it means that different classes can have methods with the same name, but they do different things.

Syntax: Just use the same method name in different classes.
'''

class CreditCardPayment:
    def process(self, amount):
        print(f"Processing ₹{amount} via Credit Card. (2% tax applied)")

class UPIPayment:
    def process(self, amount):
        print(f"Processing ₹{amount} via UPI. (0% tax applied)")

# Usage: One function can handle any payment type
def make_payment(payment_method, amount):
    payment_method.process(amount)

cc = CreditCardPayment()
upi = UPIPayment()

make_payment(cc, 500)   # Same function call
make_payment(upi, 500)  # Different output logic

'''
Explanation in Simple Language: 
    Sochiye ek "Play" button hai. Music app mein wo gaana bajata hai, aur Video app mein video. Naam ek hi hai (process), lekin class ke hisaab se kaam badal gaya. Isse hamara code bahut flexible ho jata hai.
'''

'''
Common Mistakes:
    Mismatched Arguments: 
        If CreditCard.process() takes 1 argument and UPI.process() takes 2, polymorphism will break when you try to call them in a loop
'''

'''
===================================================================
Topic 7: Abstraction (Enforcing Rules)
===================================================================

Simple Definition: 
    Abstraction is like a Contract. It is used to hide complex implementation details and only show the essential features. An Abstract Class is a class that cannot be used to create objects directly; it only serves as a blueprint for other classes.

    Think of a "Vehicle" blueprint—you can't buy a "Vehicle," you can only buy a "Car" or "Bike" that follows the Vehicle's rules.

'''



# Syntax: 
# To use abstraction, we must import ABC (Abstract Base Class) from the abc module.

from abc import ABC, abstractmethod

class Parent(ABC):
    @abstractmethod
    def must_implement(self):
        pass


# Example Code:
from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        # Every shape MUST have an area, but logic is different for each
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    # Implementing the abstract method is COMPULSORY
    def calculate_area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        return 3.14 * self.radius * self.radius

# Usage
# s = Shape() # This would throw an ERROR
sq = Square(4)
print(f"Square Area: {sq.calculate_area()}")

'''
Explanation in Simple Language: 
    Abstraction ka matlab hai "Zaroori cheezein batao, details chhupao." Shape class ne ek rule bana diya ki jo bhi mujhe use karega, use calculate_area method likhna hi padega. Isse programmer galti nahi karta aur code ka structure maintain rehta hai.

'''

'''
Common Mistakes:
    Forgetting Implementation: 
        If you inherit from an abstract class but forget to define the @abstractmethod, Python will not let you create an object of the child class.

    Instantiating the Abstract Class: Trying to create an object of the parent class itself.
'''




'''
===================================================================
Topic 8: Inner Classes (Classes inside Classes)
===================================================================

Simple Definition: Sometimes, one class is so closely related to another that it makes sense to define it inside that class. This is called an Inner Class. It is used when an object of the inner class cannot exist without the outer class.

Example: A "Car" has an "Engine." The Engine doesn't make sense without the Car.
'''





# Syntax:
class Outer:
    def __init__(self):
        self.inner = self.Inner()

    class Inner:
        # Inner class logic

# Example Code:
class Laptop:
    def __init__(self, brand, cpu_type):
        self.brand = brand
        # Creating an inner class object inside the constructor
        self.processor = self.CPU(cpu_type) 

    def show_specs(self):
        print(f"Laptop: {self.brand}")
        self.processor.display_info()

    # Inner Class
    class CPU:
        def __init__(self, type):
            self.type = type
        
        def display_info(self):
            print(f"Processor: {self.type}")

# Usage
my_laptop = Laptop("Dell", "i7")
my_laptop.show_specs()

'''
Explanation in Simple Language: Inner class tab use hoti hai jab do cheezein "Tightly Coupled" (gehra rishta) hoti hain. Yahan CPU class, Laptop ke bina adhuri hai. Isse code organized rehta hai aur namespaces clean rehte hain.

Common Mistakes:

Accessing Inner Class Directly: Beginners often try to call the inner class without going through the outer class instance. Usually, you need an outer object first.

'''

'''
===================================================================
Topic 9: Method Overloading vs Overriding
===================================================================

Simple Definition:
    Overriding: 
        Child class changes a method inherited from the parent (which we saw in Polymorphism).

    Overloading: 
        Having multiple methods with the same name but different parameters in the same class.
'''



# Note: Python does not support traditional Overloading (like Java or C++). In Python, if you define two methods with the same name, the last one will overwrite the first. However, we can achieve it using "Default Arguments."

# Example Code (Pythonic Overloading):
class Calculator:
    # We use default values to handle different numbers of inputs
    def add(self, a, b, c = 0):
        return a + b + c

calc = Calculator()
print(calc.add(5, 10))      # Works with 2 numbers
print(calc.add(5, 10, 20))  # Works with 3 numbers




