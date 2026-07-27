from .car import Car
from .bike import Bicycle
from .moto import Motorcycle
from .vehicle import Vehicle

class VehicleCatalog:

    _vehicles: dict[str, type[Vehicle]] = {
        "car": Car,
        "bike": Bicycle,
        "moto": Motorcycle
    }

    @classmethod
    def list_all_vehicles(cls)-> list[str]:
        return list(cls._vehicles.keys())

    @classmethod
    def get_vehicle_type(cls, vehicle_type: str)-> type[Vehicle] |None:
        return cls._vehicles.get(vehicle_type)