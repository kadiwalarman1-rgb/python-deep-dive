from ...products.service import ProductService


class ProductEndpoint:
    def __init__(self, service=None):
        self.service = service or ProductService()

    @staticmethod
    def _serialize(product):
        return {
            "product_id": product.product_id,
            "name": product.name,
            "price": product.price,
            "category": product.category,
        }

    def list_products(self):
        return [self._serialize(product) for product in self.service.catalog.list_products()]

    def get_product(self, product_id):
        info = self.service.get_product_info(product_id)
        if info is None:
            return None
        return {
            "product": self._serialize(info["product"]),
            "stock_level": info["stock_level"],
            "in_stock": info["in_stock"],
            "category_path": info["category_path"],
        }

    def search_category(self, category_id):
        return [
            {
                "product": self._serialize(item["product"]),
                "stock_level": item["stock_level"],
                "in_stock": item["in_stock"],
                "category_path": item["category_path"],
            }
            for item in self.service.search_products_by_category(category_id)
        ]
