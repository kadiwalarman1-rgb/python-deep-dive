"""Automated unit tests for Lab 41 encapsulation examples."""

import unittest

from person_class import Person
from person_with_properties import PersonWithProperties


class TestPersonEncapsulation(unittest.TestCase):
    def setUp(self) -> None:
        self.person = Person("alice johnson", 25)

    def test_initial_values_are_normalized_and_readable(self) -> None:
        self.assertEqual(self.person.get_name(), "Alice Johnson")
        self.assertEqual(self.person.get_age(), 25)

    def test_setters_accept_valid_values(self) -> None:
        self.person.set_name("  bob smith  ")
        self.person.set_age(42)
        self.assertEqual(self.person.get_name(), "Bob Smith")
        self.assertEqual(self.person.get_age(), 42)

    def test_invalid_names_are_rejected(self) -> None:
        for name in ("", " ", "A", None, 123):
            with self.subTest(name=name), self.assertRaises(ValueError):
                Person(name, 25)

    def test_invalid_ages_are_rejected(self) -> None:
        for age in (-1, 151, 2.5, "25", None, True):
            with self.subTest(age=age), self.assertRaises(ValueError):
                Person("Alice Johnson", age)

    def test_failed_updates_preserve_existing_values(self) -> None:
        with self.assertRaises(ValueError):
            self.person.set_name("")
        with self.assertRaises(ValueError):
            self.person.set_age(-1)
        self.assertEqual(self.person.get_name(), "Alice Johnson")
        self.assertEqual(self.person.get_age(), 25)

    def test_birthday_increments_age(self) -> None:
        self.person.have_birthday()
        self.assertEqual(self.person.get_age(), 26)

    def test_private_attributes_are_not_directly_available(self) -> None:
        with self.assertRaises(AttributeError):
            _ = self.person.__name
        with self.assertRaises(AttributeError):
            _ = self.person.__age

    def test_direct_assignment_does_not_change_name_mangled_attributes(self) -> None:
        self.person.__name = "Different Name"
        self.person.__age = 999
        self.assertEqual(self.person.__name, "Different Name")
        self.assertEqual(self.person.__age, 999)
        self.assertEqual(self.person.get_name(), "Alice Johnson")
        self.assertEqual(self.person.get_age(), 25)

    def test_age_150_cannot_be_incremented_past_limit(self) -> None:
        person = Person("Older Person", 150)
        with self.assertRaises(ValueError):
            person.have_birthday()
        self.assertEqual(person.get_age(), 150)


class TestPersonWithProperties(unittest.TestCase):
    def setUp(self) -> None:
        self.person = PersonWithProperties("alice johnson", 25)

    def test_properties_get_and_set_values(self) -> None:
        self.assertEqual(self.person.name, "Alice Johnson")
        self.assertEqual(self.person.age, 25)
        self.person.name = "bob smith"
        self.person.age = 30
        self.assertEqual(self.person.name, "Bob Smith")
        self.assertEqual(self.person.age, 30)

    def test_invalid_name_property_values_are_rejected(self) -> None:
        for name in ("", "A", 123):
            with self.subTest(name=name), self.assertRaises(ValueError):
                self.person.name = name

    def test_invalid_age_property_values_are_rejected(self) -> None:
        for age in (-1, 151, "30", True):
            with self.subTest(age=age), self.assertRaises(ValueError):
                self.person.age = age

    def test_property_birthday(self) -> None:
        self.person.have_birthday()
        self.assertEqual(self.person.age, 26)


if __name__ == "__main__":
    unittest.main(verbosity=2)
