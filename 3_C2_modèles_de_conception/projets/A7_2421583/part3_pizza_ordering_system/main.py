
from application import OnlinePizzaOrderingSystem

def main():
    system = OnlinePizzaOrderingSystem()
    available_pizzas = system.list_available_pizzas()
    print("Available pizzas:", available_pizzas)

    # Order a pizza
    for pizza_name in available_pizzas:
        try:
            print(f"Ordered pizza: {pizza_name}")
            pizza = system.order_pizza(pizza_name)
            print("** Pizza ordered successfully! ***")
            
        except ValueError as e:
            print(f"Sorry, {e}")

if __name__ == "__main__":
    main()