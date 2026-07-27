from __future__ import annotations

from dataclasses import dataclass, field    

class StoreOnline:

    def __init__(self):
        self._layout = ""
        self._product_catalog = []
        self._shopping_cart ={}
        self._payment_system = ""

    @property
    def layout(self) -> str:
        return self._layout
    @layout.setter
    def layout(self, value: str) -> None:
        self._layout = value

    @property
    def product_catalog(self) -> list[str]:
        return self._product_catalog
    @product_catalog.setter
    def product_catalog(self, value: list[str]) -> None:
        self._product_catalog = value
        
    @property
    def shopping_cart(self) -> dict[str, int]:
        return self._shopping_cart
    @shopping_cart.setter
    def shopping_cart(self, value: dict[str, int]) -> None:
        self._shopping_cart = value

    @property
    def payment_system(self) -> str:
        return self._payment_system
    @payment_system.setter
    def payment_system(self, value: str) -> None:
        self._payment_system = value