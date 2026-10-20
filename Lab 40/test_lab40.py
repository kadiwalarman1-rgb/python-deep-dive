"""Automated tests for the Lab 40 polymorphism examples."""

import math
import unittest

from shapes import (
    Shape,
    Circle,
    Rectangle,
    Triangle,
    Square,
    calculate_and_display_area,
    comprehensive_polymorphism_test,
)


class ShapeTests(unittest.TestCase):
    def test_base_shape_area_requires_implementation(self):
        shape = Shape("Custom")
        with self.assertRaises(NotImplementedError):
            shape.area()

    def test_circle_area_and_radius(self):
        circle = Circle(5)
        self.assertEqual(circle.name, "Circle")
        self.assertEqual(circle.get_radius(), 5)
        self.assertAlmostEqual(circle.area(), math.pi * 25)

    def test_rectangle_area_and_dimensions(self):
        rectangle = Rectangle(4, 6)
        self.assertEqual(rectangle.get_dimensions(), (4, 6))
        self.assertEqual(rectangle.area(), 24)

    def test_triangle_area_and_dimensions(self):
        triangle = Triangle(6, 8)
        self.assertEqual(triangle.get_dimensions(), (6, 8))
        self.assertEqual(triangle.area(), 24)

    def test_square_inherits_rectangle(self):
        square = Square(4)
        self.assertIsInstance(square, Rectangle)
        self.assertIsInstance(square, Shape)
        self.assertEqual(square.name, "Square")
        self.assertEqual(square.get_side(), 4)
        self.assertEqual(square.area(), 16)

    def test_polymorphic_area_calls(self):
        shapes = [Circle(2), Rectangle(3, 4), Triangle(6, 8), Square(3)]
        areas = [shape.area() for shape in shapes]
        self.assertAlmostEqual(areas[0], math.pi * 4)
        self.assertEqual(areas[1:], [12, 24, 9])

    def test_invalid_dimensions_are_rejected(self):
        invalid_values = [0, -1, float("inf"), float("nan"), True, "3"]
        for value in invalid_values:
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    Circle(value)
                with self.assertRaises(ValueError):
                    Rectangle(value, 2)
                with self.assertRaises(ValueError):
                    Triangle(2, value)
                with self.assertRaises(ValueError):
                    Square(value)

    def test_demo_functions_run(self):
        calculate_and_display_area(Circle(1))
        comprehensive_polymorphism_test()


if __name__ == "__main__":
    unittest.main(verbosity=2)
