"""Automated tests for Lab 50 generator examples."""
import csv
import os
import tempfile
import unittest

from generators_lab import (
    fibonacci_list, fibonacci_generator, infinite_fibonacci,
    countdown_generator, limited_generator, file_line_generator,
    filtered_lines_generator, word_generator, csv_row_generator,
    filtered_csv_generator
)


class GeneratorsLabTests(unittest.TestCase):
    def test_fibonacci_list_and_generator(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(fibonacci_list(10), expected)
        self.assertEqual(list(fibonacci_generator(10)), expected)
        self.assertEqual(fibonacci_list(0), [])
        with self.assertRaises(ValueError):
            fibonacci_list(-1)

    def test_infinite_fibonacci_is_lazy(self):
        generator = infinite_fibonacci()
        self.assertEqual([next(generator) for _ in range(7)], [0, 1, 1, 2, 3, 5, 8])

    def test_countdown_and_next_default(self):
        self.assertEqual(list(countdown_generator(3)), [3, 2, 1, "Blast off!"])
        generator = limited_generator()
        self.assertEqual(next(generator, "empty"), "First")
        self.assertEqual([next(generator, "empty") for _ in range(4)],
                         ["Second", "Third", "empty", "empty"])

    def test_text_file_generators(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "sample.txt")
            with open(path, "w", encoding="utf-8") as file:
                file.write("Python generators save memory.\nSecond sample line!\n")
            self.assertEqual(list(file_line_generator(path)),
                             [(1, "Python generators save memory."), (2, "Second sample line!")])
            self.assertEqual(list(filtered_lines_generator(path, pattern="sample")),
                             [(2, "Second sample line!")])
            words = list(word_generator(path))
            self.assertIn((1, "python"), words)
            self.assertIn((2, "line"), words)

    def test_csv_row_and_filter_generators(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "staff.csv")
            with open(path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Department", "Salary", "Years"])
                writer.writerow(["1", "Asha", "Engineering", "90000", "3"])
                writer.writerow(["2", "Ravi", "Sales", "50000", "2"])
            self.assertEqual(sum(1 for _ in csv_row_generator(path)), 2)
            filtered = list(filtered_csv_generator(path, department="Engineering"))
            self.assertEqual(len(filtered), 1)
            self.assertEqual(filtered[0]["Name"], "Asha")
            self.assertEqual(sum(1 for _ in filtered_csv_generator(path, min_salary=80000)), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
