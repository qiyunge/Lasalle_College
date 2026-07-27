from domain.pizzas import Pizza, PizzaFactory,  PizzaCatalog

class OnlinePizzaOrderingSystem:

    def list_available_pizzas(self)-> tuple[str, ...]:
        """
        Lists all available pizzas.
        """
        return PizzaCatalog.list_available_pizzas()
    
    def order_pizza(self, pizza_name: str)-> Pizza:
        """
        Orders a pizza by name.
        """
        pizza = PizzaFactory.create_pizza(pizza_name)
        if pizza is None:
            raise ValueError(f"Pizza '{pizza_name}' is not available.")

        pizza.prepare()
        pizza.bake()
        return pizza
