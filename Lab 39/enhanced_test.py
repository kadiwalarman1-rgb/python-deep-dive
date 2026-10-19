"""Demonstrate Dog training, tricks, and energy changes."""

from inheritance_lab import Dog


def main():
    my_dog = Dog("Max", "German Shepherd", 3)

    print("=== Initial Dog Information ===")
    print(my_dog.get_dog_info())

    print("\n=== Training and Learning Tricks ===")
    print(my_dog.train())
    print(my_dog.learn_trick("sit"))
    print(my_dog.learn_trick("stay"))
    print(my_dog.learn_trick("roll over"))
    print(my_dog.learn_trick("sit"))

    print("\n=== Performing Tricks ===")
    print(my_dog.perform_trick("sit"))
    print(my_dog.perform_trick("stay"))
    print(my_dog.perform_trick("jump"))

    print("\n=== Playing Fetch ===")
    for number in range(6):
        print(f"Fetch {number + 1}: {my_dog.fetch()}")

    print("\n=== Final Dog Information ===")
    print(my_dog.get_dog_info())


if __name__ == "__main__":
    main()
