from application import VehicleManufacturingSystem


def main():
    system = VehicleManufacturingSystem()
    

    # Example of manufacturing a vehicle
    vehicle_type = "moto"
    model = "Sedan"
    color = "Red"
    price = 25000.0
    engine_capacity = 1500
    system.manufacture_vehicle(vehicle_type, model, color, price, engine_capacity=engine_capacity)

if __name__ == "__main__":
    main()