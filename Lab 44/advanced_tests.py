#!/usr/bin/env python3
"""Lab 44: Advanced tests for arithmetic and comparison operators."""

from vector_class import Vector


def test_all_operators():
    print("=== Advanced Operator Testing ===")
    v1, v2, v3 = Vector(6, 8), Vector(3, 4), Vector(1, 1)

    print(f"v1 = {v1} (magnitude: {v1.magnitude():.2f})")
    print(f"v2 = {v2} (magnitude: {v2.magnitude():.2f})")
    print(f"v3 = {v3} (magnitude: {v3.magnitude():.2f})")
    print()

    print("--- Arithmetic Operations ---")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v2 - v1 = {v2 - v1}")
    print()

    print("--- Scalar Operations ---")
    print(f"v1 * 0.5 = {v1 * 0.5}")
    print(f"2 * v2 = {2 * v2}")
    print(f"v1 / 2 = {v1 / 2}")
    print()

    print("--- Dot Product ---")
    print(f"v1 * v2 = {v1 * v2}")
    print(f"v2 * v3 = {v2 * v3}")
    print()

    print("--- Comparisons ---")
    print(f"v1 == v2: {v1 == v2}")
    print(f"v3 < v2: {v3 < v2}")
    print(f"v2 < v1: {v2 < v1}")
    print()

    print("--- Complex Expressions ---")
    unit_v1 = v1 / v1.magnitude()
    print(f"Unit vector of v1: {unit_v1} (magnitude: {unit_v1.magnitude():.6f})")
    perpendicular = Vector(-v1.y, v1.x)
    print(f"Perpendicular to v1: {perpendicular}")
    print(f"Dot product (should be 0): {v1 * perpendicular}")

    print("\n--- Error Handling ---")
    try:
        _ = v1 / 0
    except ZeroDivisionError as error:
        print(f"Division by zero caught: {error}")
    try:
        _ = v1 + "invalid"
    except TypeError as error:
        print(f"Type error caught: {error}")


if __name__ == "__main__":
    test_all_operators()
