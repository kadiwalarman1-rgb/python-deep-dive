"""Compare base methods against overridden methods on Dog."""

from inheritance_lab import Animal, Dog


def main():
    generic_animal = Animal("Generic", "Unknown")
    my_dog = Dog("Bella", "Labrador", 2)

    print("=== Comparing Base Class vs Derived Class Methods ===")
    print("\n--- Base Class Animal ---")
    print(f"Animal speak: {generic_animal.speak()}")
    print(f"Animal eat: {generic_animal.eat()}")

    print("\n--- Derived Class Dog (Overridden Methods) ---")
    print(f"Dog speak: {my_dog.speak()}")
    print(f"Dog eat: {my_dog.eat()}")
    print(f"Dog eat with parameter: {my_dog.eat('premium kibble')}")

    print("\n--- Inherited Methods (Not Overridden) ---")
    print(f"Dog sleep: {my_dog.sleep()}")

    print("\n=== Method Resolution Order ===")
    print(f"Dog class MRO: {Dog.__mro__}")


if __name__ == "__main__":
    main()
