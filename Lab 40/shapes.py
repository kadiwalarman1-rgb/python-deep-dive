"""Polymorphism examples using geometric shapes."""

import math


class Shape:
    """Base class for all geometric shapes."""

    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Shape name cannot be empty")
        self.name = name.strip()

    def area(self):
        """Subclasses must implement this method."""
        raise NotImplementedError("Subclass must implement area() method")

    def display_info(self):
        """Display basic information about the shape."""
        print(f"Shape: {self.name}")
        print(f"Area: {self.area():.2f}")


class Circle(Shape):
    """Circle derived from Shape."""

    def __init__(self, radius):
        if (
            not isinstance(radius, (int, float))
            or isinstance(radius, bool)
            or not math.isfinite(radius)
            or radius <= 0
        ):
            raise ValueError("Radius must be a positive finite number")
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        """Calculate the area of a circle."""
        return math.pi * self.radius ** 2

    def get_radius(self):
        """Return the circle radius."""
        return self.radius


class Rectangle(Shape):
    """Rectangle derived from Shape."""

    def __init__(self, width, height):
        for value in (width, height):
            if (
                not isinstance(value, (int, float))
                or isinstance(value, bool)
                or not math.isfinite(value)
                or value <= 0
            ):
                raise ValueError("Width and height must be positive finite numbers")
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of a rectangle."""
        return self.width * self.height

    def get_dimensions(self):
        """Return width and height."""
        return self.width, self.height


class Triangle(Shape):
    """Triangle represented by its base and height."""

    def __init__(self, base, height):
        for value in (base, height):
            if (
                not isinstance(value, (int, float))
                or isinstance(value, bool)
                or not math.isfinite(value)
                or value <= 0
            ):
                raise ValueError("Base and height must be positive finite numbers")
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        """Calculate the area of a triangle."""
        return 0.5 * self.base * self.height

    def get_dimensions(self):
        """Return base and height."""
        return self.base, self.height


class Square(Rectangle):
    """Square is a specialized rectangle."""

    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"
        self.side = side

    def get_side(self):
        """Return the square's side length."""
        return self.side


def test_individual_classes():
    """Test the Circle and Rectangle classes."""
    print("=== Testing Individual Classes ===")

    circle = Circle(5)
    print(f"Circle with radius {circle.get_radius()}:")
    circle.display_info()
    print()

    rectangle = Rectangle(4, 6)
    width, height = rectangle.get_dimensions()
    print(f"Rectangle with width {width} and height {height}:")
    rectangle.display_info()
    print()


def calculate_and_display_area(shape):
    """Polymorphic function that works with any Shape implementation."""
    print(f"Processing a {shape.name}...")
    print(f"Area: {shape.area():.2f}")
    print("-" * 30)


def demonstrate_polymorphism():
    """Call the same function with different shape objects."""
    print("=== Demonstrating Polymorphism ===")
    circle = Circle(3)
    rectangle = Rectangle(5, 8)
    calculate_and_display_area(circle)
    calculate_and_display_area(rectangle)


def work_with_shape_collection():
    """Calculate the total and average area of mixed shapes."""
    print("\n=== Working with Shape Collections ===")
    shapes = [
        Circle(2),
        Rectangle(3, 4),
        Circle(7),
        Rectangle(10, 2),
        Circle(1.5),
    ]

    total_area = 0.0
    print("Processing all shapes in the collection:")
    for index, shape in enumerate(shapes, 1):
        area = shape.area()
        total_area += area
        print(f"{index}. {shape.name} - Area: {area:.2f}")

    print(f"\nTotal area of all shapes: {total_area:.2f}")
    print(f"Average area: {total_area / len(shapes):.2f}")


def advanced_collection_operations():
    """Count shape types and identify largest and smallest areas."""
    print("\n=== Advanced Collection Operations ===")
    shapes = [
        Circle(4),
        Rectangle(6, 3),
        Circle(2),
        Rectangle(5, 5),
        Circle(3),
    ]

    circles = [shape for shape in shapes if isinstance(shape, Circle)]
    rectangles = [shape for shape in shapes if isinstance(shape, Rectangle)]

    print(f"Total shapes: {len(shapes)}")
    print(f"Circles: {len(circles)}")
    print(f"Rectangles: {len(rectangles)}")

    largest_shape = max(shapes, key=lambda shape: shape.area())
    print(
        f"\nLargest shape: {largest_shape.name} "
        f"with area {largest_shape.area():.2f}"
    )

    smallest_shape = min(shapes, key=lambda shape: shape.area())
    print(
        f"Smallest shape: {smallest_shape.name} "
        f"with area {smallest_shape.area():.2f}"
    )


def comprehensive_polymorphism_test():
    """Test area calculation and grouping for all shape types."""
    print("\n=== Comprehensive Polymorphism Test ===")
    shapes = [
        Circle(3),
        Rectangle(4, 5),
        Triangle(6, 8),
        Square(4),
        Circle(2.5),
        Triangle(3, 4),
    ]

    print("All shapes and their areas:")
    for shape in shapes:
        print(f"{shape.name}: {shape.area():.2f}")

    shape_groups = {}
    for shape in shapes:
        shape_type = type(shape).__name__
        if shape_type not in shape_groups:
            shape_groups[shape_type] = []
        shape_groups[shape_type].append(shape)

    print("\nShapes grouped by type:")
    for shape_type, group in shape_groups.items():
        total_area = sum(shape.area() for shape in group)
        print(f"{shape_type}: {len(group)} shapes, total area: {total_area:.2f}")


if __name__ == "__main__":
    test_individual_classes()
    demonstrate_polymorphism()
    work_with_shape_collection()
    advanced_collection_operations()
    comprehensive_polymorphism_test()
