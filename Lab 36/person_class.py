class Person:
    def __init__(self, name, age):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name cannot be empty")
        if not isinstance(age, int) or isinstance(age, bool) or age < 0:
            raise ValueError("Age must be a non-negative integer")
        self.name = name.strip()
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


if __name__ == "__main__":
    person1 = Person("Alice Johnson", 25)
    person1.display_info()
