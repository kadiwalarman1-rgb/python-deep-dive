import math
import unittest

import mathtools
from mathtools import Circle, Rectangle, add, subtract, multiply, divide, power
from mathtools.statistics import mean, median, mode, range_value, variance, standard_deviation


class MathToolsTests(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(add(15, 25), 40)
        self.assertEqual(subtract(50, 20), 30)
        self.assertEqual(multiply(7, 8), 56)
        self.assertEqual(divide(100, 4), 25)
        self.assertEqual(power(3, 4), 81)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_circle(self):
        circle = Circle(7)
        self.assertAlmostEqual(circle.area(), math.pi * 49)
        self.assertAlmostEqual(circle.circumference(), 14 * math.pi)
        self.assertEqual(circle.diameter(), 14)
        with self.assertRaises(ValueError):
            Circle(0)

    def test_rectangle_and_triangle(self):
        rectangle = Rectangle(12, 8)
        self.assertEqual(rectangle.area(), 96)
        self.assertEqual(rectangle.perimeter(), 40)
        self.assertFalse(rectangle.is_square())
        self.assertTrue(Rectangle(6, 6).is_square())
        self.assertEqual(mathtools.calculate_triangle_area(12, 9), 54)
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_statistics(self):
        values = [2, 4, 4, 4, 5, 5, 7, 9]
        self.assertEqual(mean(values), 5)
        self.assertEqual(median(values), 4.5)
        self.assertEqual(mode(values), 4)
        self.assertEqual(range_value(values), 7)
        self.assertAlmostEqual(variance(values), 32 / 7)
        self.assertAlmostEqual(standard_deviation(values), math.sqrt(32 / 7))
        self.assertEqual(median([1, 3, 5]), 3)
        self.assertEqual(mode([1, 1, 2, 2]), [1, 2])

    def test_empty_or_short_statistics(self):
        for function in (mean, median, mode, range_value):
            with self.subTest(function=function.__name__):
                with self.assertRaises(ValueError):
                    function([])
        with self.assertRaises(ValueError):
            variance([5])

    def test_package_metadata(self):
        info = mathtools.get_package_info()
        self.assertEqual(info["name"], "mathtools")
        self.assertIn("geometry", info["modules"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
