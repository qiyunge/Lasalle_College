from .pizza import Pizza

class PepperoniPizza(Pizza):

    def __init__(self):
        self.name = "Pepperoni"

    def prepare(self):
        print("Preparing Pepperoni Pizza ")

    def bake(self):
        print("Baking Pepperoni Pizza ")