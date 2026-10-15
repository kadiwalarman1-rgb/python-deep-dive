class Product:
    def __init__(self, product_id, name, price, category):
        if not isinstance(product_id, int) or product_id <= 0:
            raise ValueError("Product ID must be a positive integer")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name cannot be empty")
        if not isinstance(price, (int, float)) or isinstance(price, bool) or price <= 0:
            raise ValueError("Product price must be a positive number")
        if not isinstance(category, str) or not category.strip():
            raise ValueError("Product category cannot be empty")
        self.product_id = product_id
        self.name = name.strip()
        self.price = float(price)
        self.category = category.strip()
        self.in_stock = True

    def __str__(self):
        return f"Product({self.product_id}: {self.name} - {self.price:.2f} USD)"

    def update_price(self, new_price):
        if not isinstance(new_price, (int, float)) or isinstance(new_price, bool) or new_price <= 0:
            return False
        self.price = float(new_price)
        return True


class ProductCatalog:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("product must be a Product instance")
        if product.product_id in self.products:
            raise ValueError(f"Product ID {product.product_id} already exists")
        self.products[product.product_id] = product
        return product

    def get_product(self, product_id):
        return self.products.get(product_id)

    def remove_product(self, product_id):
        return self.products.pop(product_id, None)

    def list_products(self):
        return list(self.products.values())

    def search_by_category(self, category):
        search_key = category.casefold()
        return [
            product for product in self.products.values()
            if product.category.casefold() == search_key
        ]
