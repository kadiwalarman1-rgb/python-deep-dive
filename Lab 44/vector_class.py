#!/usr/bin/env python3
"""Lab 44: Vector class demonstrating Python operator overloading."""

import math


class Vector:
    """A two-dimensional vector with overloaded operators."""

    def __init__(self, x, y):
        if isinstance(x, bool) or not isinstance(x, (int, float)):
            raise TypeError("x must be a number.")
        if isinstance(y, bool) or not isinstance(y, (int, float)):
            raise TypeError("y must be a number.")
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def magnitude(self):
        """Return the vector's length."""
        return math.hypot(self.x, self.y)

    def __add__(self, other):
        """Add two vectors with the + operator."""
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Subtract vectors with the - operator."""
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """Multiply by a scalar or compute a dot product with another vector."""
        if isinstance(other, bool):
            return NotImplemented
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    def __rmul__(self, other):
        """Support scalar * vector."""
        return self.__mul__(other)

    def __truediv__(self, other):
        """Divide a vector by a non-zero scalar."""
        if isinstance(other, bool) or not isinstance(other, (int, float)):
            return NotImplemented
        if other == 0:
            raise ZeroDivisionError("Cannot divide vector by zero.")
        return Vector(self.x / other, self.y / other)

    def __eq__(self, other):
        """Compare vectors by their x and y coordinates."""
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        """Compare vectors by magnitude."""
        if not isinstance(other, Vector):
            return NotImplemented
        return self.magnitude() < other.magnitude()

    def __abs__(self):
        """Return vector magnitude so abs(vector) is supported."""
        return self.magnitude()


if __name__ == "__main__":
    print("=== Testing All Operators ===")
    v1 = Vector(4, 3)
    v2 = Vector(2, 1)

    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print()
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 2 = {v1 * 2}")
    print(f"3 * v2 = {3 * v2}")
    print(f"v1 * v2 (dot product) = {v1 * v2}")
    print(f"v1 / 2 = {v1 / 2}")
    print(f"v1 == v2: {v1 == v2}")
    print(f"v1 < v2: {v1 < v2}")
    print(f"|v1| = {abs(v1):.2f}")

    print("\n=== Complex Operations ===")
    result = (v1 + v2) * 2 / 3
    print(f"(v1 + v2) * 2 / 3 = {result}")
