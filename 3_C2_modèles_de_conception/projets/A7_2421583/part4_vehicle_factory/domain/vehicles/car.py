from .vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, model: str, price: float, color:str,doors:int):
        super().__init__(model, price, color)
        self.doors = doors
        self.doors = doors if  doors else 4

    def manufacture(self):
        print(f"Manufacturing a {self.color} {self.model} car with {self.doors} doors at ${self.price}.")