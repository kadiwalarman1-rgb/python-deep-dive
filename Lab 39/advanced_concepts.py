"""Demonstrate super(), multilevel inheritance, and the class MRO."""

from inheritance_lab import Animal, Dog


class ServiceDog(Dog):
    """A service dog is a Dog, and therefore also an Animal."""

    def __init__(self, name, breed, age, service_type):
        if not isinstance(service_type, str) or not service_type.strip():
            raise ValueError("Service type cannot be empty")
        super().__init__(name, breed, age)
        self.service_type = service_type.strip()
        self.is_working = False

    def work(self):
        """Start a service task."""
        self.is_working = True
        return f"{self.name} is now working as a {self.service_type} dog"

    def rest(self):
        """Stop the current service task and rest."""
        self.is_working = False
        return f"{self.name} is resting after work"

    def get_service_info(self):
        """Combine inherited dog information with service details."""
        return "\n".join([
            self.get_dog_info(),
            f"Service Type: {self.service_type}, Working: {self.is_working}",
        ])


def main():
    print("=== Multi-Level Inheritance ===")
    service_dog = ServiceDog("Guide", "Labrador", 3, "Guide Dog")
    print(service_dog.get_service_info())
    print(service_dog.work())
    print(service_dog.speak())
    print(service_dog.fetch())
    print(service_dog.rest())

    print(f"\nMethod Resolution Order: {ServiceDog.__mro__}")
    print("\n=== Inheritance Hierarchy ===")
    print(f"ServiceDog is subclass of Dog: {issubclass(ServiceDog, Dog)}")
    print(f"ServiceDog is subclass of Animal: {issubclass(ServiceDog, Animal)}")
    print(f"Dog is subclass of Animal: {issubclass(Dog, Animal)}")


if __name__ == "__main__":
    main()
