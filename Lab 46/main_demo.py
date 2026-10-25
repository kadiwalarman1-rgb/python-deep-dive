#!/usr/bin/env python3
"""Lab 46: Compare composition and inheritance side by side."""

from engine_car_composition import Car, Engine
from inheritance_example import ElectricCar, GasCar, Vehicle


def compare_composition_vs_inheritance():
    print("=" * 60)
    print("COMPOSITION vs INHERITANCE COMPARISON")
    print("=" * 60)
    print("\n1. COMPOSITION APPROACH:")
    print("-" * 30)
    print("Car 'has-a' Engine relationship")
    car = Car("BMW", "M3", 2023, "Twin-Turbo I6", 473, "Premium Gasoline")
    print(f"Created: {car.make} {car.model}")
    print(f"Engine Type: {car.engine.engine_type}")
    print(f"Engine Object: {type(car.engine).__name__}")
    car.start_car()
    car.accelerate(25)
    print(f"Car Speed: {car.speed} mph")
    print(f"Engine Status: {car.engine.is_running}")
    car.stop_car()

    print("\n2. INHERITANCE APPROACH:")
    print("-" * 30)
    print("ElectricCar 'is-a' Vehicle relationship")
    electric_car = ElectricCar("Porsche", "Taycan", 2023, 93.4, 227)
    print(f"Created: {electric_car.make} {electric_car.model}")
    print(f"Is instance of Vehicle: {isinstance(electric_car, Vehicle)}")
    print(f"Class hierarchy: {[cls.__name__ for cls in electric_car.__class__.__mro__]}")
    electric_car.start()
    electric_car.accelerate(25)
    print(f"Car Speed: {electric_car.speed} mph")
    print(f"Battery Level: {electric_car.current_charge:.1f} kWh")
    electric_car.stop()


def demonstrate_flexibility():
    print("\n" + "=" * 60 + "\nFLEXIBILITY DEMONSTRATION\n" + "=" * 60)
    print("\n1. COMPOSITION FLEXIBILITY:")
    print("-" * 35)
    print("Can easily swap or modify engine components")
    v8_engine = Engine("V8", 450, "Gasoline")
    electric_motor = Engine("Electric Motor", 300, "Electricity")
    flexible_car = Car("Generic", "Sports Car", 2023, "V6", 300, "Gasoline")
    print(f"Original engine: {flexible_car.engine.get_engine_info()}")
    print("\nSwapping to V8 engine...")
    flexible_car.engine = v8_engine
    print(f"New engine: {flexible_car.engine.get_engine_info()}")
    print("\nSwapping to electric motor...")
    flexible_car.engine = electric_motor
    print(f"New engine: {flexible_car.engine.get_engine_info()}")

    print("\n2. INHERITANCE FLEXIBILITY:")
    print("-" * 35)
    print("Can create specialized vehicle types with shared behavior")
    vehicles = [
        ElectricCar("Tesla", "Cybertruck", 2024, 200, 500),
        GasCar("Ford", "Mustang", 2023, "V8", 15),
        ElectricCar("Rivian", "R1T", 2023, 135, 314),
    ]
    print("\nDemonstrating polymorphism:")
    for vehicle in vehicles:
        print(f"\n{vehicle.make} {vehicle.model}:")
        vehicle.start()
        vehicle.accelerate(20)
        vehicle.honk()
        vehicle.stop()


def analyze_relationships():
    print("\n" + "=" * 60 + "\nRELATIONSHIP ANALYSIS\n" + "=" * 60)
    print("\n1. COMPOSITION ('HAS-A' RELATIONSHIP):")
    print("-" * 40)
    for example in ["Car HAS-A Engine", "House HAS-A Door", "Computer HAS-A Processor",
                    "Phone HAS-A Battery", "Book HAS-A Chapter"]:
        print(f"  • {example}")
    print("\n   Benefits of Composition:")
    print("   - More flexible and modular")
    print("   - Easier to test individual components")
    print("   - Can change behavior at runtime")
    print("   - Follows 'favor composition over inheritance' principle")

    print("\n2. INHERITANCE ('IS-A' RELATIONSHIP):")
    print("-" * 40)
    for example in ["ElectricCar IS-A Vehicle", "Dog IS-A Animal", "Circle IS-A Shape",
                    "Manager IS-A Employee", "Smartphone IS-A Phone"]:
        print(f"  • {example}")
    print("\n   Benefits of Inheritance:")
    print("   - Code reuse through shared methods")
    print("   - Polymorphism support")
    print("   - Clear hierarchical relationships")
    print("   - Method overriding capabilities")


def practical_guidelines():
    print("\n" + "=" * 60 + "\nPRACTICAL GUIDELINES\n" + "=" * 60)
    print("\nWhen to use COMPOSITION:")
    print("-" * 30)
    for item in [
        "When you need flexibility to change components",
        "When objects have complex internal parts",
        "When you want to avoid deep inheritance hierarchies",
        "When components can be reused in different contexts",
        "When you need to combine multiple functionalities",
    ]:
        print(f"  ✓ {item}")

    print("\nWhen to use INHERITANCE:")
    print("-" * 30)
    for item in [
        "When there's a clear 'is-a' relationship",
        "When you need polymorphic behavior",
        "When subclasses share common interface",
        "When you want to extend existing functionality",
        "When the relationship is stable and unlikely to change",
    ]:
        print(f"  ✓ {item}")

    print("\nBest Practices:")
    print("-" * 15)
    for item in [
        "Favor composition over inheritance when it improves flexibility",
        "Use inheritance for 'is-a' relationships only",
        "Keep inheritance hierarchies shallow",
        "Consider interfaces/abstract classes for contracts",
        "Test both approaches to see which fits better",
    ]:
        print(f"  → {item}")


if __name__ == "__main__":
    compare_composition_vs_inheritance()
    demonstrate_flexibility()
    analyze_relationships()
    practical_guidelines()
