#!/usr/bin/env python3
"""Lab 46: Composition example using Engine and Car classes."""

class Engine:
    """An engine component owned by a Car object (has-a relationship)."""
    def __init__(self, engine_type, horsepower, fuel_type):
        if not engine_type:
            raise ValueError("Engine type cannot be empty.")
        if isinstance(horsepower, bool) or not isinstance(horsepower, (int, float)) or horsepower <= 0:
            raise ValueError("Horsepower must be a positive number.")
        if not fuel_type:
            raise ValueError("Fuel type cannot be empty.")
        self.engine_type = engine_type
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.is_running = False
        self.temperature = 20

    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            self.temperature = 90
            print(f"{self.engine_type} engine started! Temperature: {self.temperature}°C")
        else:
            print("Engine is already running!")

    def stop_engine(self):
        if self.is_running:
            self.is_running = False
            self.temperature = 20
            print(f"{self.engine_type} engine stopped. Cooling down to {self.temperature}°C")
        else:
            print("Engine is already stopped!")

    def get_engine_info(self):
        status = "Running" if self.is_running else "Stopped"
        return f"{self.engine_type} Engine - {self.horsepower}HP, Fuel: {self.fuel_type}, Status: {status}"

    def accelerate(self):
        if self.is_running:
            print(f"{self.engine_type} engine accelerating! Power output increased.")
        else:
            print("Cannot accelerate - engine is not running!")


class Car:
    """Car uses composition by containing an Engine instance."""
    def __init__(self, make, model, year, engine_type, horsepower, fuel_type):
        if not make or not model:
            raise ValueError("Car make and model cannot be empty.")
        self.make = make
        self.model = model
        self.year = int(year)
        self.engine = Engine(engine_type, horsepower, fuel_type)
        self.speed = 0
        self.gear = 0
        self.is_moving = False

    def start_car(self):
        print(f"Starting {self.year} {self.make} {self.model}...")
        self.engine.start_engine()
        if self.engine.is_running:
            print("Car is ready to drive!")

    def stop_car(self):
        print(f"Stopping {self.year} {self.make} {self.model}...")
        self.speed = 0
        self.gear = 0
        self.is_moving = False
        self.engine.stop_engine()
        print("Car has been stopped.")

    def accelerate(self, speed_increase):
        if isinstance(speed_increase, bool) or not isinstance(speed_increase, (int, float)) or speed_increase < 0:
            raise ValueError("Speed increase must be a non-negative number.")
        if self.engine.is_running:
            self.engine.accelerate()
            self.speed += speed_increase
            self.is_moving = self.speed > 0
            print(f"Car accelerated! Current speed: {self.speed} mph")
        else:
            print("Cannot accelerate - start the engine first!")

    def brake(self, speed_decrease):
        if isinstance(speed_decrease, bool) or not isinstance(speed_decrease, (int, float)) or speed_decrease < 0:
            raise ValueError("Speed decrease must be a non-negative number.")
        if self.speed > 0:
            self.speed = max(0, self.speed - speed_decrease)
            print(f"Braking applied! Current speed: {self.speed} mph")
            if self.speed == 0:
                self.is_moving = False
                print("Car has come to a complete stop.")
        else:
            print("Car is already stopped!")

    def shift_gear(self, new_gear):
        if isinstance(new_gear, bool) or not isinstance(new_gear, int) or new_gear < 0:
            raise ValueError("Gear must be a non-negative integer.")
        if self.engine.is_running:
            self.gear = new_gear
            print(f"Shifted to gear {self.gear}")
        else:
            print("Cannot shift gear - engine is not running!")

    def get_car_status(self):
        moving = "Yes" if self.is_moving else "No"
        return (
            f"\n=== {self.year} {self.make} {self.model} Status ===\n"
            f"{self.engine.get_engine_info()}\nSpeed: {self.speed} mph\n"
            f"Gear: {self.gear}\nMoving: {moving}"
        )

    def honk(self):
        print(f"{self.make} {self.model}: BEEP BEEP!")


def demonstrate_composition():
    print("=" * 50)
    print("COMPOSITION DEMONSTRATION")
    print("=" * 50)
    car = Car("Toyota", "Camry", 2023, "V6", 301, "Gasoline")
    print("1. Initial car status:")
    print(car.get_car_status())
    print("\n2. Starting the car:")
    car.start_car()
    print("\n3. Car status after starting:")
    print(car.get_car_status())
    print("\n4. Driving simulation:")
    for gear, acceleration in [(1, 20), (2, 15), (3, 25)]:
        car.shift_gear(gear)
        car.accelerate(acceleration)
    print("\n5. Current driving status:")
    print(car.get_car_status())
    print("\n6. Slowing down:")
    car.brake(30)
    car.brake(30)
    print("\n7. Honking horn:")
    car.honk()
    print("\n8. Stopping the car:")
    car.stop_car()
    print("\n9. Final status:")
    print(car.get_car_status())


def demonstrate_direct_engine_access():
    print("\n" + "=" * 50)
    print("DIRECT ENGINE ACCESS DEMONSTRATION")
    print("=" * 50)
    car = Car("Ferrari", "488 GTB", 2022, "V8 Twin-Turbo", 661, "Premium Gasoline")
    print("1. Accessing engine information directly:")
    print(car.engine.get_engine_info())
    print("\n2. Starting engine directly:")
    car.engine.start_engine()
    print("\n3. Direct engine acceleration:")
    car.engine.accelerate()
    print("\n4. Engine temperature check:")
    print(f"Engine temperature: {car.engine.temperature}°C")
    print("\n5. Stopping engine directly:")
    car.engine.stop_engine()


if __name__ == "__main__":
    demonstrate_composition()
    demonstrate_direct_engine_access()
