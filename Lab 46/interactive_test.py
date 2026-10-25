#!/usr/bin/env python3
"""Lab 46: Interactive and batch object creation tests."""

from engine_car_composition import Car
from inheritance_example import ElectricCar, GasCar


def ask_number(prompt, default, cast=int):
    value = input(prompt).strip()
    if not value:
        return default
    try:
        return cast(value)
    except ValueError:
        print(f"Invalid number; using default {default}.")
        return default


def interactive_composition_test():
    print("=" * 50)
    print("INTERACTIVE COMPOSITION TESTING")
    print("=" * 50)
    print("\nCreate your custom car (press Enter to use defaults):")
    make = input("Enter car make (e.g., Toyota): ").strip() or "Toyota"
    model = input("Enter car model (e.g., Corolla): ").strip() or "Corolla"
    year = ask_number("Enter year (e.g., 2023): ", 2023)
    engine_type = input("Enter engine type (e.g., V4): ").strip() or "V4"
    horsepower = ask_number("Enter horsepower (e.g., 150): ", 150)
    fuel_type = input("Enter fuel type (e.g., Gasoline): ").strip() or "Gasoline"

    car = Car(make, model, year, engine_type, horsepower, fuel_type)
    print(f"\nCreated: {car.year} {car.make} {car.model}")
    print(car.get_car_status())

    while True:
        print("\n" + "-" * 30)
        print("What would you like to do?")
        print("1. Start car\n2. Accelerate\n3. Brake\n4. Shift gear")
        print("5. Honk horn\n6. Check status\n7. Stop car\n8. Exit")
        choice = input("Enter your choice (1-8): ").strip()
        if choice == "1":
            car.start_car()
        elif choice == "2":
            try:
                car.accelerate(ask_number("Enter speed increase (mph): ", 10))
            except ValueError as error:
                print(error)
        elif choice == "3":
            try:
                car.brake(ask_number("Enter speed decrease (mph): ", 10))
            except ValueError as error:
                print(error)
        elif choice == "4":
            try:
                car.shift_gear(ask_number("Enter gear number: ", 1))
            except ValueError as error:
                print(error)
        elif choice == "5":
            car.honk()
        elif choice == "6":
            print(car.get_car_status())
        elif choice == "7":
            car.stop_car()
        elif choice == "8":
            print("Thanks for testing!")
            break
        else:
            print("Invalid choice! Please try again.")


def batch_object_creation_test():
    print("\n" + "=" * 50 + "\nBATCH OBJECT CREATION TEST\n" + "=" * 50)
    cars_data = [
        ("Honda", "Civic", 2023, "4-Cylinder", 158, "Regular"),
        ("BMW", "X5", 2023, "V8", 523, "Premium"),
        ("Ford", "Mustang", 2023, "V8", 450, "Premium"),
        ("Toyota", "Prius", 2023, "Hybrid", 121, "Regular"),
    ]
    composition_cars = []
    print("\nCreating cars using COMPOSITION:")
    for index, (make, model, year, engine, hp, fuel) in enumerate(cars_data, 1):
        car = Car(make, model, year, engine, hp, fuel)
        composition_cars.append(car)
        print(f"{index}. Created {car.make} {car.model}")

    electric_data = [
        ("Tesla", "Model 3", 2023, 75, 358),
        ("BMW", "iX", 2023, 111.5, 324),
        ("Audi", "e-tron GT", 2023, 93.4, 238),
        ("Mercedes", "EQS", 2023, 107.8, 453),
    ]
    electric_cars = []
    print("\nCreating cars using INHERITANCE:")
    for index, (make, model, year, battery, range_miles) in enumerate(electric_data, 1):
        car = ElectricCar(make, model, year, battery, range_miles)
        electric_cars.append(car)
        print(f"{index}. Created {car.make} {car.model}")

    print("\n" + "-" * 40 + "\nTESTING COMPOSITION CARS:\n" + "-" * 40)
    for index, car in enumerate(composition_cars, 1):
        print(f"\n{index}. {car.year} {car.make} {car.model}")
        print(car.get_car_status())
        car.start_car()
        car.accelerate(10)
        car.brake(5)
        car.shift_gear(2)
        car.honk()
        car.stop_car()

    print("\n" + "-" * 40 + "\nTESTING INHERITANCE CARS:\n" + "-" * 40)
    for index, car in enumerate(electric_cars, 1):
        print(f"\n{index}. {car.year} {car.make} {car.model}")
        car.start()
        car.accelerate(20)
        car.honk()
        car.brake(5)
        print(car.get_electric_info())
        car.stop()

    print("\nGasCar batch example:")
    gas_car = GasCar("Ford", "Mustang", 2023, "V8", 15)
    gas_car.start()
    gas_car.accelerate(10)
    print(gas_car.get_gas_info())
    gas_car.stop()
    print("\nBATCH OBJECT CREATION TEST COMPLETED")
    print(f"Composition cars tested: {len(composition_cars)}")
    print(f"Electric inheritance cars tested: {len(electric_cars)}")


if __name__ == "__main__":
    interactive_composition_test()
    batch_object_creation_test()
