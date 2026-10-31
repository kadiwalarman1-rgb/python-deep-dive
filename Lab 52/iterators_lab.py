#!/usr/bin/env python3
"""Lab 52: Custom iterators, file processing, built-ins, and itertools."""
import csv
import itertools
import os
import tempfile
from typing import Iterator, Optional, TextIO


class Counter:
    """Yield integers from start (inclusive) to end (exclusive)."""
    def __init__(self, start: int, end: int):
        self.current, self.end = start, end

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


class FibonacciIterator:
    """Yield a finite number of Fibonacci terms."""
    def __init__(self, max_terms: int):
        if max_terms < 0:
            raise ValueError("max_terms must be non-negative")
        self.max_terms = max_terms
        self.count = 0
        self.current, self.next_value = 0, 1

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.count >= self.max_terms:
            raise StopIteration
        value = self.current
        self.current, self.next_value = self.next_value, self.current + self.next_value
        self.count += 1
        return value


SAMPLE_EMPLOYEES = [
    ("John Smith", "Engineering", 75000, 5),
    ("Jane Doe", "Marketing", 65000, 3),
    ("Bob Johnson", "Engineering", 80000, 7),
    ("Alice Brown", "HR", 55000, 2),
    ("Charlie Wilson", "Marketing", 70000, 4),
    ("Diana Davis", "Engineering", 85000, 8),
    ("Eve Miller", "HR", 60000, 6),
    ("Frank Garcia", "Marketing", 72000, 5),
    ("Grace Lee", "Engineering", 78000, 4),
]


def create_sample_data(filename: str = "employee_data.csv") -> None:
    """Create a sample employee CSV using the standard csv module."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Employee", "Department", "Salary", "Years"])
        writer.writerows(SAMPLE_EMPLOYEES)
    print(f"Sample data file {filename!r} created successfully.")


class FileLineIterator:
    """Read a file one line at a time, with explicit early-exit cleanup."""
    def __init__(self, filename: str, encoding: str = "utf-8"):
        self.filename = filename
        self.encoding = encoding
        self.file: Optional[TextIO] = None

    def __iter__(self):
        if self.file is None or self.file.closed:
            self.file = open(self.filename, "r", encoding=self.encoding)
        return self

    def __next__(self) -> str:
        if self.file is None or self.file.closed:
            raise RuntimeError("Call iter() or use a with statement before next().")
        line = self.file.readline()
        if line:
            return line.rstrip("\r\n")
        self.close()
        raise StopIteration

    def close(self) -> None:
        if self.file is not None and not self.file.closed:
            self.file.close()

    def __enter__(self):
        iter(self)
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        self.close()
        return False

    def __del__(self):
        self.close()


class CSVProcessor:
    """Read CSV rows incrementally and calculate employee statistics."""
    def __init__(self, filename: str):
        self.filename = filename

    def process_employees(self) -> dict:
        total_salary = 0
        employee_count = 0
        departments = {}
        with open(self.filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            required = {"Employee", "Department", "Salary", "Years"}
            if not reader.fieldnames or not required.issubset(reader.fieldnames):
                raise ValueError("CSV is missing required employee columns.")
            print("Header:", ",".join(reader.fieldnames))
            for row in reader:
                try:
                    salary, years = int(row["Salary"]), int(row["Years"])
                except (TypeError, ValueError) as error:
                    raise ValueError(f"Invalid numeric values in row: {row}") from error
                name, department = row["Employee"], row["Department"]
                total_salary += salary
                employee_count += 1
                departments.setdefault(department, []).append({
                    "name": name, "salary": salary, "years": years
                })
                print(f"Processed: {name} from {department}")

        average_salary = total_salary / employee_count if employee_count else 0.0
        print("\n=== Employee statistics ===")
        print("Total employees processed:", employee_count)
        print(f"Average salary: {average_salary:,.2f}")
        print("Departments found:", list(departments))
        summary = {}
        for department, employees in departments.items():
            average = sum(item["salary"] for item in employees) / len(employees)
            summary[department] = {"count": len(employees), "average_salary": average}
            print(f"{department}: {len(employees)} employees, average salary: {average:,.2f}")
        return {
            "employee_count": employee_count,
            "total_salary": total_salary,
            "average_salary": average_salary,
            "departments": summary,
        }


class SquareIterator:
    """Yield squares for the inclusive range start through end."""
    def __init__(self, start: int, end: int):
        self.current, self.end = start, end

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current > self.end:
            raise StopIteration
        value = self.current ** 2
        self.current += 1
        return value


class EvenNumberIterator:
    """Yield non-negative even integers up to limit."""
    def __init__(self, limit: int):
        self.current, self.limit = 0, limit

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 2
        return value


class NumberRange:
    """Custom range iterator with an exclusive end value."""
    def __init__(self, start: int, end: int, step: int = 1):
        if step == 0:
            raise ValueError("step cannot be zero")
        if start < end and step < 0:
            raise ValueError("step must be positive when start is less than end")
        if start > end and step > 0:
            raise ValueError("step must be negative when start is greater than end")
        self.current, self.end, self.step = start, end, step

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if (self.step > 0 and self.current >= self.end) or (
            self.step < 0 and self.current <= self.end
        ):
            raise StopIteration
        value = self.current
        self.current += self.step
        return value


class LetterIterator:
    """Yield uppercase letters from start_letter through end_letter."""
    def __init__(self, start_letter: str, end_letter: str):
        if len(start_letter) != 1 or len(end_letter) != 1:
            raise ValueError("Letters must be single characters.")
        self.current, self.end = ord(start_letter.upper()), ord(end_letter.upper())
        if self.current > self.end:
            raise ValueError("start_letter must not come after end_letter")

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.current > self.end:
            raise StopIteration
        value = chr(self.current)
        self.current += 1
        return value


class DatabaseIterator:
    """Simulate a database cursor that yields namespaced records."""
    def __init__(self, table_name: str, records: list):
        self.table_name, self.records, self.index = table_name, records, 0

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.index >= len(self.records):
            raise StopIteration
        value = f"{self.table_name}:{self.records[self.index]}"
        self.index += 1
        return value


def demo_counter() -> None:
    print("\n=== TASK 1: COUNTER ITERATOR ===")
    counter = Counter(1, 6)
    print("Using next():", next(counter), next(counter), next(counter))
    print("Using for loop:")
    for number in Counter(10, 15):
        print("Count:", number)


def demo_fibonacci() -> None:
    print("\n=== TASK 2: FIBONACCI ITERATOR ===")
    print("First 10:", list(FibonacciIterator(10)))
    for index, value in enumerate(FibonacciIterator(7), start=1):
        print(f"F({index}) = {value}")


def demo_file_processing() -> None:
    print("\n=== TASK 3: FILE ITERATOR AND CSV PROCESSING ===")
    with tempfile.TemporaryDirectory(prefix="lab52_") as directory:
        filename = os.path.join(directory, "employee_data.csv")
        create_sample_data(filename)
        CSVProcessor(filename).process_employees()
        print("\nDirect file iterator usage (first 3 lines):")
        with FileLineIterator(filename) as iterator:
            for index, line in enumerate(iterator):
                if index >= 3:
                    break
                print(f"Line {index + 1}: {line}")


def demo_builtin_functions() -> None:
    print("\n=== TASK 4: BUILT-IN FUNCTIONS WITH ITERATORS ===")
    print("Squares:", list(SquareIterator(1, 5)))
    even_numbers = EvenNumberIterator(10)
    print("First three even numbers:", next(even_numbers), next(even_numbers), next(even_numbers))
    small = SquareIterator(1, 2)
    print("next() with default:",
          next(small, "No more values"),
          next(small, "No more values"),
          next(small, "No more values"))
    print("Sum of squares 1..4:", sum(SquareIterator(1, 4)))
    values = list(EvenNumberIterator(8))
    print("Even numbers:", values, "max:", max(values), "min:", min(values))
    squares = list(SquareIterator(1, 3))
    print("Squares:", squares)
    print("Any square > 5?", any(value > 5 for value in squares))
    print("All squares > 0?", all(value > 0 for value in squares))
    print("Enumerate even numbers:")
    for index, value in enumerate(EvenNumberIterator(6)):
        print(f"Index {index}: {value}")


def demo_iterator_exhaustion() -> None:
    print("\n=== ITERATOR EXHAUSTION ===")
    iterator = SquareIterator(1, 3)
    print("First iteration:", list(iterator))
    print("Second iteration of same iterator:", list(iterator))
    print("New iterator:", list(SquareIterator(1, 3)))


def demo_itertools_chain() -> None:
    print("\n=== TASK 5: itertools.chain() ===")
    combined = itertools.chain(
        NumberRange(1, 4), NumberRange(10, 13), LetterIterator("A", "C")
    )
    print("Chained values:", list(combined))
    mixed = itertools.chain(NumberRange(20, 23), [100, 200, 300], ("X", "Y", "Z"))
    print("Custom and built-in iterables:", list(mixed))
    sources = [NumberRange(1, 3), ["a", "b", "c"], (10, 20, 30), LetterIterator("X", "Z")]
    print("chain.from_iterable():", list(itertools.chain.from_iterable(sources)))


def demo_other_itertools() -> None:
    print("\n=== OTHER itertools FUNCTIONS ===")
    print("count():", list(itertools.islice(itertools.count(10, 2), 5)))
    print("cycle():", list(itertools.islice(itertools.cycle(["red", "green", "blue"]), 8)))
    print("repeat():", list(itertools.repeat("hello", 4)))
    print("islice():", list(itertools.islice(NumberRange(1, 20), 4, 10)))
    print("takewhile():", list(itertools.takewhile(lambda x: x < 15, NumberRange(10, 25))))
    print("dropwhile():", list(itertools.dropwhile(lambda x: x < 15, NumberRange(10, 20))))


def demo_multiple_data_sources() -> None:
    print("\n=== PRACTICAL EXAMPLE: MULTIPLE DATA SOURCES ===")
    streams = [
        DatabaseIterator("users", ["john", "jane", "bob"]),
        DatabaseIterator("products", ["laptop", "mouse", "keyboard"]),
        DatabaseIterator("orders", ["order1", "order2"]),
    ]
    for record in itertools.chain(*streams):
        print("Processing:", record)

    print("Admin-related records:")
    combined = itertools.chain(
        DatabaseIterator("users", ["admin", "guest", "user1"]),
        DatabaseIterator("products", ["admin_tool", "user_app"]),
    )
    for record in itertools.filterfalse(lambda item: "admin" not in item.lower(), combined):
        print(record)


def main() -> None:
    print("LAB 52: ITERATORS AND ITERABLES — COMPLETE DEMONSTRATION")
    print("=" * 64)
    demo_counter()
    demo_fibonacci()
    demo_file_processing()
    demo_builtin_functions()
    demo_iterator_exhaustion()
    demo_itertools_chain()
    demo_other_itertools()
    demo_multiple_data_sources()
    print("\n" + "=" * 64)
    print("LAB COMPLETED SUCCESSFULLY!")


if __name__ == "__main__":
    main()
