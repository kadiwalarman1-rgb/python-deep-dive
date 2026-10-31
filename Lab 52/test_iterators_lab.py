"""Automated tests for Lab 52 custom iterators and file processing."""
import os
import tempfile
import unittest

from iterators_lab import (
    Counter, FibonacciIterator, FileLineIterator, CSVProcessor,
    SquareIterator, EvenNumberIterator, NumberRange, LetterIterator,
    DatabaseIterator, create_sample_data
)


class IteratorLabTests(unittest.TestCase):
    def test_counter_iteration_and_exhaustion(self):
        iterator = Counter(2, 5)
        self.assertEqual(list(iterator), [2, 3, 4])
        self.assertEqual(list(iterator), [])
        self.assertEqual(list(Counter(5, 5)), [])

    def test_fibonacci_iterator(self):
        self.assertEqual(list(FibonacciIterator(10)), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertEqual(list(FibonacciIterator(0)), [])
        with self.assertRaises(ValueError):
            FibonacciIterator(-1)

    def test_file_iterator_reads_and_closes_at_eof(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "lines.txt")
            with open(path, "w", encoding="utf-8") as file:
                file.write("alpha\nbeta\n")
            iterator = FileLineIterator(path)
            self.assertEqual(list(iterator), ["alpha", "beta"])
            self.assertTrue(iterator.file.closed)

    def test_file_iterator_closes_on_early_exit(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "lines.txt")
            with open(path, "w", encoding="utf-8") as file:
                file.write("one\ntwo\n")
            with FileLineIterator(path) as iterator:
                self.assertEqual(next(iterator), "one")
            self.assertTrue(iterator.file.closed)

    def test_csv_processor_statistics(self):
        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "employees.csv")
            create_sample_data(path)
            stats = CSVProcessor(path).process_employees()
            self.assertEqual(stats["employee_count"], 9)
            self.assertEqual(stats["total_salary"], 640000)
            self.assertAlmostEqual(stats["average_salary"], 640000 / 9)
            self.assertEqual(stats["departments"]["Engineering"]["count"], 4)

    def test_square_and_even_iterators(self):
        self.assertEqual(list(SquareIterator(1, 5)), [1, 4, 9, 16, 25])
        self.assertEqual(list(EvenNumberIterator(8)), [0, 2, 4, 6, 8])
        self.assertEqual(sum(SquareIterator(1, 4)), 30)

    def test_number_range_and_letters(self):
        self.assertEqual(list(NumberRange(1, 4)), [1, 2, 3])
        self.assertEqual(list(NumberRange(5, 0, -2)), [5, 3, 1])
        self.assertEqual(list(LetterIterator("A", "C")), ["A", "B", "C"])
        with self.assertRaises(ValueError):
            NumberRange(1, 5, 0)
        with self.assertRaises(ValueError):
            LetterIterator("C", "A")

    def test_database_iterator_is_exhaustible(self):
        iterator = DatabaseIterator("users", ["alice", "bob"])
        self.assertEqual(list(iterator), ["users:alice", "users:bob"])
        self.assertEqual(list(iterator), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
