import math
import mathtools


def main():
    assert mathtools.add(5, 3) == 8
    assert mathtools.factorial(5) == 120
    roots = mathtools.solve_quadratic(1, -5, 6)
    assert math.isclose(roots[0], 3)
    assert math.isclose(roots[1], 2)
    assert mathtools.solve_linear(2, -6) == 3
    assert mathtools.evaluate_polynomial([1, 2, 3], 2) == 17
    assert math.isclose(mathtools.find_slope(1, 2, 3, 6), 2)
    assert math.isclose(mathtools.distance_between_points(0, 0, 3, 4), 5)
    assert mathtools.rectangle_area(5, 3) == 15
    assert math.isclose(mathtools.triangle_area_heron(3, 4, 5), 6)
    assert mathtools.rectangular_prism_volume(3, 4, 5) == 60
    try:
        mathtools.divide(10, 0)
    except ValueError:
        pass
    else:
        raise AssertionError("Division by zero was not handled")
    info = mathtools.get_package_info()
    assert info["name"] == "mathtools"
    print("External package imports and validation checks passed.")


if __name__ == "__main__":
    main()
