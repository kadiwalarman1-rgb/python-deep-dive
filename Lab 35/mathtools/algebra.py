import math


def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for quadratic equation")
    discriminant = b**2 - 4 * a * c
    if discriminant >= 0:
        root = math.sqrt(discriminant)
        return ((-b + root) / (2 * a), (-b - root) / (2 * a))
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-discriminant) / (2 * a)
    return (complex(real_part, imaginary_part), complex(real_part, -imaginary_part))


def solve_linear(a, b):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for linear equation")
    return -b / a


def evaluate_polynomial(coefficients, x):
    result = 0
    for exponent, coefficient in enumerate(coefficients):
        result += coefficient * (x ** exponent)
    return result


def find_slope(x1, y1, x2, y2):
    if x1 == x2:
        raise ValueError("Cannot calculate slope of vertical line (same x-coordinates)")
    return (y2 - y1) / (x2 - x1)


def distance_between_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
