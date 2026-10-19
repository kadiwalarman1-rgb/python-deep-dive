"""Basic demonstration of inherited Animal methods on a Dog instance."""

from inheritance_lab import Animal, Dog


def main():
    my_dog = Dog("Buddy", "Golden Retriever")

    print("=== Testing Inherited and Overridden Methods ===")
    print(my_dog.speak())
    print(my_dog.eat())
    print(my_dog.sleep())
    print(my_dog.get_info())

    print("\n=== Dog-Specific Method ===")
    print(my_dog.bark())

    print("\n=== Dog Attributes ===")
    print(f"Name: {my_dog.name}")
    print(f"Species: {my_dog.species}")
    print(f"Breed: {my_dog.breed}")
    print(f"Is Trained: {my_dog.is_trained}")
    print(f"Is Alive: {my_dog.is_alive}")


if __name__ == "__main__":
    main()
