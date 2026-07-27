from __future__ import annotations

from .store_builder import StoreBuilder

class BasicStoreBuilder(StoreBuilder):
    def build_layout(self) -> None:
        self._store_online.layout = "Basic Layout"

    def build_product_catalog(self) -> None:
        self._store_online.product_catalog = ["Product A", "Product B", "Product C"]

    def build_shopping_cart(self) -> None:
        self._store_online.shopping_cart = "Basic Shopping Cart"

    def build_shopping_cart(self) -> None:
        self._store_online.shopping_cart = {"Product A": 0, "Product B": 0, "Product C": 0}

    def build_payment_system(self) -> None:
        self._store_online.payment_system = "Basic Payment System"