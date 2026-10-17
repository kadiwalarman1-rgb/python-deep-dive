import unittest

from enhanced_person import Person
from multiple_persons import Person as BasicPerson
from object_experiments import Vehicle
from self_demo import Counter
from student_system import Student


class Lab36Tests(unittest.TestCase):
    def test_basic_person_and_independence(self):
        first = BasicPerson("Alice", 25)
        second = BasicPerson("Bob", 30)
        first.have_birthday()
        self.assertEqual(first.age, 26)
        self.assertEqual(second.age, 30)

    def test_enhanced_person(self):
        person = Person("Emma", 28, "Engineer", "Surat")
        self.assertTrue(person.is_adult())
        self.assertEqual(person.get_age_group(), "Adult")
        self.assertTrue(person.add_friend("John"))
        self.assertFalse(person.add_friend("John"))
        person.change_occupation("Developer")
        person.move_to_city("Ahmedabad")
        self.assertEqual(person.occupation, "Developer")
        self.assertEqual(person.city, "Ahmedabad")

    def test_counter_state(self):
        counter = Counter(2)
        counter.increment()
        counter.add_value(4)
        self.assertEqual(counter.get_value(), 7)
        counter.reset()
        self.assertEqual(counter.get_value(), 0)

    def test_student_grades_and_gpa(self):
        student = Student("S001", "Alice", 20)
        self.assertTrue(student.enroll_course("Python"))
        self.assertFalse(student.enroll_course("Python"))
        self.assertTrue(student.add_grade("Python", 95))
        self.assertTrue(student.add_grade("Linux", 85))
        self.assertEqual(student.calculate_gpa(), 3.5)
        self.assertEqual(student.get_academic_status(), "Dean's List")
        self.assertFalse(student.add_grade("Invalid", 120))

    def test_vehicle_state(self):
        vehicle = Vehicle("Toyota", "Camry", 2020)
        self.assertFalse(vehicle.drive(5))
        vehicle.start_engine()
        self.assertTrue(vehicle.drive(20))
        self.assertEqual(vehicle.mileage, 20)
        vehicle.stop_engine()
        self.assertFalse(vehicle.is_running)
        vehicle.paint_vehicle("Silver")
        self.assertEqual(vehicle.color, "Silver")

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            BasicPerson("", 20)
        with self.assertRaises(ValueError):
            Student("S002", "Bob", -1)
        with self.assertRaises(ValueError):
            Vehicle("Toyota", "Camry", 2020).drive(-2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
