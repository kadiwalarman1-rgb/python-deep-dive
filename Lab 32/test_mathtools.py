import mathtools
from mathtools import add, subtract, multiply, divide, Circle, Rectangle
from mathtools import basic_operations, geometry
from mathtools.statistics import mean, median, mode, range_value, variance, standard_deviation


def main():
    print("=" * 60)
    print("TESTING MATHTOOLS PACKAGE")
    print("=" * 60)
    print("Package info:", mathtools.get_package_info())

    print("\nBasic operations:")
    print("Addition:", add(10, 5))
    print("Subtraction:", subtract(10, 5))
    print("Multiplication:", multiply(10, 5))
    print("Division:", divide(10, 5))
    print("Power:", mathtools.power(2, 8))
    print("PI constant:", mathtools.PI)

    print("\nGeometry:")
    circle = Circle(5)
    print(circle)
    print(f"Area: {circle.area():.2f}")
    print(f"Circumference: {circle.circumference():.2f}")
    print("Diameter:", circle.diameter())
    rectangle = Rectangle(4, 6)
    print(rectangle)
    print("Area:", rectangle.area())
    print("Perimeter:", rectangle.perimeter())
    print("Is square:", rectangle.is_square())
    print("Triangle area:", geometry.calculate_triangle_area(10, 8))

    values = [2, 4, 4, 4, 5, 5, 7, 9]
    print("\nStatistics for", values)
    print("Mean:", mean(values))
    print("Median:", median(values))
    print("Mode:", mode(values))
    print("Range:", range_value(values))
    print("Sample variance:", variance(values))
    print("Sample standard deviation:", standard_deviation(values))
    print("Module info:", basic_operations.get_module_info())
    print("Statistics info:", mathtools.statistics.get_stats_info())
    print("\nAll demo sections completed.")


if __name__ == "__main__":
    main()
