"""Product inventory constructor, stock movement, and sales examples."""


class Product:
    """Represent a product and its current inventory state."""

    def __init__(self, product_id, name, category, price, quantity=0, supplier="Unknown"):
        for label, value in (
            ("Product ID", product_id), ("Name", name),
            ("Category", category), ("Supplier", supplier),
        ):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{label} cannot be empty")
        if isinstance(price, bool) or not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be non-negative")
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer")
        self.product_id = product_id.strip()
        self.name = name.strip()
        self.category = category.strip()
        self.price = float(price)
        self.quantity = quantity
        self.supplier = supplier.strip()
        self.reorder_level = 10
        self.sales_count = 0
        self.revenue_generated = 0.0

    def add_stock(self, quantity):
        """Add a positive whole number of units to stock."""
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            return "Invalid quantity. Must be a positive integer."
        self.quantity += quantity
        return f"Added {quantity} units. New stock: {self.quantity}"

    def sell_product(self, quantity):
        """Sell units only when quantity and stock availability are valid."""
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            return "Invalid sale quantity"
        if quantity > self.quantity:
            return f"Insufficient stock. Available: {self.quantity}"
        self.quantity -= quantity
        self.sales_count += quantity
        sale_revenue = quantity * self.price
        self.revenue_generated += sale_revenue
        return f"Sold {quantity} units for USD {sale_revenue:.2f}. Remaining stock: {self.quantity}"

    def needs_reorder(self):
        """Return True when stock is at or below the reorder threshold."""
        return self.quantity <= self.reorder_level

    def calculate_inventory_value(self):
        """Return the total value of on-hand stock."""
        return self.quantity * self.price

    def display_product_info(self):
        """Print product details and sales metrics."""
        print("=" * 55)
        print("PRODUCT INFORMATION")
        print("=" * 55)
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Price: USD {self.price:.2f}")
        print(f"Current Stock: {self.quantity} units")
        print(f"Supplier: {self.supplier}")
        print(f"Reorder Level: {self.reorder_level} units")
        print(f"Total Sales: {self.sales_count} units")
        print(f"Revenue Generated: USD {self.revenue_generated:.2f}")
        print(f"Inventory Value: USD {self.calculate_inventory_value():.2f}")
        print("REORDER ALERT: Stock is at or below minimum level!" if self.needs_reorder()
              else "Stock level is adequate")
        print("=" * 55)


def create_sample_inventory():
    """Create sample products, including products that use defaults."""
    return [
        Product("ELEC001", "Wireless Headphones", "Electronics", 79.99, 25, "TechSupply Co."),
        Product("ELEC002", "Smartphone Case", "Electronics", 19.99, 50, "MobileAccessories Inc."),
        Product("ELEC003", "USB Cable", "Electronics", 12.99, 100, "TechSupply Co."),
        Product("BOOK001", "Python Programming Guide", "Books", 45.99, 15, "BookWorld"),
        Product("BOOK002", "Data Science Handbook", "Books", 59.99, 8, "BookWorld"),
        Product("CLOTH001", "Cotton T-Shirt", "Clothing", 24.99, 30, "FashionHub"),
        Product("CLOTH002", "Denim Jeans", "Clothing", 69.99, 20, "FashionHub"),
        Product("HOME001", "Coffee Maker", "Home & Kitchen", 89.99, 12, "HomeGoods Ltd."),
        Product("HOME002", "Blender", "Home & Kitchen", 129.99, 8, "HomeGoods Ltd."),
        Product("SPORT001", "Yoga Mat", "Sports", 34.99, 18, "SportEquip Co."),
        Product("MISC001", "Notebook", "Stationery", 4.99),
    ]


def simulate_sales_activity(products):
    """Simulate sample sales and return the successful revenue total."""
    print("SIMULATING SALES ACTIVITIES")
    print("=" * 60)
    sales_data = [(0, 5), (1, 12), (2, 25), (3, 3), (4, 2),
                  (5, 8), (6, 4), (7, 2), (8, 1), (9, 6)]
    total_revenue = 0.0
    for product_index, quantity in sales_data:
        product = products[product_index]
        result = product.sell_product(quantity)
        print(f"- {product.name}: {result}")
        if result.startswith("Sold "):
            total_revenue += quantity * product.price
    print(f"\nTotal Revenue from Sales: USD {total_revenue:.2f}")
    print("=" * 60)
    return total_revenue


def demo_inventory():
    """Run initial inventory, sales, and summary demonstrations."""
    inventory = create_sample_inventory()
    print("INVENTORY MANAGEMENT SYSTEM")
    print(f"Inventory created with {len(inventory)} products\n")
    print("INITIAL INVENTORY STATUS")
    for product in inventory:
        product.display_product_info()
        print()
    simulate_sales_activity(inventory)
    print("\nUPDATED INVENTORY STATUS")
    total_inventory_value = 0.0
    products_needing_reorder = []
    for product in inventory:
        product.display_product_info()
        total_inventory_value += product.calculate_inventory_value()
        if product.needs_reorder():
            products_needing_reorder.append(product.name)
        print()
    print("INVENTORY SUMMARY REPORT")
    print(f"Total Products: {len(inventory)}")
    print(f"Total Inventory Value: USD {total_inventory_value:.2f}")
    print(f"Products Needing Reorder: {len(products_needing_reorder)}")
    if products_needing_reorder:
        print("\nProducts to Reorder:")
        for product_name in products_needing_reorder:
            print(f"- {product_name}")
    else:
        print("\nAll products have adequate stock levels")


if __name__ == "__main__":
    demo_inventory()
