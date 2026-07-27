from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, model: str, price: float, color:str):
        self.model = model
        self.price = price
        self.color = color

    @abstractmethod
    def manufacture(self):
        pass