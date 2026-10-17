class Person:
    def __init__(self, name, age):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name cannot be empty")
        if not isinstance(age, int) or isinstance(age, bool) or age < 0:
            raise ValueError("Age must be a non-negative integer")
        self.name = name.strip()
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.")


if __name__ == "__main__":
    person1 = Person("Alice Johnson", 25)
    person2 = Person("Bob Smith", 30)
    person3 = Person("Carol Davis", 22)

    print("=== Initial Information ===")
    person1.display_info()
    person2.display_info()
    person3.display_info()

    print("\n=== Birthday Celebrations ===")
    person1.have_birthday()
    person3.have_birthday()

    print("\n=== Updated Information ===")
    person1.display_info()
    person2.display_info()
    person3.display_info()
