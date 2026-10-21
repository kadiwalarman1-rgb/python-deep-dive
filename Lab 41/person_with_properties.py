"""A Pythonic encapsulation example using property decorators."""


class PersonWithProperties:
    """Represent a person with validated name and age properties."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self) -> str:
        """Return the person's name."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """Validate and normalize the name before storing it."""
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        cleaned_name = value.strip()
        if len(cleaned_name) < 2:
            raise ValueError("Name must be at least 2 characters long")
        self.__name = cleaned_name.title()

    @property
    def age(self) -> int:
        """Return the person's age."""
        return self.__age

    @age.setter
    def age(self, value: int) -> None:
        """Validate and store an age between 0 and 150 inclusive."""
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError("Age must be an integer")
        if not 0 <= value <= 150:
            raise ValueError("Age must be between 0 and 150")
        self.__age = value

    def display_info(self) -> None:
        """Print the person's current information."""
        print(f"Person: {self.name}, Age: {self.age}")

    def have_birthday(self) -> None:
        """Increment age through the validated property setter."""
        print(f"Happy Birthday, {self.name}!")
        self.age += 1


if __name__ == "__main__":
    print("=== Property Decorator Demonstration ===")
    person = PersonWithProperties("alice johnson", 25)
    person.display_info()

    person.name = "Alice Johnson-Smith"
    person.age = 26
    person.display_info()

    try:
        person.age = -5
    except ValueError as error:
        print(f"Validation works: {error}")
