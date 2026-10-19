"""Experiment with multiple instances, polymorphism, and type checks."""

from inheritance_lab import Animal, Dog


def main():
    print("=== Creating Base Class Objects ===")
    cat = Animal("Whiskers", "Feline")
    bird = Animal("Tweety", "Avian")
    fish = Animal("Nemo", "Aquatic")
    animals = [cat, bird, fish]

    for animal in animals:
        print(animal.get_info())
        print(f"  {animal.speak()}")
        print(f"  {animal.eat()}")
        print()

    print("=== Creating Derived Class Objects ===")
    dog1 = Dog("Rex", "German Shepherd", 4)
    dog2 = Dog("Luna", "Border Collie", 2)
    dog3 = Dog("Charlie", "Bulldog", 6)
    dogs = [dog1, dog2, dog3]

    for dog in dogs:
        print(dog.get_dog_info())
        print(f"  {dog.speak()}")
        print(f"  {dog.bark()}")
        print()

    print("=== Polymorphism Demonstration ===")
    all_creatures = [*animals, *dogs]
    for creature in all_creatures:
        print(f"{creature.name}: {creature.speak()}")

    print("\n=== Type Checking ===")
    for creature in all_creatures:
        print(f"{creature.name}:")
        print(f"  Is Animal: {isinstance(creature, Animal)}")
        print(f"  Is Dog: {isinstance(creature, Dog)}")
        print(f"  Type: {type(creature).__name__}")


if __name__ == "__main__":
    main()
