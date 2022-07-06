from abc import ABC, abstractmethod
from dataclasses import dataclass


class Order:
    items: list[str] = []
    quantities: list[int] = []
    prices: list[float] = []
    status: str = "open"

    def add_item(self, name: str, quantity: int, price: float) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self) -> float:
        total = 0.0
        for i in range(len(self.quantities)):
            total += self.prices[i] * self.quantities[i]
        return total

    def set_status(self) -> None:
        self.status = "paid"


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order):
        """Pay with credit"""
        

class PaymentProcessorWithSMS(PaymentProcessor):
    @abstractmethod
    def auth_sms(self, code):
        """Authenticate with sms code before pay"""


@dataclass
class CreditPaymentProcessor(PaymentProcessor):
    security_code: int
    verified: bool = False
    
    def auth_sms(self, code):
        raise Exception('Credit Payment does not required auth sms')
    
    def pay(self, order: Order):
        print("Processing credit payment")
        print(f"Verifying security code {self.security_code}")
        order.set_status()


class DebitPaymentProcessor(PaymentProcessor):
    security_code: int
    verified: bool = False
    
    def auth_sms(self, code):
        print(f"Verifying sms code {code}")
        self.verified = True
    
    def pay(self, order: Order):
        print("Processing debit payment")
        print(f"Verifying security code {self.security_code}")
        order.set_status()
        

@dataclass
class PayPalPaymentProcessor(PaymentProcessor):
    email_address: str
    verified: bool = False
    
    def auth_sms(self, code):
        print(f"Verifying sms code {code}")
        self.verified = True
    
    def pay(self, order: Order):
        print("Processing debit payment")
        print(f"Verifying email address {self.email_address}")
        self.validate_email()
        order.set_status()
        
    def validate_email(self):
        if not isinstance(self.email_address, str):
            raise Exception("Invalid email address")
        
        if '@' not in self.email_address:
            raise Exception("Not a valid email address")


if __name__ == "__main__":
    order = Order()
    pay_processor = CreditPaymentProcessor("Johnson@sloovi.com")
    order.add_item("Sumo", 12, 3.45)
    order.add_item("Bama", 6, 230)
    order.add_item("Tuna", 2, 560)
    print(f"Total price: {order.total_price()}")
    pay_processor.auth_sms(34590)
    pay_processor.pay(order)
    print(f"Order status: {order.status}")
