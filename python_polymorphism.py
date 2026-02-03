"""
POLYMORPHISM IN PYTHON – COMPLETE GUIDE
--------------------------------------
"""

print("========== POLYMORPHISM ==========\n")

# ==================================================
# 1. DEFINITION (IN COMMENTS)
# ==================================================

# Polymorphism means "one name, many forms".
# In Python, the same function, method, or operator
# behaves differently depending on the object or data type.


# ==================================================
# 2. SIMPLE EXAMPLE – FUNCTION POLYMORPHISM
# ==================================================

print("---- Function Polymorphism ----")

print(len("Python"))        # string -> counts characters
print(len([1, 2, 3, 4]))    # list -> counts items
print(len({"a": 1, "b": 2})) # dict -> counts keys


# ==================================================
# 3. SIMPLE EXAMPLE – METHOD POLYMORPHISM
# ==================================================

print("\n---- Method Polymorphism ----")

class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

Dog().speak()
Cat().speak()

# Same method name: speak()
# Different behavior -> polymorphism


# ==================================================
# 4. OPERATOR POLYMORPHISM
# ==================================================

print("\n---- Operator Polymorphism ----")

print(10 + 5)           # integer addition
print("Hi " + "There")  # string concatenation
print([1, 2] + [3, 4])  # list merging


# ==================================================
# 5. DUCK TYPING (POLYMORPHISM WITHOUT INHERITANCE)
# ==================================================

print("\n---- Duck Typing ----")

class Car:
    def move(self):
        print("Car is moving")

class Bike:
    def move(self):
        print("Bike is moving")

for v in (Car(), Bike()):
    v.move()

# Python only checks:
# "Does the object have a move() method?"


# ==================================================
# 6. METHOD OVERLOADING (PYTHON WAY)
# ==================================================

print("\n---- Method Overloading (Python Style) ----")

class Test:
    def add(self, a, b, c=0):
        return a + b + c

t = Test()
print(t.add(2, 3))      # works with 2 arguments
print(t.add(2, 3, 4))   # works with 3 arguments


# ==================================================
# 7. HEAVY / REAL-WORLD POLYMORPHISM EXAMPLE
# ==================================================
# PAYMENT SYSTEM (INTERVIEW + PROJECT LEVEL)
# ==================================================

print("\n---- Real-World Polymorphism: Payment System ----")

class Payment:
    def pay(self, amount):
        raise NotImplementedError("Pay method must be implemented")

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class NetBanking(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Net Banking")

class Cash(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Cash")

# Polymorphic behavior
payments = [
    CreditCard(),
    UPI(),
    NetBanking(),
    Cash()
]

for payment in payments:
    payment.pay(1000)

# Same method: pay()
# Different implementations
# Python decides at runtime which one to call







"""
MINI PROJECT: ONLINE SHOPPING ORDER SYSTEM
------------------------------------------
This project demonstrates:
1. Encapsulation      -> private data (__)
2. Abstraction        -> abstract base class
3. Inheritance        -> child classes
4. Polymorphism       -> same method, different behavior
"""

from abc import ABC, abstractmethod


# ==================================================
# 1. ABSTRACTION
# ==================================================

class Payment(ABC):
    """Abstract base class"""

    @abstractmethod
    def pay(self, amount):
        pass


# ==================================================
# 2. INHERITANCE + POLYMORPHISM
# ==================================================

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Payment of ₹{amount} done using Credit Card")


class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Payment of ₹{amount} done using UPI")


class CashOnDelivery(Payment):
    def pay(self, amount):
        print(f"Payment of ₹{amount} will be collected on delivery")


# ==================================================
# 3. ENCAPSULATION
# ==================================================

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.__items = []        # private
        self.__total_price = 0   # private

    def add_item(self, name, price):
        if price <= 0:
            print("Invalid item price")
            return

        self.__items.append(name)
        self.__total_price += price

    def get_total(self):
        return self.__total_price

    def show_order(self):
        print("\nOrder Summary")
        print("Customer:", self.customer_name)
        print("Items:", self.__items)
        print("Total Price: ₹", self.__total_price)


# ==================================================
# 4. POLYMORPHISM IN ACTION
# ==================================================

class Checkout:
    def __init__(self, payment_method: Payment):
        self.payment_method = payment_method

    def process_payment(self, amount):
        self.payment_method.pay(amount)


# ==================================================
# 5. USING THE PROJECT
# ==================================================

print("========== ONLINE SHOPPING SYSTEM ==========")

# Create order
order = Order("Manish")

# Add items
order.add_item("Laptop", 50000)
order.add_item("Mouse", 500)
order.add_item("Keyboard", 1500)

# Show order
order.show_order()

total_amount = order.get_total()

# Choose payment method (POLYMORPHISM)
payment_methods = [
    CreditCardPayment(),
    UPIPayment(),
    CashOnDelivery()
]

print("\nProcessing Payments:\n")

for method in payment_methods:
    checkout = Checkout(method)
    checkout.process_payment(total_amount)