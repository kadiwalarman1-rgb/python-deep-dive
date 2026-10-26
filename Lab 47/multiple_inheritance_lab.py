#!/usr/bin/env python3
"""Lab 47: Multiple Inheritance - runnable demonstrations."""


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        print(f"Animal constructor called for {self.name}")

    def make_sound(self):
        return f"{self.name} makes a generic animal sound"

    def move(self):
        return f"{self.name} moves around"

    def eat(self):
        return f"{self.name} eats food"

    def get_info(self):
        return f"Animal: {self.name}, Species: {self.species}"


class Mammal:
    def __init__(self, fur_color, warm_blooded=True):
        self.fur_color = fur_color
        self.warm_blooded = warm_blooded
        print(f"Mammal constructor called with fur color: {self.fur_color}")

    def make_sound(self):
        return "Mammal makes a warm-blooded sound"

    def regulate_temperature(self):
        return ("Regulating body temperature internally" if self.warm_blooded
                else "Cannot regulate body temperature")

    def feed_young(self):
        return "Feeds young with milk"

    def get_mammal_info(self):
        return f"Fur color: {self.fur_color}, Warm-blooded: {self.warm_blooded}"


class Dog(Animal, Mammal):
    def __init__(self, name, breed, fur_color):
        Animal.__init__(self, name, "Canine")
        Mammal.__init__(self, fur_color)
        self.breed = breed
        print(f"Dog constructor called for {self.name} ({self.breed})")

    def make_sound(self):
        return f"{self.name} barks: Woof! Woof!"

    def fetch(self):
        return f"{self.name} fetches the ball"

    def wag_tail(self):
        return f"{self.name} wags tail happily"

    def get_full_info(self):
        return (f"{self.get_info()}, {self.get_mammal_info()}, "
                f"Breed: {self.breed}")


class EnhancedDog(Animal, Mammal):
    def __init__(self, name, breed, fur_color, age):
        super().__init__(name, "Canine")
        Mammal.__init__(self, fur_color)
        self.breed = breed
        self.age = age

    def make_sound(self):
        return f"{super().make_sound()} - Enhanced: {self.name} barks loudly!"

    def move(self):
        return f"{super().move()} - specifically by running and jumping"

    def get_enhanced_info(self):
        return (f"{super().get_info()}, {self.get_mammal_info()}, "
                f"Breed: {self.breed}, Age: {self.age}")


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        return f"{self.make} {self.model} engine started"

    def stop_engine(self):
        return f"{self.make} {self.model} engine stopped"


class Electric:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def charge_battery(self):
        return f"Charging {self.battery_capacity}kWh battery"

    def check_battery_level(self):
        return f"Battery level: 85% ({self.battery_capacity}kWh capacity)"


class Autonomous:
    def __init__(self, autonomy_level):
        self.autonomy_level = autonomy_level

    def engage_autopilot(self):
        return f"Autopilot engaged (Level {self.autonomy_level})"

    def disengage_autopilot(self):
        return "Autopilot disengaged"


class ElectricAutonomousCar(Vehicle, Electric, Autonomous):
    def __init__(self, make, model, battery_capacity, autonomy_level, color):
        Vehicle.__init__(self, make, model)
        Electric.__init__(self, battery_capacity)
        Autonomous.__init__(self, autonomy_level)
        self.color = color

    def start_engine(self):
        return f"{self.make} {self.model} electric motor activated silently"

    def full_status(self):
        return (f"{self.color} {self.make} {self.model} - "
                f"Battery: {self.battery_capacity}kWh, "
                f"Autonomy: Level {self.autonomy_level}")


class A:
    def method(self):
        return "Method from A"


class B(A):
    def method(self):
        return "Method from B"


class C(A):
    def method(self):
        return "Method from C"


class D(B, C):
    def method(self):
        return f"Method from D, calling super: {super().method()}"


def main():
    print("=" * 60)
    print("LAB 47: MULTIPLE INHERITANCE DEMONSTRATION")
    print("=" * 60)

    print("\n1. BASIC MULTIPLE INHERITANCE")
    dog = Dog("Buddy", "Golden Retriever", "Golden")
    print(dog.make_sound())
    print(dog.move())
    print(dog.eat())
    print(dog.regulate_temperature())
    print(dog.fetch())
    print(dog.get_full_info())

    print("\n2. METHOD RESOLUTION ORDER (MRO)")
    for index, cls in enumerate(Dog.__mro__, start=1):
        print(f"{index}. {cls.__name__}")

    print("\n3. USING super()")
    enhanced = EnhancedDog("Rex", "German Shepherd", "Brown", 3)
    print(enhanced.make_sound())
    print(enhanced.move())
    print(enhanced.get_enhanced_info())

    print("\n4. COMPLEX MULTIPLE INHERITANCE")
    tesla = ElectricAutonomousCar("Tesla", "Model S", 100, 4, "Red")
    print(tesla.start_engine())
    print(tesla.stop_engine())
    print(tesla.charge_battery())
    print(tesla.check_battery_level())
    print(tesla.engage_autopilot())
    print(tesla.disengage_autopilot())
    print(tesla.full_status())

    print("\n5. DIAMOND PROBLEM")
    d = D()
    print(d.method())
    for index, cls in enumerate(D.__mro__, start=1):
        print(f"{index}. {cls.__name__}")

    print("\nLAB COMPLETED SUCCESSFULLY!")


if __name__ == "__main__":
    main()
