"""
=========================================================
BANK MANAGEMENT SYSTEM
Inheritance Based Real-World Python Project
=========================================================

Concepts Used:
- Single Inheritance
- Multilevel Inheritance
- super() keyword
- Real-world OOP design
"""


# =========================================================
# BASE CLASS: BANK
# =========================================================
class Bank:
    def __init__(self, bank_name, ifsc):
        self.bank_name = bank_name
        self.ifsc = ifsc

    def bank_info(self):
        print("Bank Name:", self.bank_name)
        print("IFSC Code:", self.ifsc)


# =========================================================
# DERIVED CLASS: USER (inherits Bank)
# =========================================================
class User(Bank):
    def __init__(self, bank_name, ifsc, name, account_no, balance):
        super().__init__(bank_name, ifsc)
        self.name = name
        self.account_no = account_no
        self.balance = balance
        self.active = True

    def deposit(self, amount):
        if self.active:
            self.balance += amount
            print(amount, "deposited successfully")
        else:
            print("Account is blocked")

    def withdraw(self, amount):
        if not self.active:
            print("Account is blocked")
            return

        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(amount, "withdrawn successfully")

    def check_balance(self):
        print("Current Balance:", self.balance)

    def user_info(self):
        self.bank_info()
        print("User Name:", self.name)
        print("Account No:", self.account_no)
        print("Balance:", self.balance)
        print("Status:", "Active" if self.active else "Blocked")


# =========================================================
# DERIVED CLASS: ADMIN (inherits User)
# =========================================================
class Admin(User):
    def block_account(self):
        self.active = False
        print("Account has been blocked")

    def unblock_account(self):
        self.active = True
        print("Account has been unblocked")


# =========================================================
# PROGRAM EXECUTION
# =========================================================
print("\n--- Creating User Account ---")
user1 = User(
    bank_name="State Bank of Python",
    ifsc="SBIN0001234",
    name="Manish Kumar",
    account_no=100200300,
    balance=5000
)

user1.user_info()

print("\n--- User Transactions ---")
user1.deposit(2000)
user1.withdraw(1000)
user1.check_balance()

print("\n--- Admin Actions ---")
admin = Admin(
    bank_name="State Bank of Python",
    ifsc="SBIN0001234",
    name="Admin",
    account_no=999999,
    balance=0
)

admin.block_account()

# Admin blocks user's account
user1.active = admin.active

print("\n--- User Transaction After Blocking ---")
user1.withdraw(500)


# =========================================================
# END OF PROGRAM
# =========================================================
