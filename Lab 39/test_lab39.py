"""Automated tests for Lab 39 inheritance concepts."""

import unittest

from inheritance_lab import Animal, Dog
from advanced_concepts import ServiceDog


class AnimalTests(unittest.TestCase):
    def test_animal_initialization_and_methods(self):
        animal = Animal("Milo", "Cat")
        self.assertEqual(animal.name, "Milo")
        self.assertEqual(animal.species, "Cat")
        self.assertTrue(animal.is_alive)
        self.assertEqual(animal.speak(), "Milo makes a sound")
        self.assertEqual(animal.eat(), "Milo is eating")
        self.assertEqual(animal.sleep(), "Milo is sleeping")

    def test_empty_values_are_rejected(self):
        with self.assertRaises(ValueError):
            Animal("", "Unknown")
        with self.assertRaises(ValueError):
            Animal("Milo", "")


class DogTests(unittest.TestCase):
    def test_constructor_and_parent_initialization(self):
        dog = Dog("Buddy", "Golden Retriever")
        self.assertEqual(dog.species, "Canine")
        self.assertEqual(dog.age, 1)
        self.assertTrue(dog.is_alive)
        self.assertFalse(dog.is_trained)
        self.assertEqual(dog.energy_level, 100)

    def test_method_overriding_and_inherited_method(self):
        dog = Dog("Bella", "Labrador", 2)
        self.assertEqual(dog.speak(), "Bella barks: Woof! Woof!")
        self.assertEqual(dog.eat(), "Bella is eating dog food from the dog bowl")
        self.assertEqual(dog.eat("premium kibble"), "Bella is eating premium kibble from the dog bowl")
        self.assertEqual(dog.sleep(), "Bella is sleeping")

    def test_trick_learning_and_performance(self):
        dog = Dog("Max", "Shepherd")
        self.assertIn("learned", dog.learn_trick("sit"))
        self.assertIn("already knows", dog.learn_trick("sit"))
        self.assertIn("performs sit", dog.perform_trick("sit"))
        self.assertIn("doesn't know", dog.perform_trick("jump"))

    def test_fetch_decreases_energy_and_stops_at_threshold(self):
        dog = Dog("Max", "Shepherd")
        for expected in (80, 60, 40, 20):
            self.assertIn(f"Energy level: {expected}", dog.fetch())
        self.assertEqual(dog.energy_level, 20)
        self.assertIn("too tired", dog.fetch())
        self.assertEqual(dog.energy_level, 20)

    def test_invalid_dog_inputs(self):
        with self.assertRaises(ValueError):
            Dog("Buddy", "")
        with self.assertRaises(ValueError):
            Dog("Buddy", "Shepherd", -1)


class ServiceDogTests(unittest.TestCase):
    def test_multilevel_inheritance(self):
        dog = ServiceDog("Guide", "Labrador", 3, "Guide Dog")
        self.assertIsInstance(dog, Dog)
        self.assertIsInstance(dog, Animal)
        self.assertFalse(dog.is_working)
        self.assertIn("now working", dog.work())
        self.assertTrue(dog.is_working)
        self.assertIn("resting", dog.rest())
        self.assertFalse(dog.is_working)
        self.assertEqual(dog.speak(), "Guide barks: Woof! Woof!")


if __name__ == "__main__":
    unittest.main(verbosity=2)
