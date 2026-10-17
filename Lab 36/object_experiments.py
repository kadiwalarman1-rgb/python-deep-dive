class Vehicle:
    def __init__(self, make, model, year, color="Unknown"):
        for field_name, field_value in (("make", make), ("model", model), ("color", color)):
            if not isinstance(field_value, str) or not field_value.strip():
                raise ValueError(f"{field_name.capitalize()} cannot be empty")
        if not isinstance(year, int) or isinstance(year, bool) or year < 1886:
            raise ValueError("Year must be a valid integer of 1886 or later")
        self.make = make.strip()
        self.model = model.strip()
        self.year = year
        self.color = color.strip()
        self.mileage = 0
        self.is_running = False

    def display_info(self):
        status = "Running" if self.is_running else "Stopped"
        print(f"{self.year} {self.make} {self.model} ({self.color})")
        print(f"Mileage: {self.mileage} miles - Status: {status}")

    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.make} {self.model} engine started!")
        else:
            print(f"{self.make} {self.model} is already running.")

    def stop_engine(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.make} {self.model} engine stopped.")
        else:
            print(f"{self.make} {self.model} is already stopped.")

    def drive(self, miles):
        if not isinstance(miles, (int, float)) or isinstance(miles, bool) or miles < 0:
            raise ValueError("Miles must be a non-negative number")
        if self.is_running:
            self.mileage += miles
            print(f"Drove {miles} miles. Total mileage: {self.mileage}")
            return True
        print("Cannot drive. Engine is not running!")
        return False

    def paint_vehicle(self, new_color):
        if not isinstance(new_color, str) or not new_color.strip():
            raise ValueError("Color cannot be empty")
        old_color = self.color
        self.color = new_color.strip()
        print(f"Vehicle painted from {old_color} to {self.color}")


if __name__ == "__main__":
    print("=== Vehicle Management Experiment ===\n")
    car1 = Vehicle("Toyota", "Camry", 2020, "Blue")
    car2 = Vehicle("Honda", "Civic", 2019, "Red")
    truck1 = Vehicle("Ford", "F-150", 2021, "Black")
    vehicles = [car1, car2, truck1]

    print("Initial Vehicle States:")
    for number, vehicle in enumerate(vehicles, 1):
        print(f"Vehicle {number}:")
        vehicle.display_info()
        print()

    print("=== Experiment 1: Starting and Driving ===")
    car1.start_engine()
    car1.drive(50)
    car1.drive(25)
    car2.drive(30)
    car2.start_engine()
    car2.drive(30)

    print("\n=== Experiment 2: Vehicle Modifications ===")
    car1.paint_vehicle("Silver")
    truck1.paint_vehicle("White")

    print("\n=== Experiment 3: Complex Operations ===")
    truck1.start_engine()
    truck1.drive(100)
    truck1.drive(75)
    truck1.stop_engine()
    truck1.drive(25)

    print("\n=== Final Vehicle States ===")
    for number, vehicle in enumerate(vehicles, 1):
        print(f"Vehicle {number}:")
        vehicle.display_info()
        print()

    print("=== Experiment 4: Dynamic Vehicle Creation ===")
    vehicle_data = [
        ("BMW", "X5", 2022, "White"),
        ("Mercedes", "C-Class", 2021, "Silver"),
        ("Audi", "A4", 2020, "Black"),
    ]
    dynamic_vehicles = [Vehicle(*data) for data in vehicle_data]
    for vehicle in dynamic_vehicles:
        print(f"Created: {vehicle.year} {vehicle.make} {vehicle.model}")

    print("\nOperating on dynamic vehicles:")
    for vehicle in dynamic_vehicles:
        vehicle.start_engine()
        vehicle.drive(20)
        vehicle.display_info()
        print()
