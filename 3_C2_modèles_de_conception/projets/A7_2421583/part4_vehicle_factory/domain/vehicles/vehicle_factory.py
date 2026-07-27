from .vehicle_catalog import VehicleCatalog
from .vehicle import Vehicle

class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type, model: str, color: str, price: float, **kwargs)-> Vehicle:
       vehicle_class = VehicleCatalog.get_vehicle_type(vehicle_type)
       if vehicle_class is None:
           raise ValueError(f"Vehicle type '{vehicle_type}' is not recognized.")

       return vehicle_class(model=model, color=color, price=price, **kwargs)