from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class stripePayment:
    def pay(self, amount):
        print(f"Processing payment of ${amount} through Stripe.")

class paypalPayment:
    def pay(self, amount):
        print(f"Processing payment of ${amount} through PayPal.")

class bkashPayment:
    def pay(self, amount):
        print(f"Processing payment of ${amount} through Bkash.")


class paymentService:
    def __init__(self, processor: PaymentProcessor):
        self.processor = processor
    
    def makePayment(self, amount):
        self.processor.pay(amount)

# Usage
stripe_processor = paymentService(stripePayment())
stripe_processor.makePayment(100)

paypal_processor = paymentService(paypalPayment())
paypal_processor.makePayment(200)


bkash_processor = paymentService(bkashPayment())
bkash_processor.makePayment(300)