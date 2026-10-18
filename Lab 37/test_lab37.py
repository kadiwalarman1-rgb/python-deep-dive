"""Unit tests for Lab 37 constructors and initialization behavior."""

import unittest

from student_class import Student, create_multiple_students
from book_library import Book
from vehicle_system import Vehicle, create_vehicle_fleet
from inventory_system import Product
from default_parameters import Employee


class StudentConstructorTests(unittest.TestCase):
    def test_default_major_and_initial_values(self):
        student = Student("Alice Johnson", 20, "STU001")
        self.assertEqual(student.major, "Undeclared")
        self.assertEqual(student.courses, [])
        self.assertEqual(student.credits, 0)
        self.assertEqual(student.gpa, 0.0)

    def test_course_lists_are_independent(self):
        first, second = create_multiple_students()[:2]
        first.add_course("New Course", 2)
        self.assertNotIn("New Course", [item["name"] for item in second.courses])

    def test_course_and_gpa_validation(self):
        student = Student("Alice", 20, "STU001")
        self.assertTrue(student.add_course("Math", 4))
        self.assertFalse(student.add_course("Math", 3))
        self.assertEqual(student.credits, 4)
        self.assertFalse(student.update_gpa(4.5))
        self.assertTrue(student.update_gpa(3.5))


class BookConstructorTests(unittest.TestCase):
    def test_default_book_fields_and_borrowing(self):
        book = Book("Python", "Author", "ISBN001", 2024, "Technology")
        self.assertEqual(book.pages, 0)
        self.assertEqual(book.price, 0.0)
        self.assertTrue(book.is_available)
        self.assertIn("borrowed by Alice", book.borrow_book("Alice"))
        self.assertFalse(book.is_available)
        self.assertIn("currently borrowed", book.borrow_book("Bob"))
        self.assertIn("returned by Alice", book.return_book())
        self.assertTrue(book.is_available)

    def test_review_average(self):
        book = Book("Python", "Author", "ISBN002", 2024, "Technology")
        book.add_review("Good", 4)
        book.add_review("Excellent", 5)
        self.assertAlmostEqual(book.rating, 4.5)
        self.assertIn("between 1 and 5", book.add_review("Invalid", 7))


class VehicleConstructorTests(unittest.TestCase):
    def test_default_mileage_and_operations(self):
        vehicle = Vehicle("Toyota", "Corolla", 2024, "White")
        self.assertEqual(vehicle.mileage, 0)
        self.assertFalse(vehicle.is_running)
        self.assertIn("not running", vehicle.drive(10))
        vehicle.start_engine()
        vehicle.drive(100)
        self.assertEqual(vehicle.mileage, 100)
        self.assertAlmostEqual(vehicle.fuel_level, 95.0)

    def test_maintenance_lists_are_independent(self):
        vehicles = create_vehicle_fleet()
        vehicles[0].add_maintenance_record("Service", "2026-01-01", 20)
        self.assertEqual(len(vehicles[1].maintenance_records), 2)


class InventoryConstructorTests(unittest.TestCase):
    def test_default_product_values(self):
        product = Product("P001", "Notebook", "Stationery", 4.99)
        self.assertEqual(product.quantity, 0)
        self.assertEqual(product.supplier, "Unknown")
        self.assertEqual(product.calculate_inventory_value(), 0)
        self.assertTrue(product.needs_reorder())

    def test_sales_and_stock_rules(self):
        product = Product("P002", "Pen", "Stationery", 2.0, 5)
        self.assertIn("Sold 3 units", product.sell_product(3))
        self.assertEqual(product.quantity, 2)
        self.assertEqual(product.revenue_generated, 6.0)
        self.assertIn("Insufficient stock", product.sell_product(10))
        self.assertEqual(product.sales_count, 3)


class EmployeeConstructorTests(unittest.TestCase):
    def test_employee_default_parameters(self):
        employee = Employee("Alice Johnson", "EMP001")
        self.assertEqual(employee.department, "General")
        self.assertEqual(employee.position, "Staff")
        self.assertEqual(employee.salary, 50000.0)
        self.assertEqual(employee.hire_date, "Not specified")
        self.assertEqual(employee.email, "alice.johnson@company.com")
        self.assertTrue(employee.is_active)
        self.assertEqual(employee.projects, [])

    def test_rating_project_and_status_methods(self):
        employee = Employee("Bob Smith", "EMP002")
        self.assertEqual(employee.calculate_average_rating(), 0.0)
        employee.add_performance_rating(4, "Q1")
        employee.add_performance_rating(5, "Q2")
        self.assertEqual(employee.calculate_average_rating(), 4.5)
        self.assertIn("assigned", employee.assign_project("Migration", "2026-01-01"))
        self.assertIn("completed", employee.complete_project("Migration"))
        employee.set_active(False)
        self.assertFalse(employee.is_active)
        self.assertIn("between 1 and 5", employee.add_performance_rating(6, "Q3"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
