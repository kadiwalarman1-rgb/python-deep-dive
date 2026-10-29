#!/usr/bin/env python3
"""Lab 50: Python generators, lazy pipelines, memory, performance, files, and CSV."""
import csv
import os
import random
import re
import sys
import time
from typing import Iterator, Optional, Tuple


def fibonacci_list(n: int) -> list:
    """Return the first n Fibonacci values in a list."""
    if n < 0:
        raise ValueError("n must be non-negative")
    result, a, b = [], 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def fibonacci_generator(n: int) -> Iterator[int]:
    """Yield the first n Fibonacci values lazily."""
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def infinite_fibonacci() -> Iterator[int]:
    """Yield Fibonacci values indefinitely."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def countdown_generator(start: int) -> Iterator[object]:
    """Yield a countdown, then a final message."""
    if start < 0:
        raise ValueError("start must be non-negative")
    while start > 0:
        yield start
        start -= 1
    yield "Blast off!"


def limited_generator() -> Iterator[str]:
    yield "First"
    yield "Second"
    yield "Third"


def demo_fibonacci() -> None:
    print("\n=== Fibonacci: list vs generator ===")
    values = fibonacci_list(10)
    print("List type:", type(values))
    print("List values:", values)
    generator = fibonacci_generator(10)
    print("Generator type:", type(generator))
    print("Generator values:", list(generator))

    print("\n=== Infinite Fibonacci, first 15 values ===")
    infinite = infinite_fibonacci()
    for index in range(15):
        print(f"F({index}) = {next(infinite)}")
    print("Next value:", next(infinite))


def demo_next() -> None:
    print("\n=== Manual next() and StopIteration ===")
    countdown = countdown_generator(5)
    try:
        while True:
            print("Countdown:", next(countdown))
    except StopIteration:
        print("Generator exhausted: StopIteration caught.")

    print("\n=== next() with default ===")
    generator = limited_generator()
    for index in range(1, 6):
        print(f"Call {index}: {next(generator, 'No more values')}")


def demo_expressions() -> None:
    print("\n=== List comprehension vs generator expression ===")
    squares_list = [number ** 2 for number in range(10)]
    squares_gen = (number ** 2 for number in range(10))
    print("List:", squares_list)
    print("List shallow size:", sys.getsizeof(squares_list), "bytes")
    print("Generator object shallow size:", sys.getsizeof(squares_gen), "bytes")
    print("Generator values:", list(squares_gen))
    print("After exhaustion:", list(squares_gen))

    print("\n=== Advanced lazy pipelines ===")
    even_squares = (number ** 2 for number in range(20) if number % 2 == 0)
    print("Even squares:", list(even_squares))
    words = ["hello", "world", "python", "generator", "expression"]
    long_words = (word.upper() for word in words if len(word) > 5)
    print("Long uppercase words:", list(long_words))
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    odd_numbers = (number for row in matrix for number in row if number % 2)
    print("Odd matrix values:", list(odd_numbers))
    multiples = (number for number in range(100) if number % 3 == 0)
    squared = (number ** 2 for number in multiples)
    limited = (number for number in squared if number < 1000)
    print("Pipeline result:", list(limited))


def create_large_list(n: int) -> list:
    return [number ** 2 for number in range(n)]


def create_large_generator(n: int) -> Iterator[int]:
    for number in range(n):
        yield number ** 2


def demo_memory(n: int = 1_000_000) -> None:
    print(f"\n=== Memory experiment for {n:,} squares ===")
    start = time.perf_counter()
    values = create_large_list(n)
    list_time = time.perf_counter() - start
    list_size = sys.getsizeof(values)

    start = time.perf_counter()
    generator = create_large_generator(n)
    generator_time = time.perf_counter() - start
    generator_size = sys.getsizeof(generator)

    print(f"List construction: {list_time:.4f}s")
    print(f"List shallow container size: {list_size:,} bytes")
    print(f"Generator creation: {generator_time:.6f}s")
    print(f"Generator object size: {generator_size:,} bytes")
    print("Note: sys.getsizeof() is shallow; it excludes referenced list items.")
    del values, generator


def sum_with_list(n: int) -> int:
    return sum([number for number in range(n)])


def sum_with_generator(n: int) -> int:
    return sum(number for number in range(n))


def sum_with_generator_function(n: int) -> int:
    def numbers() -> Iterator[int]:
        for number in range(n):
            yield number
    return sum(numbers())


def demo_performance(n: int = 1_000_000) -> None:
    print(f"\n=== Summation performance for range({n:,}) ===")
    methods = [
        ("List", lambda: sum_with_list(n)),
        ("Generator expression", lambda: sum_with_generator(n)),
        ("Generator function", lambda: sum_with_generator_function(n)),
        ("Built-in range", lambda: sum(range(n))),
    ]
    results = []
    for name, function in methods:
        start = time.perf_counter()
        value = function()
        elapsed = time.perf_counter() - start
        results.append(value)
        print(f"{name:24} result={value:,} time={elapsed:.4f}s")
    print("All results match:", len(set(results)) == 1)


def create_large_file(filename: str = "large_sample.txt", num_lines: int = 100_000) -> None:
    if num_lines < 0:
        raise ValueError("num_lines must be non-negative")
    with open(filename, "w", encoding="utf-8") as file:
        for index in range(num_lines):
            file.write(f"This is line {index + 1} with sample data for testing generators.\n")
    print(f"Created {filename} with {num_lines:,} lines.")


def read_file_all_at_once(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as file:
        return file.readlines()


def file_line_generator(filename: str, encoding: str = "utf-8") -> Iterator[Tuple[int, str]]:
    """Yield (1-based line number, stripped line) from a text file."""
    with open(filename, "r", encoding=encoding) as file:
        for line_number, line in enumerate(file, start=1):
            yield line_number, line.rstrip("\r\n")


def filtered_lines_generator(filename: str, pattern: Optional[str] = None,
                             min_length: int = 0) -> Iterator[Tuple[int, str]]:
    if min_length < 0:
        raise ValueError("min_length must be non-negative")
    compiled_pattern = re.compile(pattern, re.IGNORECASE) if pattern else None
    for line_number, line in file_line_generator(filename):
        if len(line) < min_length:
            continue
        if compiled_pattern and not compiled_pattern.search(line):
            continue
        yield line_number, line


def word_generator(filename: str) -> Iterator[Tuple[int, str]]:
    for line_number, line in file_line_generator(filename):
        for word in line.split():
            cleaned = re.sub(r"[^\w]", "", word)
            if cleaned:
                yield line_number, cleaned.lower()


def take(iterator, count: int):
    for _ in range(count):
        try:
            yield next(iterator)
        except StopIteration:
            return


def demo_file_reading(filename: str = "large_sample.txt") -> None:
    if not os.path.isfile(filename):
        print(f"File {filename!r} not found; creating a small sample file first.")
        create_large_file(filename, 1_000)

    print(f"\n=== Text file processing: {filename} ===")
    start = time.perf_counter()
    lines = read_file_all_at_once(filename)
    list_words = sum(len(line.split()) for line in lines)
    list_elapsed = time.perf_counter() - start
    list_shallow = sys.getsizeof(lines)

    start = time.perf_counter()
    generator_words = sum(len(line.split()) for _, line in file_line_generator(filename))
    generator_elapsed = time.perf_counter() - start
    print(f"File size: {os.path.getsize(filename):,} bytes")
    print(f"Whole-file word count: {list_words:,}; time: {list_elapsed:.4f}s")
    print(f"Streaming word count: {generator_words:,}; time: {generator_elapsed:.4f}s")
    print(f"Word counts match: {list_words == generator_words}")
    print(f"List shallow size: {list_shallow:,} bytes (not total process memory)")

    print("\nFirst five lines:")
    for number, line in take(file_line_generator(filename), 5):
        print(f"{number}: {line[:80]}")
    print("\nFirst three lines containing 'sample':")
    for number, line in take(filtered_lines_generator(filename, pattern="sample"), 3):
        print(f"{number}: {line}")
    unique_words = set()
    for _, word in word_generator(filename):
        unique_words.add(word)
        if len(unique_words) >= 10:
            break
    print("\nFirst unique words:", sorted(unique_words))
    line_count = sum(1 for _ in file_line_generator(filename))
    word_count = sum(1 for _ in word_generator(filename))
    long_line_count = sum(1 for _ in filtered_lines_generator(filename, min_length=50))
    print(f"Line count: {line_count:,}; word count: {word_count:,}; lines >=50 chars: {long_line_count:,}")


def create_sample_csv(filename: str = "employees.csv", num_records: int = 50_000, seed: int = 42) -> None:
    if num_records < 0:
        raise ValueError("num_records must be non-negative")
    rng = random.Random(seed)
    departments = ["Engineering", "Marketing", "Sales", "HR", "Finance"]
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Department", "Salary", "Years"])
        for index in range(num_records):
            writer.writerow([
                index + 1, f"Employee_{index + 1:05d}", rng.choice(departments),
                rng.randint(30_000, 120_000), rng.randint(1, 20)
            ])
    print(f"Created {filename} with {num_records:,} records.")


def csv_row_generator(filename: str) -> Iterator[dict]:
    with open(filename, "r", newline="", encoding="utf-8") as file:
        yield from csv.DictReader(file)


def filtered_csv_generator(filename: str, department: Optional[str] = None,
                           min_salary: Optional[int] = None) -> Iterator[dict]:
    for row in csv_row_generator(filename):
        try:
            salary = int(row["Salary"])
        except (KeyError, ValueError) as error:
            raise ValueError("CSV must contain a numeric Salary column") from error
        if department is not None and row.get("Department") != department:
            continue
        if min_salary is not None and salary < min_salary:
            continue
        yield row


def demo_csv(filename: str = "employees.csv") -> None:
    if not os.path.isfile(filename):
        print(f"File {filename!r} not found; creating sample CSV data first.")
        create_sample_csv(filename, 5_000)

    print(f"\n=== CSV processing: {filename} ===")
    start = time.perf_counter()
    with open(filename, "r", newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    list_elapsed = time.perf_counter() - start
    list_average = sum(int(row["Salary"]) for row in rows) / len(rows) if rows else 0

    start = time.perf_counter()
    count = total_salary = 0
    for row in csv_row_generator(filename):
        total_salary += int(row["Salary"])
        count += 1
    gen_elapsed = time.perf_counter() - start
    gen_average = total_salary / count if count else 0

    print(f"Traditional: {len(rows):,} records, average salary {list_average:,.2f}, {list_elapsed:.4f}s")
    print(f"Generator:   {count:,} records, average salary {gen_average:,.2f}, {gen_elapsed:.4f}s")
    print("Counts match:", len(rows) == count, "| averages match:", abs(list_average - gen_average) < 0.01)

    engineering = list(take(filtered_csv_generator(filename, department="Engineering"), 3))
    print("\nFirst engineering employees:")
    for row in engineering:
        print(f"  {row['Name']}: salary {int(row['Salary']):,}")
    high_earners = sum(1 for _ in filtered_csv_generator(filename, min_salary=80_001))
    print(f"Employees earning more than 80,000: {high_earners:,}")


def main() -> None:
    print("Python Generators Lab — Complete Demonstration")
    print("=" * 56)
    demo_fibonacci()
    demo_next()
    demo_expressions()
    demo_memory()
    demo_performance()
    demo_file_reading()
    demo_csv()
    print("\n" + "=" * 56)
    print("LAB COMPLETED SUCCESSFULLY!")


if __name__ == "__main__":
    main()
