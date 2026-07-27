from .pizza import Pizza

class MargheritaPizza(Pizza):

    def __init__(self):
        self.name = "Margherita"

    def prepare(self):
        print("Preparing Margherita Pizza ")

    def bake(self):
        print("Baking Margherita Pizza ")