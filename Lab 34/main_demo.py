from ecommerce import (
    Address, AuthManager, EcommerceLogger, JsonStore, OrderManager,
    OrderStatus, PaymentMethod, PaymentProcessor, ProductEndpoint,
    ProductService, ProfileManager, validate_email, validate_password,
)


def main():
    logger = EcommerceLogger("EcommerceDemo")
    logger.info("Starting e-commerce package demonstration")

    service = ProductService(logger=logger)
    service.setup_categories()
    service.add_product_with_validation(1, "Gaming Laptop", 1299.99, 11, 10)
    service.add_product_with_validation(2, "Wireless Mouse", 29.99, 1, 50)
    service.add_product_with_validation(3, "Python Handbook", 34.50, 3, 20)
    service.add_product_with_validation(4, "Mobile Phone", 799.00, 12, 15)

    endpoint = ProductEndpoint(service)
    print("=== Product catalog ===")
    for product in endpoint.list_products():
        print(product)
    print("Electronics category search:", endpoint.search_category(1))

    print("\n=== User authentication ===")
    auth = AuthManager()
    user = auth.register_user("john_doe", "john@example.com", "SecurePass123")
    token = auth.authenticate("john_doe", "SecurePass123")
    print("Registered user:", user.username)
    print("Authentication successful:", token is not None)
    print("Wrong password rejected:", auth.authenticate("john_doe", "wrong-password") is None)

    profiles = ProfileManager()
    profile = profiles.create_profile(user.user_id)
    profile.first_name = "John"
    profile.last_name = "Doe"
    profile.add_address(Address("12 Sample Road", "Surat", "Gujarat", "395001", "India"))
    profile.set_preference("newsletter", True)
    print("Profile name:", profile.get_full_name())
    print("Address:", profile.addresses[0])

    print("\n=== Order and simulated payment ===")
    orders = OrderManager()
    order = orders.create_order(user.user_id)
    laptop = service.catalog.get_product(1)
    mouse = service.catalog.get_product(2)
    order.add_item(laptop.product_id, 1, laptop.price)
    order.add_item(mouse.product_id, 2, mouse.price)
    service.inventory.remove_stock(laptop.product_id, 1)
    service.inventory.remove_stock(mouse.product_id, 2)
    order.update_status(OrderStatus.CONFIRMED)

    payments = PaymentProcessor()
    payment = payments.create_payment(order.order_id, order.total_amount, PaymentMethod.CREDIT_CARD)
    payments.process_payment(payment.payment_id)
    print(f"Order #{order.order_id} total: {order.total_amount:.2f} USD")
    print("Order status:", order.status.value)
    print("Simulated payment status:", payment.status.value)

    print("\n=== Validation ===")
    print("Email valid:", validate_email("learner@example.com"))
    print("Password check:", validate_password("SecurePass123"))
    store = JsonStore("lab34_output/sample_export.json")
    store.save({"user": user.username, "order_id": order.order_id, "order_total": order.total_amount})
    print("JSON store saved and loaded:", store.load())
    print("Demo completed successfully.")


if __name__ == "__main__":
    main()
