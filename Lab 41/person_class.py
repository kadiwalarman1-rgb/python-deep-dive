"""Person class demonstrating encapsulation with getters and validated setters."""


class Person:
    """Represent a person while controlling access to name and age."""

    def __init__(self, name: str, age: int) -> None:
        # Route initialization through the setters so initial values are validated.
        self.set_name(name)
        self.set_age(age)

    def get_name(self) -> str:
        """Return the person's name."""
        return self.__name

    def get_age(self) -> int:
        """Return the person's age."""
        return self.__age

    def set_name(self, name: str) -> None:
        """Validate, normalize, and store a name."""
        if not isinstance(name, str):
            raise ValueError("Name must be a string")

        cleaned_name = name.strip()
        if len(cleaned_name) < 2:
            raise ValueError("Name must be at least 2 characters long")

        self.__name = cleaned_name.title()

    def set_age(self, age: int) -> None:
        """Validate and store an age between 0 and 150 inclusive."""
        # bool is a subclass of int in Python, but it is not a meaningful age.
        if isinstance(age, bool) or not isinstance(age, int):
            raise ValueError("Age must be an integer")
        if not 0 <= age <= 150:
            raise ValueError("Age must be between 0 and 150")

        self.__age = age

    def display_info(self) -> None:
        """Print the person's current information using getters."""
        print(f"Person Info: {self.get_name()}, Age: {self.get_age()}")

    def have_birthday(self) -> None:
        """Increase the age by one, preserving the setter's validation."""
        print(f"Happy Birthday, {self.get_name()}!")
        self.set_age(self.get_age() + 1)


if __name__ == "__main__":
    print("=== Testing Person Class with Encapsulation ===")
    person = Person("alice johnson", 25)
    person.display_info()

    print("\n=== Testing Setter Methods ===")
    person.set_name("Bob Smith")
    person.set_age(30)
    person.display_info()

    print("\n=== Testing Birthday Method ===")
    person.have_birthday()
    person.display_info()
