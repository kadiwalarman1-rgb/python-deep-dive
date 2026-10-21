"""Comprehensive demonstration of the encapsulation concepts in Lab 41."""

from person_class import Person


def main_demo() -> None:
    """Demonstrate validated construction, getters, setters, and methods."""
    print("=" * 60)
    print("ENCAPSULATION DEMONSTRATION")
    print("=" * 60)

    print("\n1. CREATING PERSON OBJECTS WITH VALIDATION")
    person1 = Person("john smith", 28)
    person2 = Person("MARY JOHNSON", 35)
    person1.display_info()
    person2.display_info()

    print("\n2. ACCESSING DATA THROUGH GETTER METHODS")
    print(f"Person 1 name: {person1.get_name()}")
    print(f"Person 1 age: {person1.get_age()}")
    print(f"Person 2 name: {person2.get_name()}")
    print(f"Person 2 age: {person2.get_age()}")

    print("\n3. MODIFYING DATA THROUGH SETTER METHODS")
    person1.set_name("Jonathan Smith Jr.")
    person1.set_age(29)
    person1.display_info()

    print("\n4. VALIDATION PREVENTING INVALID DATA")
    invalid_operations = [
        ("Empty name", lambda: person1.set_name("")),
        ("Negative age", lambda: person1.set_age(-10)),
        ("Age too high", lambda: person1.set_age(200)),
        ("Non-string name", lambda: person1.set_name(12345)),
        ("Non-integer age", lambda: person1.set_age("thirty")),
    ]
    for label, operation in invalid_operations:
        try:
            operation()
        except ValueError as error:
            print(f"PASS: {label} rejected: {error}")
        else:
            print(f"FAIL: {label} was unexpectedly allowed")

    print("\n5. METHODS WORKING WITH ENCAPSULATED DATA")
    person1.have_birthday()
    person2.have_birthday()
    person1.display_info()
    person2.display_info()

    print("\n6. ENCAPSULATION BENEFITS DEMONSTRATED")
    print("- Validation supports data integrity.")
    print("- Getters and setters provide a controlled interface.")
    print("- Private-name conventions reduce accidental access.")
    print("- Business rules are centralized in setter methods.")


if __name__ == "__main__":
    main_demo()
