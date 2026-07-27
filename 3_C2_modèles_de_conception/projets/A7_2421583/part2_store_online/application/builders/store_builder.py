from __future__ import annotations

from abc import ABC, abstractmethod
from domain import StoreOnline

class StoreBuilder(ABC):
    def __init__(self) -> None:
        self._store_online: StoreOnline = StoreOnline()

    @abstractmethod
    def build_layout(self) -> None:
        pass

    @abstractmethod
    def build_product_catalog(self) -> None:
        pass

    @abstractmethod
    def build_shopping_cart(self) -> None:
        pass

    @abstractmethod
    def build_payment_system(self) -> None:
        pass

    def get_store_online(self) -> StoreOnline:
        return self._store_online
