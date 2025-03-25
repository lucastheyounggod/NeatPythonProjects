from abc import ABC, abstractmethod

# Abstract Class
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        """Abstract method - Must be implemented by all payment types"""
        pass

# Child Classes
class CreditCard(Payment):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"

class PayPal(Payment):
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}"

class Crypto(Payment):
    def process_payment(self, amount):
        return f"Processing cryptocurrency payment of ${amount}"

class BankTransfer(Payment):
    def process_payment(self, amount):
        return f"Processing Bank Transfer payment of ${amount}"

user_pins = {
    "credit card": "1234",
    "paypal": "4321",
    "crypto": "5678",
    "bank transfer": "8765"
}

payment_method = {
        "credit card": CreditCard(),
        "paypal": PayPal(),
        "crypto": Crypto(),
        "bank transfer": BankTransfer()
}

def payment_choice():
    """Users are to choose a payment method"""
    choice = input("Enter a payment method (Credit Card, PayPal, Crypto, Bank Transfer): ").strip().lower()

    if choice in payment_method:
        attempts = 0
        while attempts < 3:
            pin = input("Enter your 4-digit PIN: ")

            print(f"Expected PIN: {user_pins[choice]}")

            if pin == user_pins[choice]:
                amount = float(input("Enter amount to pay: "))
                print(payment_method[choice].process_payment(amount))
                return
            else:
                attempts += 1
                print(f"Incorrect PIN! {3 - attempts} attempts remaining.")
        print("Too many incorrect attempts. Access blocked.")
    else:
        print("Invalid payment method. Please try again!")


payment_choice()