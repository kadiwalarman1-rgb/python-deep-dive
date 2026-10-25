#!/usr/bin/env python3
"""Lab 46: Inheritance examples using Vehicle, ElectricCar, and GasCar."""

class Vehicle:
    """Base vehicle class shared by specialized vehicle types."""
    def __init__(self, make, model, year):
        if not make or not model:
            raise ValueError("Vehicle make and model cannot be empty.")
        self.make = make
        self.model = model
        self.year = int(year)
        self.speed = 0
        self.is_moving = False

    def start(self):
        print(f"Starting {self.year} {self.make} {self.model}...")
        print("Vehicle is ready!")

    def stop(self):
        print(f"Stopping {self.year} {self.make} {self.model}...")
        self.speed = 0
        self.is_moving = False
        print("Vehicle has stopped.")

    def accelerate(self, speed_increase):
        if isinstance(speed_increase, bool) or not isinstance(speed_increase, (int, float)) or speed_increase < 0:
            raise ValueError("Speed increase must be a non-negative number.")
        self.speed += speed_increase
        self.is_moving = self.speed > 0
        print(f"Vehicle accelerated! Current speed: {self.speed} mph")

    def brake(self, speed_decrease):
        if isinstance(speed_decrease, bool) or not isinstance(speed_decrease, (int, float)) or speed_decrease < 0:
            raise ValueError("Speed decrease must be a non-negative number.")
        self.speed = max(0, self.speed - speed_decrease)
        self.is_moving = self.speed > 0
        print(f"Braking applied! Current speed: {self.speed} mph")

    def get_vehicle_info(self):
        return f"{self.year} {self.make} {self.model} - Speed: {self.speed} mph"

    def honk(self):
        print(f"{self.make} {self.model}: HONK HONK!")


class ElectricCar(Vehicle):
    """Electric car inherits shared vehicle behavior and adds battery features."""
    def __init__(self, make, model, year, battery_capacity, range_miles):
        super().__init__(make, model, year)
        if battery_capacity <= 0 or range_miles <= 0:
            raise ValueError("Battery capacity and range must be positive.")
        self.battery_capacity = float(battery_capacity)
        self.current_charge = float(battery_capacity)
        self.range_miles = float(range_miles)
        self.is_charging = False
        self.regenerative_braking = True

    def start(self):
        print(f"Powering on {self.year} {self.make} {self.model}...")
        if self.current_charge > 0:
            print("Electric motor activated! Ready to drive silently.")
        else:
            print("Battery depleted! Please charge the vehicle.")

    def stop(self):
        print(f"Powering down {self.year} {self.make} {self.model}...")
        super().stop()
        print("Electric motor deactivated.")

    def accelerate(self, speed_increase):
        if self.current_charge > 0:
            super().accelerate(speed_increase)
            consumption = speed_increase * 0.1
            self.current_charge = max(0, self.current_charge - consumption)
            print(f"Battery level: {self.current_charge:.1f} kWh")
        else:
            print("Cannot accelerate - battery is depleted!")

    def brake(self, speed_decrease):
        super().brake(speed_decrease)
        if self.regenerative_braking and self.speed > 0:
            regen_charge = speed_decrease * 0.05
            self.current_charge = min(self.battery_capacity, self.current_charge + regen_charge)
            print(f"Regenerative braking activated! Battery level: {self.current_charge:.1f} kWh")

    def charge_battery(self, charge_amount):
        if isinstance(charge_amount, bool) or not isinstance(charge_amount, (int, float)) or charge_amount < 0:
            raise ValueError("Charge amount must be a non-negative number.")
        if not self.is_charging:
            self.is_charging = True
            print(f"Charging {self.make} {self.model}...")
        self.current_charge = min(self.battery_capacity, self.current_charge + charge_amount)
        print(f"Battery charged to {self.current_charge:.1f} kWh")
        if self.current_charge >= self.battery_capacity:
            print("Battery fully charged!")
            self.is_charging = False

    def get_electric_info(self):
        percent = (self.current_charge / self.battery_capacity) * 100
        estimated_range = percent / 100 * self.range_miles
        return (
            f"{self.get_vehicle_info()}\n"
            f"Battery: {self.current_charge:.1f}/{self.battery_capacity:.1f} kWh ({percent:.1f}%)\n"
            f"Estimated Range: {estimated_range:.0f} miles\n"
            f"Charging: {'Yes' if self.is_charging else 'No'}\n"
            f"Regenerative Braking: {'Enabled' if self.regenerative_braking else 'Disabled'}"
        )

    def honk(self):
        print(f"{self.make} {self.model}: *quiet beep beep*")


class GasCar(Vehicle):
    """Gas car inherits vehicle behavior and tracks fuel usage."""
    def __init__(self, make, model, year, engine_type, mpg):
        super().__init__(make, model, year)
        if not engine_type or mpg <= 0:
            raise ValueError("Engine type must be provided and MPG must be positive.")
        self.engine_type = engine_type
        self.mpg = mpg
        self.fuel_level = 100.0
        self.engine_running = False

    def start(self):
        print(f"Starting {self.year} {self.make} {self.model}...")
        if self.fuel_level > 0:
            self.engine_running = True
            print(f"{self.engine_type} engine started! *vroom vroom*")
        else:
            print("Out of fuel! Please refuel the vehicle.")

    def stop(self):
        print(f"Stopping {self.year} {self.make} {self.model}...")
        self.engine_running = False
        super().stop()
        print("Engine turned off.")

    def accelerate(self, speed_increase):
        if self.fuel_level > 0 and self.engine_running:
            super().accelerate(speed_increase)
            self.fuel_level = max(0, self.fuel_level - speed_increase * 0.2)
            print(f"Fuel level: {self.fuel_level:.1f}%")
        else:
            print("Cannot accelerate - check fuel and engine status!")

    def refuel(self, fuel_amount):
        if isinstance(fuel_amount, bool) or not isinstance(fuel_amount, (int, float)) or fuel_amount < 0:
            raise ValueError("Fuel amount must be a non-negative number.")
        self.fuel_level = min(100, self.fuel_level + fuel_amount)
        print(f"Refueled! Fuel level: {self.fuel_level:.1f}%")

    def get_gas_info(self):
        return (
            f"{self.get_vehicle_info()}\nEngine: {self.engine_type}\n"
            f"Fuel Level: {self.fuel_level:.1f}%\nMPG: {self.mpg}\n"
            f"Engine Running: {'Yes' if self.engine_running else 'No'}"
        )


def demonstrate_inheritance():
    print("=" * 50)
    print("INHERITANCE DEMONSTRATION")
    print("=" * 50)
    tesla = ElectricCar("Tesla", "Model S", 2023, 100, 405)
    print("1. Electric Car Information:")
    print(tesla.get_electric_info())
    print("\n2. Starting electric car:")
    tesla.start()
    print("\n3. Driving electric car:")
    tesla.accelerate(30)
    tesla.accelerate(20)
    tesla.brake(15)
    print("\n4. Electric car status after driving:")
    print(tesla.get_electric_info())
    print("\n5. Charging the electric car:")
    tesla.charge_battery(5)
    print("\n6. Electric car horn:")
    tesla.honk()
    print("\n7. Stopping electric car:")
    tesla.stop()

    print("\n" + "=" * 30 + "\nGAS CAR COMPARISON\n" + "=" * 30)
    honda = GasCar("Honda", "Civic", 2023, "4-Cylinder", 32)
    print("\n8. Gas Car Information:")
    print(honda.get_gas_info())
    print("\n9. Starting gas car:")
    honda.start()
    print("\n10. Driving gas car:")
    honda.accelerate(30)
    honda.accelerate(20)
    honda.brake(15)
    print("\n11. Gas car status after driving:")
    print(honda.get_gas_info())
    print("\n12. Gas car horn:")
    honda.honk()
    print("\n13. Stopping gas car:")
    honda.stop()


if __name__ == "__main__":
    demonstrate_inheritance()
