from .vehicle import Vehicle

class Bicycle(Vehicle):
    def __init__(self, model: str, price: float, color:str, frame_type:str):
        super().__init__(model, price, color)
        self.frame_type =  frame_type if  frame_type else "Standard"

    def manufacture(self):
        print(f"Manufacturing a {self.color} {self.model} bicycle with a {self.frame_type} frame priced at ${self.price}.")