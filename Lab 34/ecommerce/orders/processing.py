from datetime import datetime
from enum import Enum


class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class OrderItem:
    def __init__(self, product_id, quantity, unit_price):
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        if not isinstance(unit_price, (int, float)) or isinstance(unit_price, bool) or unit_price <= 0:
            raise ValueError("Unit price must be positive")
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = float(unit_price)

    @property
    def total_price(self):
        return self.quantity * self.unit_price


class Order:
    def __init__(self, order_id, user_id):
        self.order_id = order_id
        self.user_id = user_id
        self.items = []
        self.status = OrderStatus.PENDING
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def add_item(self, product_id, quantity, unit_price):
        item = OrderItem(product_id, quantity, unit_price)
        self.items.append(item)
        self.updated_at = datetime.now()

    @property
    def total_amount(self):
        return sum(item.total_price for item in self.items)

    def update_status(self, new_status):
        if not isinstance(new_status, OrderStatus):
            raise TypeError("new_status must be an OrderStatus value")
        self.status = new_status
        self.updated_at = datetime.now()


class OrderManager:
    def __init__(self):
        self.orders = {}
        self.next_order_id = 1

    def create_order(self, user_id):
        order = Order(self.next_order_id, user_id)
        self.orders[self.next_order_id] = order
        self.next_order_id += 1
        return order

    def get_order(self, order_id):
        return self.orders.get(order_id)

    def get_user_orders(self, user_id):
        return [order for order in self.orders.values() if order.user_id == user_id]
