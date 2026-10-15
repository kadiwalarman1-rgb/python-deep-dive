__version__ = "1.0.0"
__author__ = "Python Deep Dive learner"
__description__ = "A structured sample e-commerce system package"

from .products import Product, ProductCatalog, InventoryManager, ProductService
from .products.categories import Category, CategoryManager
from .users import User, AuthManager, Address, ProfileManager, UserProfile
from .orders import (
    Order, OrderItem, OrderManager, OrderStatus,
    Payment, PaymentMethod, PaymentProcessor, PaymentStatus,
)
from .utils import EcommerceLogger, JsonStore, validate_email, validate_password, validate_price
from .api import ProductEndpoint

__all__ = [
    "Product", "ProductCatalog", "InventoryManager", "ProductService",
    "Category", "CategoryManager", "User", "AuthManager", "Address",
    "ProfileManager", "UserProfile", "Order", "OrderItem", "OrderManager",
    "OrderStatus", "Payment", "PaymentMethod", "PaymentProcessor", "PaymentStatus",
    "EcommerceLogger", "JsonStore", "validate_email", "validate_password",
    "validate_price", "ProductEndpoint", "__version__", "__author__", "__description__",
]
