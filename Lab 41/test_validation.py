"""Standalone demonstrations of Person input validation."""

from person_class import Person


def run_validation_demo() -> None:
    """Show valid inputs and confirm common invalid inputs are rejected."""
    print("=== Testing Input Validation ===")

    print("\nTest 1: Creating a valid person...")
    person = Person("John Doe", 30)
    person.display_info()
    print("PASS: Valid person created successfully")

    invalid_cases = [
        ("empty name", lambda: Person("", 25)),
        ("non-string name", lambda: Person(123, 25)),
        ("negative age", lambda: Person("Jane Doe", -5)),
        ("age above 150", lambda: Person("Old Person", 200)),
        ("non-integer age", lambda: Person("Jane Doe", "twenty-five")),
        ("boolean age", lambda: Person("Jane Doe", True)),
    ]

    for label, operation in invalid_cases:
        print(f"\nTesting {label}...")
        try:
            operation()
        except ValueError as error:
            print(f"PASS: Validation rejected {label}: {error}")
        else:
            raise AssertionError(f"Validation unexpectedly accepted {label}")

    print("\nTesting invalid update of an existing person...")
    try:
        person.set_name("")
    except ValueError as error:
        print(f"PASS: Invalid name update rejected: {error}")
    else:
        raise AssertionError("Validation unexpectedly accepted an empty name")


if __name__ == "__main__":
    run_validation_demo()
