import tempfile
import unittest
from pathlib import Path

from ecommerce import (
    Address, AuthManager, InventoryManager, JsonStore, OrderManager,
    OrderStatus, PaymentMethod, PaymentProcessor, Product, ProductCatalog,
    ProductEndpoint, ProductService, ProfileManager, validate_email,
    validate_password, validate_price,
)


class EcommercePackageTests(unittest.TestCase):
    def test_product_catalog_and_inventory(self):
        catalog = ProductCatalog()
        product = Product(1, "Keyboard", 25.0, "Electronics")
        catalog.add_product(product)
        self.assertIs(catalog.get_product(1), product)
        self.assertEqual(len(catalog.search_by_category("electronics")), 1)
        with self.assertRaises(ValueError):
            catalog.add_product(product)
        inventory = InventoryManager()
        inventory.add_stock(1, 5)
        self.assertTrue(inventory.remove_stock(1, 2))
        self.assertEqual(inventory.check_stock(1), 3)
        self.assertFalse(inventory.remove_stock(1, 4))

    def test_categories_service_and_endpoint(self):
        service = ProductService()
        service.setup_categories()
        ok, _ = service.add_product_with_validation(1, "Laptop", 999, 11, 4)
        self.assertTrue(ok)
        result = service.search_products_by_category(1)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["stock_level"], 4)
        endpoint = ProductEndpoint(service)
        self.assertEqual(endpoint.get_product(1)["product"]["name"], "Laptop")
        self.assertFalse(service.add_product_with_validation(2, "Bad Price", -1, 1)[0])
        self.assertFalse(service.add_product_with_validation(3, "Bad Category", 10, 999)[0])

    def test_auth_and_validation(self):
        manager = AuthManager()
        user = manager.register_user("learner", "learner@example.com", "SecurePass123")
        token = manager.authenticate("learner", "SecurePass123")
        self.assertIsNotNone(token)
        self.assertIs(manager.get_user_by_token(token), user)
        self.assertIsNone(manager.authenticate("learner", "incorrect"))
        self.assertTrue(manager.logout(token))
        self.assertTrue(validate_email("hello@example.org"))
        self.assertFalse(validate_email("bad-email"))
        self.assertTrue(validate_password("StrongPass123")[0])
        self.assertTrue(validate_price("5.25")[0])
        self.assertFalse(validate_price("0")[0])

    def test_orders_payments_and_profiles(self):
        orders = OrderManager()
        order = orders.create_order(1)
        order.add_item(10, 2, 4.5)
        self.assertEqual(order.total_amount, 9.0)
        order.update_status(OrderStatus.CONFIRMED)
        self.assertEqual(order.status, OrderStatus.CONFIRMED)
        payments = PaymentProcessor()
        payment = payments.create_payment(order.order_id, order.total_amount, PaymentMethod.PAYPAL)
        self.assertTrue(payments.process_payment(payment.payment_id))
        self.assertEqual(payments.get_payment(payment.payment_id).status.value, "completed")
        profiles = ProfileManager()
        profile = profiles.create_profile(1)
        profile.first_name = "Alex"
        profile.last_name = "Patel"
        profile.add_address(Address("Main Road", "Surat", "Gujarat", "395001", "India"))
        self.assertEqual(profile.get_full_name(), "Alex Patel")

    def test_json_store(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "nested" / "data.json"
            store = JsonStore(path)
            self.assertEqual(store.load(default={}), {})
            data = {"ok": True, "items": [1, 2, 3]}
            store.save(data)
            self.assertEqual(store.load(), data)

    def test_nested_package_imports(self):
        from ecommerce.products.categories import Category
        from ecommerce.orders.payment import PaymentStatus
        from ecommerce.users.profiles import UserProfile
        from ecommerce.api.endpoints import ProductEndpoint as Endpoint
        self.assertEqual(Category(1, "Root").name, "Root")
        self.assertEqual(PaymentStatus.PENDING.value, "pending")
        self.assertEqual(UserProfile(4).user_id, 4)
        self.assertTrue(Endpoint)


if __name__ == "__main__":
    unittest.main(verbosity=2)
