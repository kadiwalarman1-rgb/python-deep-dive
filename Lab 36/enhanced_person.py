class Person:
    def __init__(self, name, age, occupation="Unemployed", city="Unknown"):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name cannot be empty")
        if not isinstance(age, int) or isinstance(age, bool) or age < 0:
            raise ValueError("Age must be a non-negative integer")
        if not isinstance(occupation, str) or not occupation.strip():
            raise ValueError("Occupation cannot be empty")
        if not isinstance(city, str) or not city.strip():
            raise ValueError("City cannot be empty")
        self.name = name.strip()
        self.age = age
        self.occupation = occupation.strip()
        self.city = city.strip()
        self.friends = []

    def display_info(self):
        print(f"--- {self.name}'s Profile ---")
        print(f"Age: {self.age}")
        print(f"Occupation: {self.occupation}")
        print(f"City: {self.city}")
        print(f"Number of friends: {len(self.friends)}")
        if self.friends:
            print(f"Friends: {', '.join(self.friends)}")
        print("-" * 30)

    def add_friend(self, friend_name):
        if not isinstance(friend_name, str) or not friend_name.strip():
            raise ValueError("Friend name cannot be empty")
        friend_name = friend_name.strip()
        if friend_name not in self.friends:
            self.friends.append(friend_name)
            print(f"{friend_name} has been added to {self.name}'s friend list.")
            return True
        print(f"{friend_name} is already {self.name}'s friend.")
        return False

    def change_occupation(self, new_occupation):
        if not isinstance(new_occupation, str) or not new_occupation.strip():
            raise ValueError("Occupation cannot be empty")
        old_occupation = self.occupation
        self.occupation = new_occupation.strip()
        print(f"{self.name} changed occupation from {old_occupation} to {self.occupation}")

    def move_to_city(self, new_city):
        if not isinstance(new_city, str) or not new_city.strip():
            raise ValueError("City cannot be empty")
        old_city = self.city
        self.city = new_city.strip()
        print(f"{self.name} moved from {old_city} to {self.city}")

    def is_adult(self):
        return self.age >= 18

    def get_age_group(self):
        if self.age < 13:
            return "Child"
        if self.age < 20:
            return "Teenager"
        if self.age < 60:
            return "Adult"
        return "Senior"


if __name__ == "__main__":
    person1 = Person("Emma Wilson", 28, "Software Engineer", "San Francisco")
    person2 = Person("Michael Brown", 17, "Student", "Chicago")
    person3 = Person("Sarah Davis", 35, "Teacher", "New York")

    print("=== Initial Profiles ===")
    for person in (person1, person2, person3):
        person.display_info()

    print("=== Adding Friends ===")
    person1.add_friend("John")
    person1.add_friend("Lisa")
    person1.add_friend("Mike")
    person2.add_friend("Alex")
    person2.add_friend("Sam")

    print("\n=== Life Changes ===")
    person2.change_occupation("College Student")
    person3.move_to_city("Los Angeles")

    print("\n=== Age Analysis ===")
    for person in (person1, person2, person3):
        adult_status = "an adult" if person.is_adult() else "not an adult"
        print(f"{person.name} is {adult_status} and belongs to the {person.get_age_group()} age group.")

    print("\n=== Final Profiles ===")
    for person in (person1, person2, person3):
        person.display_info()
