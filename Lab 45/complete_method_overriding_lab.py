#!/usr/bin/env python3
"""
Lab 45: Inheritance and Method Overriding
Complete runnable implementation of the lab objectives.
"""


# Task 1: Basic method overriding
class Animal:
    """Base class representing a generic animal."""

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        """Default behavior, overridden by child classes."""
        return f"{self.name} makes a generic animal sound"

    def introduce(self):
        """Demonstrate dynamic dispatch through make_sound()."""
        return f"Hello, I'm {self.name}. {self.make_sound()}"


class Dog(Animal):
    """Dog-specific implementation of make_sound()."""

    def make_sound(self):
        return f"{self.name} barks: Woof! Woof!"


class Cat(Animal):
    """Cat-specific implementation of make_sound()."""

    def make_sound(self):
        return f"{self.name} meows: Meow! Meow!"


# Task 3: Real-world vehicle example
class Vehicle:
    """Base class for all vehicles."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            return f"{self.year} {self.make} {self.model} engine started"
        return f"{self.year} {self.make} {self.model} is already running"

    def stop_engine(self):
        if self.is_running:
            self.is_running = False
            return f"{self.year} {self.make} {self.model} engine stopped"
        return f"{self.year} {self.make} {self.model} is already stopped"

    def get_info(self):
        status = "running" if self.is_running else "stopped"
        return f"{self.year} {self.make} {self.model} - Status: {status}"

    def accelerate(self):
        if self.is_running:
            return f"{self.make} {self.model} is accelerating"
        return "Cannot accelerate - engine is not running"


class Car(Vehicle):
    """Car class overriding selected Vehicle methods."""

    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            return (
                f"Car {self.year} {self.make} {self.model} "
                "engine started with a smooth purr"
            )
        return f"Car {self.year} {self.make} {self.model} is already running"

    def accelerate(self):
        if self.is_running:
            return f"Car {self.make} {self.model} accelerates smoothly on the road"
        return "Cannot accelerate - car engine is not running"

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Doors: {self.doors}"


class Motorcycle(Vehicle):
    """Motorcycle class overriding selected Vehicle methods."""

    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size

    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            return (
                f"Motorcycle {self.year} {self.make} {self.model} "
                "engine roars to life!"
            )
        return (
            f"Motorcycle {self.year} {self.make} {self.model} "
            "is already running"
        )

    def accelerate(self):
        if self.is_running:
            return (
                f"Motorcycle {self.make} {self.model} "
                "accelerates with a powerful roar"
            )
        return "Cannot accelerate - motorcycle engine is not running"

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Engine: {self.engine_size}cc"


# Task 4: super() example
class ElectricCar(Car):
    """Electric car showing method overriding and super()."""

    def __init__(self, make, model, year, doors, battery_capacity):
        super().__init__(make, model, year, doors)
        self.battery_capacity = battery_capacity
        self.battery_level = 100

    def start_engine(self):
        if self.battery_level <= 0:
            return f"Cannot start {self.make} {self.model} - battery is empty"
        if not self.is_running:
            self.is_running = True
            return (
                f"Electric car {self.year} {self.make} {self.model} "
                "started silently"
            )
        return (
            f"Electric car {self.year} {self.make} {self.model} "
            "is already running"
        )

    def accelerate(self):
        if self.battery_level <= 10:
            return f"Low battery warning! {self.make} {self.model} needs charging"

        parent_message = super().accelerate()
        if "Cannot accelerate" in parent_message:
            return parent_message

        self.battery_level -= 2
        return f"Electric {parent_message} - Battery: {self.battery_level}%"

    def charge_battery(self):
        if self.battery_level < 100:
            self.battery_level = 100
            return f"{self.make} {self.model} battery fully charged"
        return f"{self.make} {self.model} battery is already full"

    def get_info(self):
        base_info = super().get_info()
        return (
            f"{base_info}, Battery: {self.battery_capacity}kWh "
            f"({self.battery_level}%)"
        )


# Task 5: Multi-level inheritance
class LuxuryCar(Car):
    """Car with additional comfort features."""

    def __init__(self, make, model, year, doors, luxury_features):
        super().__init__(make, model, year, doors)
        self.luxury_features = luxury_features

    def start_engine(self):
        base_start = super().start_engine()
        if "engine started" in base_start:
            return f"{base_start} with premium comfort settings activated"
        return base_start

    def accelerate(self):
        base_accelerate = super().accelerate()
        if "accelerates" in base_accelerate:
            return f"{base_accelerate} with adaptive suspension engaged"
        return base_accelerate

    def get_info(self):
        base_info = super().get_info()
        features = ", ".join(self.luxury_features)
        return f"{base_info}, Luxury Features: [{features}]"


class SportsCar(LuxuryCar):
    """Sports car adds sport mode on top of LuxuryCar."""

    def __init__(self, make, model, year, doors, luxury_features, top_speed):
        super().__init__(make, model, year, doors, luxury_features)
        self.top_speed = top_speed
        self.sport_mode = False

    def activate_sport_mode(self):
        self.sport_mode = True
        return f"{self.make} {self.model} sport mode activated!"

    def deactivate_sport_mode(self):
        self.sport_mode = False
        return f"{self.make} {self.model} sport mode deactivated"

    def accelerate(self):
        if not self.is_running:
            return "Cannot accelerate - engine is not running"
        if self.sport_mode:
            return (
                f"Sports car {self.make} {self.model} "
                "launches forward with incredible power!"
            )
        return f"{super().accelerate()} (Sport mode available)"

    def get_info(self):
        base_info = super().get_info()
        mode = "Sport" if self.sport_mode else "Normal"
        return f"{base_info}, Top Speed: {self.top_speed}mph, Mode: {mode}"


def test_basic_overriding():
    print("\n=== Task 1: Basic Method Overriding ===")
    generic = Animal("Generic")
    buddy = Dog("Buddy")
    whiskers = Cat("Whiskers")

    print(f"Generic Animal: {generic.make_sound()}")
    print(f"Dog: {buddy.make_sound()}")
    print(f"Cat: {whiskers.make_sound()}")
    print("\nUsing introduce method:")
    print(buddy.introduce())
    print(whiskers.introduce())


def test_polymorphism():
    print("\n=== Task 2: Polymorphism Demonstration ===")
    animals = [Animal("Generic Animal"), Dog("Rex"), Cat("Mittens"), Dog("Max")]
    for animal in animals:
        print(f"{type(animal).__name__}: {animal.make_sound()}")


def show_method_resolution():
    print("\n=== Method Resolution Order ===")
    print("Method Resolution Order for Dog class:")
    for cls in Dog.__mro__:
        print(f"  {cls}")
    print(f"Dog class has make_sound method: {hasattr(Dog, 'make_sound')}")
    print(f"Animal class has make_sound method: {hasattr(Animal, 'make_sound')}")


def test_vehicles():
    print("\n=== Task 3: Vehicle Classes ===")
    vehicles = [
        Vehicle("Generic", "Vehicle", 2020),
        Car("Toyota", "Camry", 2022, 4),
        Motorcycle("Harley-Davidson", "Street 750", 2021, 750),
    ]

    for item in vehicles:
        print(f"\n--- {type(item).__name__} ---")
        print(item.get_info())
        print(item.start_engine())
        print(item.accelerate())
        print(item.stop_engine())


def test_super_usage():
    print("\n=== Task 4: Using super() ===")
    tesla = ElectricCar("Tesla", "Model 3", 2023, 4, 75)
    print("Initial state:")
    print(tesla.get_info())
    print("\nStarting and accelerating:")
    print(tesla.start_engine())

    for index in range(3):
        print(f"Acceleration {index + 1}: {tesla.accelerate()}")

    print("\nCharging battery:")
    print(tesla.charge_battery())
    print(tesla.get_info())


def test_multilevel_inheritance():
    print("\n=== Task 5: Multi-Level Inheritance ===")
    ferrari = SportsCar(
        make="Ferrari",
        model="488 GTB",
        year=2023,
        doors=2,
        luxury_features=["Leather Seats", "Premium Audio", "Climate Control"],
        top_speed=205,
    )

    print("Ferrari Information:")
    print(ferrari.get_info())
    print("\nStarting Ferrari:")
    print(ferrari.start_engine())
    print("\nNormal acceleration:")
    print(ferrari.accelerate())
    print("\nActivating sport mode:")
    print(ferrari.activate_sport_mode())
    print(ferrari.get_info())
    print("\nSport mode acceleration:")
    print(ferrari.accelerate())
    print("\nMethod Resolution Order for SportsCar:")
    for cls in SportsCar.__mro__:
        print(f"  {cls}")


def demonstrate_override_chain():
    print("\n=== Method Override Chain Demonstration ===")
    items = [
        ("Vehicle", Vehicle("Generic", "Vehicle", 2020)),
        ("Car", Car("Honda", "Civic", 2022, 4)),
        ("LuxuryCar", LuxuryCar("BMW", "7 Series", 2023, 4,
                                ["Massage Seats", "Panoramic Roof"])),
        ("SportsCar", SportsCar("Porsche", "911", 2023, 2,
                                ["Racing Seats", "Sport Exhaust"], 190)),
    ]

    for name, item in items:
        print(f"\n{name}:")
        print(f"  {item.start_engine()}")

    print("\nComparing accelerate() across inheritance levels:")
    for name, item in items:
        print(f"\n{name}:")
        print(f"  {item.accelerate()}")


def main():
    print("Lab 45: Inheritance and Method Overriding")
    print("=" * 50)
    test_basic_overriding()
    test_polymorphism()
    show_method_resolution()
    test_vehicles()
    test_super_usage()
    test_multilevel_inheritance()
    demonstrate_override_chain()
    print("\n" + "=" * 50)
    print("Lab completed successfully!")


if __name__ == "__main__":
    main()
