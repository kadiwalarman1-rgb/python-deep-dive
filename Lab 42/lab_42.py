"""
Lab 42: Data Hiding with @property
----------------------------------
One complete script covering:
- Private attributes and Python name mangling
- @property getters and validated setters
- Price discounts
- Multiple properties (price, quantity, category)
- Read-only computed properties
- Restocking, selling, and inventory valuation
- Validation tests and a short demo

Run:
    python lab_42_property_data_hiding.py
"""

from math import isfinite


VALID_CATEGORIES = {"Electronics", "Clothing", "Books", "Home", "Sports"}


class Product:
    """A product with a private price and validated public property."""

    MAX_PRICE = 100_000.00

    def __init__(self, name: str, price: float) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name must be a non-empty string.")

        self.name = name.strip()
        self.__price = 0.0
        self.price = price  # Route initial value through the setter.

    @property
    def price(self) -> float:
        """Return the product price without exposing the private field."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Set price only when it meets the validation rules."""
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Price must be a number.")
        if not isfinite(value):
            raise ValueError("Price must be a finite number.")
        if value < 0:
            raise ValueError("Price cannot be negative.")
        if value > self.MAX_PRICE:
            raise ValueError(f"Price cannot exceed ${self.MAX_PRICE:,.2f}.")
        self.__price = float(value)

    def apply_discount(self, percentage: float) -> float:
        """Apply a discount from 0 to 100 percent and return the new price."""
        if isinstance(percentage, bool) or not isinstance(percentage, (int, float)):
            raise TypeError("Discount percentage must be a number.")
        if not isfinite(percentage) or not 0 <= percentage <= 100:
            raise ValueError("Discount percentage must be between 0 and 100.")

        self.price = self.price * (1 - percentage / 100)
        return self.price

    def display_info(self) -> None:
        print(f"Product: {self.name}")
        print(f"Price: ${self.price:,.2f}")


class SmartProduct(Product):
    """Inventory product with validated properties and computed read-only values."""

    MAX_QUANTITY = 10_000

    def __init__(self, name: str, price: float, quantity: int, category: str) -> None:
        super().__init__(name, price)
        self.__quantity = 0
        self.__category = ""
        self.quantity = quantity
        self.category = category

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("Quantity must be an integer.")
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        if value > self.MAX_QUANTITY:
            raise ValueError(f"Quantity cannot exceed {self.MAX_QUANTITY:,}.")
        self.__quantity = value

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Category must be a string.")
        if value not in VALID_CATEGORIES:
            choices = ", ".join(sorted(VALID_CATEGORIES))
            raise ValueError(f"Category must be one of: {choices}.")
        self.__category = value

    @property
    def total_value(self) -> float:
        """Read-only calculated value of all units currently in stock."""
        return self.price * self.quantity

    @property
    def is_expensive(self) -> bool:
        """Read-only indicator for products priced above $1,000."""
        return self.price > 1_000

    @property
    def stock_status(self) -> str:
        """Read-only stock level based on current quantity."""
        if self.quantity == 0:
            return "Out of Stock"
        if self.quantity < 10:
            return "Low Stock"
        if self.quantity < 50:
            return "Medium Stock"
        return "High Stock"

    def display_full_info(self) -> None:
        print("\n--- Product Information ---")
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Price: ${self.price:,.2f}")
        print(f"Quantity: {self.quantity}")
        print(f"Total inventory value: ${self.total_value:,.2f}")
        print(f"Stock status: {self.stock_status}")
        print(f"Expensive item: {'Yes' if self.is_expensive else 'No'}")

    def restock(self, amount: int) -> None:
        if isinstance(amount, bool) or not isinstance(amount, int):
            raise TypeError("Restock amount must be an integer.")
        if amount <= 0:
            raise ValueError("Restock amount must be positive.")
        self.quantity = self.quantity + amount
        print(f"Restocked {amount} units. New quantity: {self.quantity}")

    def sell(self, amount: int) -> float:
        if isinstance(amount, bool) or not isinstance(amount, int):
            raise TypeError("Sell amount must be an integer.")
        if amount <= 0:
            raise ValueError("Sell amount must be positive.")
        if amount > self.quantity:
            raise ValueError(
                f"Cannot sell {amount} units; only {self.quantity} available."
            )

        revenue = amount * self.price
        self.quantity = self.quantity - amount
        print(f"Sold {amount} units. Revenue: ${revenue:,.2f}")
        print(f"Remaining quantity: {self.quantity}")
        return revenue


def expect_error(label: str, operation, expected_exception: type[Exception]) -> None:
    """Run a validation check and report whether the expected error occurred."""
    try:
        operation()
    except expected_exception as error:
        print(f"PASS: {label} -> {error}")
    except Exception as error:
        print(f"FAIL: {label} raised the wrong error: {error}")
    else:
        print(f"FAIL: {label} was accepted but should have been rejected.")


def run_demo() -> None:
    print("=== Lab 42: Data Hiding with @property ===")

    # 1. Private attribute + property getter/setter
    laptop = Product("Gaming Laptop", 1_200)
    laptop.display_info()
    print(f"Read through property: ${laptop.price:,.2f}")

    try:
        print(laptop.__price)
    except AttributeError:
        print("Direct laptop.__price access is blocked, as expected.")

    # Name mangling exists, but bypassing it is not recommended.
    print(f"Name-mangled value (demonstration only): ${laptop._Product__price:,.2f}")

    # 2. Update a value through the validated setter and apply a discount.
    laptop.price = 1_350
    print(f"Updated price: ${laptop.price:,.2f}")
    laptop.apply_discount(15)
    print(f"Price after 15% discount: ${laptop.price:,.2f}")

    # 3. Multiple properties + computed read-only properties.
    stock = SmartProduct("Gaming Laptop", 1_500, 25, "Electronics")
    stock.display_full_info()
    stock.restock(20)
    stock.sell(15)
    stock.display_full_info()

    print("\n=== Validation checks ===")
    expect_error("Negative price", lambda: setattr(laptop, "price", -50), ValueError)
    expect_error("Text price", lambda: setattr(laptop, "price", "expensive"), TypeError)
    expect_error("Excessive price", lambda: setattr(laptop, "price", 150_000), ValueError)
    expect_error("Negative quantity", lambda: setattr(stock, "quantity", -5), ValueError)
    expect_error("Fractional quantity", lambda: setattr(stock, "quantity", 2.5), TypeError)
    expect_error("Invalid category", lambda: setattr(stock, "category", "Toys"), ValueError)
    expect_error("Sell more than stock", lambda: stock.sell(100_000), ValueError)
    expect_error("Invalid discount", lambda: laptop.apply_discount(150), ValueError)

    print("\n=== Multiple products ===")
    products = [
        SmartProduct("Smartphone", 800, 50, "Electronics"),
        SmartProduct("T-Shirt", 25, 100, "Clothing"),
        SmartProduct("Python Book", 45, 15, "Books"),
    ]
    for product in products:
        product.display_full_info()

    inventory_total = sum(product.total_value for product in products)
    print(f"\nTotal inventory value: ${inventory_total:,.2f}")
    print("\nLab demo complete.")


if __name__ == "__main__":
    run_demo()
