from .catalog import Product, ProductCatalog
from .inventory import InventoryManager
from .categories.manager import CategoryManager
from ..utils.validators import validate_price
from ..utils.logger import EcommerceLogger


class ProductService:
    def __init__(self, logger=None):
        self.catalog = ProductCatalog()
        self.inventory = InventoryManager()
        self.category_manager = CategoryManager()
        self.logger = logger or EcommerceLogger("ProductService")

    def setup_categories(self):
        self.category_manager.create_category(1, "Electronics")
        self.category_manager.create_category(2, "Clothing")
        self.category_manager.create_category(3, "Books")
        self.category_manager.create_category(11, "Computers", 1)
        self.category_manager.create_category(12, "Mobile Phones", 1)
        self.category_manager.create_category(21, "Men's Clothing", 2)
        self.category_manager.create_category(22, "Women's Clothing", 2)
        self.logger.info("Product categories set up successfully")

    def add_product_with_validation(self, product_id, name, price, category_id, initial_stock=0):
        is_valid, message = validate_price(price)
        if not is_valid:
            self.logger.error(f"Invalid price for product {name}: {message}")
            return False, message
        if not isinstance(initial_stock, int) or isinstance(initial_stock, bool) or initial_stock < 0:
            return False, "Initial stock must be a non-negative integer"
        category_path = self.category_manager.get_category_path(category_id)
        if not category_path:
            self.logger.error(f"Invalid category ID: {category_id}")
            return False, "Invalid category"
        try:
            product = Product(product_id, name, float(price), category_path)
            self.catalog.add_product(product)
            if initial_stock > 0:
                self.inventory.add_stock(product_id, initial_stock)
        except (TypeError, ValueError) as error:
            self.logger.error(str(error))
            return False, str(error)
        self.logger.info(f"Product added: {product} with stock: {initial_stock}")
        return True, "Product added successfully"

    def get_product_info(self, product_id):
        product = self.catalog.get_product(product_id)
        if product is None:
            return None
        stock_level = self.inventory.check_stock(product_id)
        return {
            "product": product,
            "stock_level": stock_level,
            "in_stock": stock_level > 0,
            "category_path": product.category,
        }

    def search_products_by_category(self, category_id):
        category_path = self.category_manager.get_category_path(category_id)
        if not category_path:
            return []
        products = [
            product for product in self.catalog.list_products()
            if product.category == category_path
            or product.category.startswith(category_path + " > ")
        ]
        results = []
        for product in products:
            results.append({
                "product": product,
                "stock_level": self.inventory.check_stock(product.product_id),
                "in_stock": self.inventory.is_in_stock(product.product_id),
                "category_path": product.category,
            })
        return results
