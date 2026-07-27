from copy import deepcopy

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return f"Product(name={self.name}, price={self.price})"