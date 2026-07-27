from .product import Product

class ProductCatalog:

    _products ={}

    @classmethod
    def load_catalog(cls):
        cls._products = {
            "p1": Product("Laptop", 999.99),
            "p2": Product("Smartphone", 499.99),
            "p3": Product("Tablet", 299.99)
        }

    @classmethod
    def get_product(cls, product_id):
        product = cls._products.get(product_id)
        if product is None:
            raise ValueError(f"Product with ID '{product_id}' not found in the catalog.")
        return product.clone()
            

    def __str__(self):
        return f"ProductCatalog(products={self.products})"