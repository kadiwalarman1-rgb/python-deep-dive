"""Demonstrate private-name access, name mangling, and encapsulation."""

from person_class import Person


def test_direct_access() -> None:
    """Show expected behavior when accessing double-underscore attributes."""
    print("=== Testing Direct Access to Private Attributes ===")
    person = Person("Alice Johnson", 25)

    for attribute in ("__name", "__age"):
        print(f"\nAttempting direct access to {attribute}...")
        try:
            getattr(person, attribute)
        except AttributeError as error:
            print(f"PASS: Direct access is unavailable: {error}")
        else:
            raise AssertionError(f"Unexpectedly found {attribute}")

    print("\nUsing getter methods...")
    print(f"Name via getter: {person.get_name()}")
    print(f"Age via getter: {person.get_age()}")

    print("\nPython name-mangled attributes (demonstration only)...")
    print(f"Name via mangled attribute: {person._Person__name}")
    print(f"Age via mangled attribute: {person._Person__age}")
    print("Name-mangled access is possible, but should not be used as the public interface.")

    print("\nAssigning person.__name creates a separate attribute...")
    person.__name = "Hacker Name"
    person.__age = 999
    print(f"Separate public attribute: {person.__name}, {person.__age}")
    print(f"Actual encapsulated values: {person.get_name()}, {person.get_age()}")


if __name__ == "__main__":
    test_direct_access()
