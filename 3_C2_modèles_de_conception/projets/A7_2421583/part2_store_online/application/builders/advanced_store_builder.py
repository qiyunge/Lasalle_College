from .store_builder import StoreBuilder

class AdvancedStoreBuilder(StoreBuilder):
    def build_layout(self) -> None:
        self._store_online.layout = "Advanced layout with multiple sections and categories"

    def build_product_catalog(self) -> None:
        self._store_online.product_catalog = ["Electronics", "Clothing", "Home Appliances", "Books"]

    def build_shopping_cart(self) -> None:
        self._store_online.shopping_cart = {"Electronics": 0, "Clothing": 0, "Home Appliances": 0, "Books": 0}

    def build_payment_system(self) -> None:
        self._store_online.payment_system = "Integrated payment system with multiple options"