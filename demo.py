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
