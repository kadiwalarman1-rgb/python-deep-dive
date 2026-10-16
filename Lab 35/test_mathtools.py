import math
import unittest

import mathtools


class MathToolsTests(unittest.TestCase):
    def test_arithmetic(self):
        self.assertEqual(mathtools.add(5, 3), 8)
        self.assertEqual(mathtools.subtract(10, 4), 6)
        self.assertEqual(mathtools.multiply(6, 7), 42)
        self.assertEqual(mathtools.divide(15, 3), 5)
        self.assertEqual(mathtools.power(2, 3), 8)
        self.assertEqual(mathtools.factorial(5), 120)
        self.assertEqual(mathtools.factorial(0), 1)
        with self.assertRaises(ValueError):
            mathtools.divide(10, 0)
        with self.assertRaises(ValueError):
            mathtools.factorial(-1)
        with self.assertRaises(TypeError):
            mathtools.factorial(2.5)

    def test_algebra(self):
        roots = mathtools.solve_quadratic(1, -5, 6)
        self.assertTrue(math.isclose(roots[0], 3.0))
        self.assertTrue(math.isclose(roots[1], 2.0))
        self.assertEqual(mathtools.solve_linear(2, -6), 3)
        self.assertEqual(mathtools.evaluate_polynomial([1, 2, 3], 2), 17)
        self.assertEqual(mathtools.find_slope(1, 2, 3, 6), 2)
        self.assertEqual(mathtools.distance_between_points(0, 0, 3, 4), 5)
        with self.assertRaises(ValueError):
            mathtools.solve_quadratic(0, 2, 1)
        with self.assertRaises(ValueError):
            mathtools.solve_linear(0, 2)
        complex_roots = mathtools.solve_quadratic(1, 0, 1)
        self.assertTrue(all(isinstance(root, complex) for root in complex_roots))

    def test_geometry(self):
        self.assertTrue(math.isclose(mathtools.circle_area(5), math.pi * 25))
        self.assertTrue(math.isclose(mathtools.circle_circumference(5), 2 * math.pi * 5))
        self.assertEqual(mathtools.rectangle_area(5, 3), 15)
        self.assertEqual(mathtools.rectangle_perimeter(5, 3), 16)
        self.assertEqual(mathtools.triangle_area(6, 4), 12)
        self.assertTrue(math.isclose(mathtools.triangle_area_heron(3, 4, 5), 6))
        self.assertTrue(math.isclose(mathtools.sphere_volume(3), (4 / 3) * math.pi * 27))
        self.assertTrue(math.isclose(mathtools.sphere_surface_area(3), 4 * math.pi * 9))
        self.assertTrue(math.isclose(mathtools.cylinder_volume(2, 5), 20 * math.pi))
        self.assertEqual(mathtools.rectangular_prism_volume(3, 4, 5), 60)
        with self.assertRaises(ValueError):
            mathtools.circle_area(-1)
        with self.assertRaises(ValueError):
            mathtools.triangle_area_heron(1, 2, 5)

    def test_package_info(self):
        info = mathtools.get_package_info()
        self.assertEqual(info["name"], "mathtools")
        self.assertEqual(info["version"], mathtools.__version__)
        functions = mathtools.list_functions()
        self.assertIn("factorial", functions["arithmetic"])
        self.assertIn("find_slope", functions["algebra"])
        self.assertIn("cylinder_volume", functions["geometry"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
