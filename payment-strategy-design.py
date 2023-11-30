from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    
class DebitCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing {amount} payment by debit card")
        
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing {amount} payment by credit card") 

class PaypalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing {amount} payment by PayPal")
        
class PaymentContext:
    def __init__(self, strategy):
        self._strategy = strategy
    
    def execute_payment(self, amount):
        self._strategy.pay(amount)
        
# Usage        
amount = 1000

context = PaymentContext(DebitCardPayment())
context.execute_payment(amount)

context = PaymentContext(PaypalPayment())
context.execute_payment(amount)
