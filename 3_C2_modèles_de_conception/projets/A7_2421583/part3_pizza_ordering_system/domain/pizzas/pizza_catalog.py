from .pizza import Pizza
from .margherita_pizza import MargheritaPizza
from .pepperoni_pizza import PepperoniPizza
from .vegtarian_pizza import VegetarianPizza

class PizzaCatalog:

    _catalog = {
        "margherita": MargheritaPizza,
        "pepperoni": PepperoniPizza,
        "vegetarian": VegetarianPizza,
    }

    @classmethod
    def list_available_pizzas(cls) -> tuple[str, ...]:
        return tuple(cls._catalog.keys())

    @classmethod
    def get_pizza_type(cls, name: str) -> type[Pizza]:
        return cls._catalog[name]