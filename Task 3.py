# Implement a Simple Payment System:
# Design a payment system where users can: pay via Credit Card or PayPal and use polymorphism to handle different payment types.

from abc import ABC, abstractmethod # abc = abstract base class. The "abstractmethod" decorator forces subclasses to implement the method

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass # This method HAS to be implemented so that other subclasses can acc implement the abstract method.


class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number: str, card_holder: str, expiry_date: str, cvv: str):
        # Note that all of the attributes are defined as strings bc they're not meant for mathematical operations and leading zeroes could exist. 
        self.card_number = card_number
        self.card_holder = card_holder
        self.expiry_date = expiry_date
        self.cvv = cvv

    def process_payment(self, amount: float):
        # Simulating a credit card transaction
        print(f"Processing Credit Card payment of ${amount:.2f} for {self.card_holder}")
        return f"Credit Card payment of ${amount:.2f} successful!"


class PayPalPayment(PaymentMethod):
    def __init__(self, email: str):
        self.email = email

    def process_payment(self, amount: float):
        # Simulating a PayPal transaction
        print(f"Processing PayPal payment of ${amount:.2f} for {self.email}")
        return f"PayPal payment of ${amount:.2f} successful!"


def process_transaction(payment_method: PaymentMethod, amount: float):
    return payment_method.process_payment(amount)

credit_card_payment = CreditCardPayment("1234-5678-9012-3456", "John Doe", "12/26", "123")
paypal_payment = PayPalPayment("johndoe@example.com")
print(process_transaction(credit_card_payment, 100.0))
print(process_transaction(paypal_payment, 50.0))