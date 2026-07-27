from .pizza import Pizza
from .pizza_catalog import PizzaCatalog   

class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type: str) -> Pizza:
        if pizza_type in PizzaCatalog.list_available_pizzas():
            return PizzaCatalog.get_pizza_type(pizza_type)()
        else:
            raise ValueError(f"Unknown pizza type: {pizza_type}")