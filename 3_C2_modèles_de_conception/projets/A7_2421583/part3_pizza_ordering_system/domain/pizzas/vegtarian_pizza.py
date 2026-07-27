from .pizza import Pizza

class VegetarianPizza(Pizza):

    def __init__(self):
        self.name = "Vegetarian Pizza"

    def prepare(self):
        print(f"Preparing {self.name}.")

    def bake(self):
        print(f"Baking {self.name}.")