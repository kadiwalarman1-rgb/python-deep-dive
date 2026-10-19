# Lab 39: Inheritance — Basic Inheritance Concept

## Objectives

- Create base and derived classes in Python.
- Reuse constructor initialization with super().
- Call inherited methods through a derived-class instance.
- Add attributes and behavior to a child class.
- Override parent methods and observe polymorphism.
- Use isinstance(), issubclass(), and method resolution order (MRO).
- Implement multilevel inheritance with ServiceDog.

## Files

| File | Purpose |
|---|---|
| inheritance_lab.py | Animal and Dog classes, inherited behavior, overriding, tricks, training, and energy. |
| test_inheritance.py | Basic inherited-method demonstration. |
| enhanced_test.py | Dog training, trick learning, and fetch-energy demonstration. |
| override_test.py | Compares Animal methods with overridden Dog methods. |
| experiment.py | Multiple Animal/Dog objects, polymorphism, and type checks. |
| advanced_concepts.py | ServiceDog subclass and multilevel inheritance using super(). |
| test_lab39.py | Automated tests for inheritance behavior and edge cases. |

## Run the lab

Use Python 3.8 or newer. No third-party packages are required. Run these commands from this directory:

    python3 inheritance_lab.py
    python3 test_inheritance.py
    python3 enhanced_test.py
    python3 override_test.py
    python3 experiment.py
    python3 advanced_concepts.py
    python3 -m unittest -v test_lab39.py

## Concepts demonstrated

- Animal is the base class. It provides shared attributes and methods.
- Dog inherits from Animal and initializes its parent attributes through super().__init__().
- Dog adds breed, age, training status, tricks, and energy level.
- Dog overrides speak() and eat(), while continuing to inherit methods such as sleep() and get_info().
- Polymorphism allows the same speak() call to produce different results for Animal and Dog objects.
- ServiceDog inherits from Dog, which itself inherits from Animal, demonstrating multilevel inheritance.
- isinstance() checks an object's type relationship; issubclass() checks a class relationship; __mro__ shows method lookup order.

## Behavior notes

- Dog age defaults to 1 when omitted.
- A successful fetch reduces energy by 20 while the energy level is above 20. At 20 or lower, the dog is too tired to fetch.
- Learning the same trick twice does not add a duplicate.
- This lab is a local learning exercise; it does not require external services or third-party packages.
