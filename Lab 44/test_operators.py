#!/usr/bin/env python3
"""Lab 44: Practical tests for overloaded vector operators."""

from vector_class import Vector


def test_vector_creation():
    print("=== Testing Vector Creation ===")
    v1 = Vector(5, 12)
    v2 = Vector(-3, 4)
    print(f"Created v1: {v1}")
    print(f"Created v2: {v2}")
    print()


def test_addition():
    print("=== Testing Addition Operator ===")
    v1, v2, v3 = Vector(2, 3), Vector(4, 5), Vector(-1, 2)
    print(f"{v1} + {v2} = {v1 + v2}")
    print(f"{v1} + {v2} + {v3} = {v1 + v2 + v3}")
    print(f"Chain addition: {Vector(1, 1) + Vector(2, 2) + Vector(3, 3)}")
    print()


def test_equality():
    print("=== Testing Equality Operator ===")
    v1, v2, v3 = Vector(3, 4), Vector(3, 4), Vector(4, 3)
    print(f"{v1} == {v2}: {v1 == v2}")
    print(f"{v1} == {v3}: {v1 == v3}")
    v4, v5 = Vector(1, 2), Vector(2, 2)
    computed = v4 + v5
    print(f"{v1} == ({v4} + {v5}): {v1 == computed}")
    print()


def test_less_than():
    print("=== Testing Less-Than Operator ===")
    vectors = [Vector(1, 1), Vector(3, 4), Vector(0, 5), Vector(6, 8)]
    for vector in vectors:
        print(f"{vector} has magnitude {vector.magnitude():.2f}")

    print("\nComparisons:")
    print(f"{vectors[0]} < {vectors[1]}: {vectors[0] < vectors[1]}")
    print(f"{vectors[1]} < {vectors[2]}: {vectors[1] < vectors[2]}")
    print(f"{vectors[2]} < {vectors[3]}: {vectors[2] < vectors[3]}")
    print()


def test_combined_operations():
    print("=== Testing Combined Operations ===")
    v1, v2, v3 = Vector(1, 2), Vector(2, 3), Vector(3, 4)
    result = v1 + v2
    print(f"Step 1: {v1} + {v2} = {result}")
    print(f"Step 2: {result} == Vector(3, 5): {result == Vector(3, 5)}")
    print(f"Step 3: {result} < {v3}: {result < v3}")
    print(f"Step 4: {result} + {v3} = {result + v3}")
    print()


def test_error_handling():
    print("=== Testing Error Handling ===")
    try:
        Vector(1, 2) / 0
    except ZeroDivisionError as error:
        print(f"Division by zero caught: {error}")

    try:
        Vector(1, 2) + "invalid"
    except TypeError as error:
        print(f"Type error caught: {error}")


if __name__ == "__main__":
    test_vector_creation()
    test_addition()
    test_equality()
    test_less_than()
    test_combined_operations()
    test_error_handling()
    print("=== All Tests Completed ===")
