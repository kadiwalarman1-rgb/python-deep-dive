"""Base and derived classes for the Lab 39 inheritance exercises."""


class Animal:
    """Base class representing a generic animal."""

    def __init__(self, name, species):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Animal name cannot be empty")
        if not isinstance(species, str) or not species.strip():
            raise ValueError("Species cannot be empty")
        self.name = name.strip()
        self.species = species.strip()
        self.is_alive = True

    def speak(self):
        """Return a generic animal sound."""
        return f"{self.name} makes a sound"

    def eat(self):
        """Return a generic eating message."""
        return f"{self.name} is eating"

    def sleep(self):
        """Return a sleeping message."""
        return f"{self.name} is sleeping"

    def get_info(self):
        """Return basic animal information."""
        return f"Name: {self.name}, Species: {self.species}, Alive: {self.is_alive}"


class Dog(Animal):
    """Dog inherits common behavior from Animal and specializes it."""

    def __init__(self, name, breed, age=1):
        if not isinstance(breed, str) or not breed.strip():
            raise ValueError("Breed cannot be empty")
        if not isinstance(age, int) or isinstance(age, bool) or age < 0:
            raise ValueError("Age must be a non-negative integer")

        super().__init__(name, "Canine")
        self.breed = breed.strip()
        self.age = age
        self.is_trained = False
        self.tricks = []
        self.energy_level = 100

    def bark(self):
        """Return a dog-specific sound."""
        return f"{self.name} says Woof! Woof!"

    def speak(self):
        """Override the base Animal.speak method."""
        return f"{self.name} barks: Woof! Woof!"

    def eat(self, food="dog food"):
        """Override Animal.eat while allowing a food argument."""
        if not isinstance(food, str) or not food.strip():
            raise ValueError("Food cannot be empty")
        return f"{self.name} is eating {food.strip()} from the dog bowl"

    def fetch(self):
        """Fetch a ball when sufficient energy remains."""
        if self.energy_level > 20:
            self.energy_level -= 20
            return f"{self.name} fetches the ball! Energy level: {self.energy_level}"
        return f"{self.name} is too tired to fetch"

    def learn_trick(self, trick):
        """Teach the dog a trick, avoiding duplicate entries."""
        if not isinstance(trick, str) or not trick.strip():
            return "Trick name cannot be empty"
        trick = trick.strip()
        if trick not in self.tricks:
            self.tricks.append(trick)
            return f"{self.name} learned a new trick: {trick}"
        return f"{self.name} already knows {trick}"

    def perform_trick(self, trick):
        """Perform a trick only if the dog has learned it."""
        if trick in self.tricks:
            return f"{self.name} performs {trick}!"
        return f"{self.name} doesn't know how to {trick}"

    def train(self):
        """Mark the dog as trained."""
        self.is_trained = True
        return f"{self.name} has been trained!"

    def get_dog_info(self):
        """Return base animal data plus dog-specific details."""
        return "\n".join([
            self.get_info(),
            f"Breed: {self.breed}, Age: {self.age}, Trained: {self.is_trained}",
            f"Tricks: {', '.join(self.tricks) if self.tricks else 'None'}",
            f"Energy Level: {self.energy_level}",
        ])


if __name__ == "__main__":
    example_dog = Dog("Buddy", "Golden Retriever")
    print(example_dog.get_info())
    print(example_dog.speak())
    print(example_dog.eat())
    print(example_dog.bark())
