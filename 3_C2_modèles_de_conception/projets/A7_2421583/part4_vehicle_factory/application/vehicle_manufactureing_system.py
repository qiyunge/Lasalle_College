from domain.vehicles import VehicleCatalog
from domain.vehicles import VehicleFactory
from domain.vehicles import Vehicle

class VehicleManufacturingSystem:

    def list_available_vehicles(self)-> list[str]:
       print("Available vehicle types:")
       rst = VehicleCatalog.list_all_vehicles()
       print(rst)
       return rst

    def manufacture_vehicle(self, vehicle_type,model: str,color: str,price: float, **kwargs)->Vehicle|None:
        # This method would handle the manufacturing process of a vehicle
        try:
            vehicle = VehicleFactory.create_vehicle(vehicle_type, model, color, price, **kwargs)
            vehicle.manufacture()  
            print(f"Manufactured a new {vehicle_type}")
        except ValueError as e:
            print(e)
            return None
       
        return vehicle