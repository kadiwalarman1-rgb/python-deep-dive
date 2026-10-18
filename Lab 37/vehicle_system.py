"""Vehicle constructor, engine, driving, fuel, and maintenance examples."""


class Vehicle:
    """Represent a vehicle with default mileage and operating state."""

    def __init__(self, make, model, year, color, mileage=0):
        for label, value in (("Make", make), ("Model", model), ("Color", color)):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{label} cannot be empty")
        if not isinstance(year, int) or isinstance(year, bool) or year <= 0:
            raise ValueError("Year must be a positive integer")
        if isinstance(mileage, bool) or not isinstance(mileage, (int, float)) or mileage < 0:
            raise ValueError("Mileage must be non-negative")
        self.make = make.strip()
        self.model = model.strip()
        self.year = year
        self.color = color.strip()
        self.mileage = mileage
        self.is_running = False
        self.fuel_level = 100.0
        self.maintenance_records = []

    def start_engine(self):
        """Start engine unless it is already on."""
        if self.is_running:
            return f"{self.year} {self.make} {self.model} is already running"
        self.is_running = True
        return f"{self.year} {self.make} {self.model} engine started!"

    def stop_engine(self):
        """Stop engine unless it is already off."""
        if not self.is_running:
            return f"{self.year} {self.make} {self.model} engine is already off"
        self.is_running = False
        return f"{self.year} {self.make} {self.model} engine stopped"

    def drive(self, miles):
        """Drive a positive distance while the engine is on and fuel remains."""
        if isinstance(miles, bool) or not isinstance(miles, (int, float)) or miles <= 0:
            return "Distance must be a positive number"
        if not self.is_running:
            return "Cannot drive. Engine is not running!"
        if self.fuel_level <= 0:
            return "Cannot drive. Out of fuel!"
        fuel_consumed = miles * 0.05
        if fuel_consumed > self.fuel_level:
            max_distance = self.fuel_level / 0.05
            return f"Insufficient fuel. Maximum possible distance is {max_distance:.1f} miles"
        self.mileage += miles
        self.fuel_level = max(0.0, self.fuel_level - fuel_consumed)
        return f"Drove {miles:g} miles. Total mileage: {self.mileage:g}. Fuel: {self.fuel_level:.1f}%"

    def refuel(self):
        """Refill the vehicle to 100 percent."""
        self.fuel_level = 100.0
        return f"{self.year} {self.make} {self.model} refueled to 100%"

    def add_maintenance_record(self, service_type, service_date, cost):
        """Record a service and its non-negative cost."""
        if not isinstance(service_type, str) or not service_type.strip():
            raise ValueError("Service type cannot be empty")
        if not isinstance(service_date, str) or not service_date.strip():
            raise ValueError("Service date cannot be empty")
        if isinstance(cost, bool) or not isinstance(cost, (int, float)) or cost < 0:
            raise ValueError("Maintenance cost must be non-negative")
        self.maintenance_records.append({
            "service": service_type.strip(),
            "date": service_date.strip(),
            "cost": float(cost),
        })

    def display_vehicle_info(self):
        """Print vehicle details and maintenance costs."""
        print("=" * 50)
        print("VEHICLE INFORMATION")
        print("=" * 50)
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Mileage: {self.mileage:,.1f} miles")
        print(f"Engine Status: {'Running' if self.is_running else 'Off'}")
        print(f"Fuel Level: {self.fuel_level:.1f}%")
        if self.maintenance_records:
            print("\nMAINTENANCE RECORDS:")
            total_cost = 0.0
            for record in self.maintenance_records:
                print(f"- {record['service']} - {record['date']} - USD {record['cost']:.2f}")
                total_cost += record["cost"]
            print(f"Total Maintenance Cost: USD {total_cost:.2f}")
        else:
            print("\nNo maintenance records available")
        print("=" * 50)


def create_vehicle_fleet():
    """Create several vehicles with varied constructor arguments."""
    vehicles = [
        Vehicle("Toyota", "Camry", 2022, "Silver", 15000),
        Vehicle("Honda", "Civic", 2021, "Blue", 22000),
        Vehicle("Ford", "F-150", 2023, "Red", 8000),
        Vehicle("Tesla", "Model 3", 2023, "White", 5000),
        Vehicle("BMW", "X5", 2020, "Black", 35000),
        Vehicle("Chevrolet", "Malibu", 2019, "Gray", 45000),
        Vehicle("Toyota", "Corolla", 2024, "White"),
    ]
    vehicles[0].add_maintenance_record("Oil Change", "2023-01-15", 45.99)
    vehicles[0].add_maintenance_record("Tire Rotation", "2023-03-20", 25.00)
    vehicles[0].add_maintenance_record("Brake Inspection", "2023-06-10", 89.50)
    vehicles[1].add_maintenance_record("Oil Change", "2023-02-10", 42.99)
    vehicles[1].add_maintenance_record("Air Filter Replacement", "2023-04-15", 35.00)
    vehicles[4].add_maintenance_record("Premium Service", "2023-01-20", 299.99)
    vehicles[4].add_maintenance_record("Brake Pad Replacement", "2023-05-15", 450.00)
    return vehicles


def demo_vehicles():
    """Run the fleet and vehicle-operation examples."""
    fleet = create_vehicle_fleet()
    print(f"Fleet created with {len(fleet)} vehicles\n")
    for index, vehicle in enumerate(fleet, 1):
        print(f"VEHICLE #{index}")
        vehicle.display_vehicle_info()
        print()
    print("VEHICLE OPERATIONS DEMONSTRATION")
    vehicle = fleet[0]
    print(f"Testing with: {vehicle.year} {vehicle.make} {vehicle.model}")
    for operation in (
        vehicle.start_engine(),
        vehicle.drive(50),
        vehicle.drive(100),
        vehicle.refuel(),
        vehicle.drive(200),
        vehicle.stop_engine(),
    ):
        print(f"- {operation}")
    print(f"\nFinal mileage: {vehicle.mileage:,.1f} miles")
    print(f"Fuel level: {vehicle.fuel_level:.1f}%")
    print(f"Engine: {'Running' if vehicle.is_running else 'Off'}")


if __name__ == "__main__":
    demo_vehicles()
