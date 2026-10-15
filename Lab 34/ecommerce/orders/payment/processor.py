import secrets
from datetime import datetime
from enum import Enum


class PaymentMethod(Enum):
    CREDIT_CARD = "credit_card"
    DEBIT_CARD = "debit_card"
    PAYPAL = "paypal"
    BANK_TRANSFER = "bank_transfer"


class PaymentStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"


class Payment:
    def __init__(self, payment_id, order_id, amount, method):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount <= 0:
            raise ValueError("Payment amount must be positive")
        if not isinstance(method, PaymentMethod):
            raise TypeError("method must be a PaymentMethod value")
        self.payment_id = payment_id
        self.order_id = order_id
        self.amount = float(amount)
        self.method = method
        self.status = PaymentStatus.PENDING
        self.transaction_id = None
        self.created_at = datetime.now()
        self.processed_at = None

    def process(self):
        self.status = PaymentStatus.PROCESSING
        self.transaction_id = secrets.token_hex(16)
        self.status = PaymentStatus.COMPLETED
        self.processed_at = datetime.now()
        return True


class PaymentProcessor:
    def __init__(self):
        self.payments = {}
        self.next_payment_id = 1

    def create_payment(self, order_id, amount, method):
        payment = Payment(self.next_payment_id, order_id, amount, method)
        self.payments[self.next_payment_id] = payment
        self.next_payment_id += 1
        return payment

    def process_payment(self, payment_id):
        payment = self.payments.get(payment_id)
        return payment.process() if payment else False

    def get_payment(self, payment_id):
        return self.payments.get(payment_id)

    def get_order_payments(self, order_id):
        return [payment for payment in self.payments.values() if payment.order_id == order_id]
