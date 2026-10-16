import mathtools


def calculator_example():
    print("=" * 40)
    print("CALCULATOR EXAMPLE")
    print("=" * 40)
    a, b = 15, 4
    print(f"Numbers: a = {a}, b = {b}")
    print(f"Addition: {a} + {b} = {mathtools.add(a, b)}")
    print(f"Subtraction: {a} - {b} = {mathtools.subtract(a, b)}")
    print(f"Multiplication: {a} * {b} = {mathtools.multiply(a, b)}")
    print(f"Division: {a} / {b} = {mathtools.divide(a, b):.2f}")
    print(f"Power: {a}^{b} = {mathtools.power(a, b)}")
    print(f"Factorial of 5: {mathtools.factorial(5)}")
    print()


def geometry_example():
    print("=" * 40)
    print("GEOMETRY EXAMPLE: GARDEN PLANNING")
    print("=" * 40)
    length, width = 10, 6
    veg_area = mathtools.rectangle_area(length, width)
    veg_perimeter = mathtools.rectangle_perimeter(length, width)
    print(f"Vegetable garden ({length}m x {width}m):")
    print(f"  Area: {veg_area} m²")
    print(f"  Fencing needed: {veg_perimeter} m")
    radius = 3
    flower_area = mathtools.circle_area(radius)
    flower_circumference = mathtools.circle_circumference(radius)
    print(f"\nFlower bed (radius {radius}m):")
    print(f"  Area: {flower_area:.2f} m²")
    print(f"  Border length: {flower_circumference:.2f} m")
    base, height = 4, 3
    herb_area = mathtools.triangle_area(base, height)
    print(f"\nHerb garden (base {base}m, height {height}m):")
    print(f"  Area: {herb_area} m²")
    total_area = veg_area + flower_area + herb_area
    print(f"\nTotal garden area: {total_area:.2f} m²")
    print()


def algebra_example():
    print("=" * 40)
    print("ALGEBRA EXAMPLE: PROJECTILE MOTION")
    print("=" * 40)
    print("Equation: h = -16t² + 64t + 80")
    solutions = mathtools.solve_quadratic(-16, 64, 80)
    print(f"Solutions: t = {solutions[0]:.2f}s or t = {solutions[1]:.2f}s")
    print(f"Positive ground-impact time: {max(solutions):.2f}s")
    t_max = -64 / (2 * -16)
    h_max = mathtools.evaluate_polynomial([80, 64, -16], t_max)
    print(f"Maximum height reached at t = {t_max:.2f}s: h = {h_max:.2f} feet")
    print()


def engineering_example():
    print("=" * 40)
    print("ENGINEERING EXAMPLE: TANK DESIGN")
    print("=" * 40)
    radius, height = 2, 5
    volume = mathtools.cylinder_volume(radius, height)
    top_bottom_area = 2 * mathtools.circle_area(radius)
    side_area = mathtools.circle_circumference(radius) * height
    total_surface_area = top_bottom_area + side_area
    print(f"Tank radius: {radius}m")
    print(f"Tank height: {height}m")
    print(f"Tank volume: {volume:.2f} m³")
    print(f"Top and bottom area: {top_bottom_area:.2f} m²")
    print(f"Side surface area: {side_area:.2f} m²")
    print(f"Total surface area: {total_surface_area:.2f} m²")
    print()


def main():
    print(f"MathTools v{mathtools.__version__}")
    calculator_example()
    geometry_example()
    algebra_example()
    engineering_example()
    print("All usage examples completed.")


if __name__ == "__main__":
    main()
