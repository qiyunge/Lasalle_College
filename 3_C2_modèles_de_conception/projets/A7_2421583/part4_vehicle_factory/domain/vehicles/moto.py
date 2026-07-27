from .vehicle import Vehicle

class Motorcycle(Vehicle):

    def __init__(self, model: str, price: float, color:str, engine_capacity:int):
        super().__init__(model, price, color)
        self.engine_capacity = engine_capacity
        self.engine_capacity = engine_capacity if  engine_capacity else 500

    def manufacture(self):
        print(f"Manufacturing a {self.color} {self.model} motorcycle with {self.engine_capacity}cc engine at ${self.price}.")       