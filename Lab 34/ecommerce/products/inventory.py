class InventoryManager:
    def __init__(self):
        self.stock_levels = {}

    def add_stock(self, product_id, quantity):
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            raise ValueError("Stock quantity must be a positive integer")
        self.stock_levels[product_id] = self.stock_levels.get(product_id, 0) + quantity
        return self.stock_levels[product_id]

    def remove_stock(self, product_id, quantity):
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            raise ValueError("Stock quantity must be a positive integer")
        current = self.stock_levels.get(product_id, 0)
        if current < quantity:
            return False
        self.stock_levels[product_id] = current - quantity
        return True

    def check_stock(self, product_id):
        return self.stock_levels.get(product_id, 0)

    def is_in_stock(self, product_id, quantity=1):
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity < 0:
            return False
        return self.check_stock(product_id) >= quantity
