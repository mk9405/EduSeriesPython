"""
CHAPTER: ENCAPSULATION IN PYTHON
================================

Encapsulation is about protecting data inside a class by bundling properties 
and methods together and controlling access.

Key Concepts:
1. Public: name (Accessible everywhere)
2. Protected: _name (Convention: Please don't touch)
3. Private: __name (Enforced: Cannot access directly)
"""
"""
Python Encapsulation – Complete Example File
--------------------------------------------
This file demonstrates:
1. Private variables
2. Getter and Setter methods
3. Validation using encapsulation
4. Protected variables
5. Private methods
6. Name mangling
"""

# ==================================================
# 1. PRIVATE PROPERTIES (__variable)
# ==================================================

class Person:
    def __init__(self, name, age):
        self.name = name          # Public variable
        self.__age = age          # Private variable (cannot access directly)

    def get_age(self):
        # Getter method to read private variable
        return self.__age

    def set_age(self, age):
        # Setter method with validation
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")


print("---- Private Property Example ----")
p1 = Person("Emil", 25)

print(p1.name)           # ✅ Allowed (public)
print(p1.get_age())      # ✅ Allowed via getter

p1.set_age(30)           # Modify using setter
print(p1.get_age())

# print(p1.__age)        # ❌ Not allowed (private)


# ==================================================
# 2. ENCAPSULATION WITH VALIDATION (Student Example)
# ==================================================

class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0          # Private variable

    def set_grade(self, grade):
        # Validation logic
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Grade must be between 0 and 100")

    def get_grade(self):
        return self.__grade

    def get_status(self):
        # Business logic hidden inside class
        if self.__grade >= 60:
            return "Passed"
        return "Failed"


print("\n---- Student Encapsulation Example ----")
student = Student("Tobias")
student.set_grade(85)

print("Grade:", student.get_grade())
print("Status:", student.get_status())


# ==================================================
# 3. PROTECTED PROPERTIES (_variable)
# ==================================================

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary     # Protected variable (convention only)

print("\n---- Protected Property Example ----")
emp = Employee("Linus", 50000)

print(emp.name)        # ✅ Public
print(emp._salary)    # ⚠️ Technically allowed, but should be avoided


# ==================================================
# 4. PRIVATE METHODS (__method)
# ==================================================

class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self, num):
        # Private method: checks if input is a number
        return isinstance(num, (int, float))

    def add(self, num):
        # Public method uses private method internally
        if self.__validate(num):
            self.result += num
        else:
            print("Invalid number")

print("\n---- Private Method Example ----")
calc = Calculator()

calc.add(10)
calc.add(5)
calc.add("hello")      # Invalid input

print("Result:", calc.result)

# calc.__validate(5)   # ❌ Not allowed (private method)


# ==================================================
# 5. NAME MANGLING (How Python Handles __)
# ==================================================

class Demo:
    def __init__(self):
        self.__secret = "Hidden Value"

print("\n---- Name Mangling Example ----")
d = Demo()

# Python internally renames __secret to _ClassName__secret
print(d._Demo__secret)   # ⚠️ Works, but NOT recommended



#=======================================================================
#=======================================================================
#=======================================================================

##### for practice 

"""
Bank / ATM System using Encapsulation
------------------------------------
Concepts used:
1. Private variables (__balance, __pin)
2. Getter method
3. Setter-style methods with validation
4. Private method for PIN verification
"""

class BankAccount:
    def __init__(self, account_holder, balance, pin):
        self.account_holder = account_holder   # Public variable
        self.__balance = balance               # Private variable
        self.__pin = pin                       # Private variable

    # ---------- PRIVATE METHOD ----------
    def __verify_pin(self, entered_pin):
        # Checks whether entered PIN is correct
        return self.__pin == entered_pin

    # ---------- PUBLIC METHODS ----------
    def get_balance(self, entered_pin):
        # Allows balance check only after PIN verification
        if self.__verify_pin(entered_pin):
            return self.__balance
        else:
            return "Invalid PIN"

    def deposit(self, amount):
        # Deposit does not need PIN
        if amount > 0:
            self.__balance += amount
            return "Amount deposited successfully"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount, entered_pin):
        # Withdraw requires PIN verification
        if not self.__verify_pin(entered_pin):
            return "Invalid PIN"

        if amount <= 0:
            return "Invalid withdrawal amount"

        if amount > self.__balance:
            return "Insufficient balance"

        self.__balance -= amount
        return "Withdrawal successful"


# ================== USING THE CLASS ==================

print("---- ATM Simulation ----")

account = BankAccount("Manish", 5000, 1234)

print("Account Holder:", account.account_holder)

print("Balance:", account.get_balance(1234))     # Correct PIN
print("Withdraw:", account.withdraw(1000, 1234))
print("Balance:", account.get_balance(1234))

print("Withdraw:", account.withdraw(500, 1111))  # Wrong PIN
print("Deposit:", account.deposit(2000))
print("Balance:", account.get_balance(1234))

# print(account.__balance)  # ❌ Not allowed (private)
# print(account.__pin)      # ❌ Not allowed (private)




"""
Login System using Encapsulation
--------------------------------
Concepts used:
1. Private variables (__username, __password)
2. Getter-like methods (login check)
3. Setter-like methods (change password)
4. Private method for validation
"""

class LoginSystem:
    def __init__(self, username, password):
        self.__username = username      # Private variable
        self.__password = password      # Private variable

    # ---------- PRIVATE METHOD ----------
    def __validate_credentials(self, username, password):
        # This method checks if credentials are correct
        return self.__username == username and self.__password == password

    # ---------- PUBLIC METHOD ----------
    def login(self, username, password):
        # Public method to perform login
        if self.__validate_credentials(username, password):
            return "Login successful"
        else:
            return "Invalid username or password"

    # ---------- CHANGE PASSWORD ----------
    def change_password(self, old_password, new_password):
        # Password can be changed only if old password matches
        if self.__password != old_password:
            return "Old password is incorrect"

        if len(new_password) < 6:
            return "Password must be at least 6 characters long"

        self.__password = new_password
        return "Password changed successfully"


# ================== USING THE CLASS ==================

print("---- Login System ----")

user = LoginSystem("admin", "admin123")

# Correct login
print(user.login("admin", "admin123"))

# Wrong login
print(user.login("admin", "wrongpass"))

# Change password
print(user.change_password("admin123", "newpass456"))

# Login with old password
print(user.login("admin", "admin123"))

# Login with new password
print(user.login("admin", "newpass456"))

# ❌ Direct access not allowed
# print(user.__password)
# print(user.__username)