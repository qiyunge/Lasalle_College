from __future__ import annotations

from application.builders import StoreBuilder
from domain import StoreOnline


class StoreDirector:
    def __init__(self, builder: StoreBuilder) -> None:
        self._builder = builder

    def set_builder(self, builder: StoreBuilder) -> None:
        self._builder = builder

    def construct_store_online(self) -> StoreOnline:
        self._builder.build_layout()
        self._builder.build_product_catalog()
        self._builder.build_shopping_cart()
        self._builder.build_payment_system()
        return self._builder.get_store_online()