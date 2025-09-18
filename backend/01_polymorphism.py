# Payment Gateway Example
# Different payment providers but same interface:

from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class PayPal(PaymentGateway):
    def __init__(self, user_mail):
        self.user_mail = user_mail


    def pay(self, amount):
        return f"Paid {amount} using PayPal account {self.user_mail}."
    

class Stripe(PaymentGateway):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        return f"Paid {amount} using Stripe with card {self.card_number}."
    
class GooglePay(PaymentGateway):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def pay(self, amount):
        return f"Paid {amount} using Google Pay with phone number {self.phone_number}."



class SpecialDiscount(PayPal):
    def __init__(self, user_mail, discount):
        super().__init__(user_mail)
        self.discount = discount

    def pay(self, amount):
        discounted_amount = amount - self.discount
        return f"Paid {discounted_amount} using PayPal account {self.user_mail} with a discount of {self.discount}."
    

payments = [
    PayPal("user1@gmail.com"),
    Stripe("1234-5678-9876-5432"),
    GooglePay("9876543210"),
    SpecialDiscount("user2@gmail.com", 20)

]

for payment in payments:
    print(f"{payment.__class__.__name__}: {payment.pay(100)}")
        
        