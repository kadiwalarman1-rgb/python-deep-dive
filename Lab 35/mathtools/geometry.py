import math


def circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius**2


def circle_circumference(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 2 * math.pi * radius


def rectangle_area(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative")
    return length * width


def rectangle_perimeter(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative")
    return 2 * (length + width)


def triangle_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative")
    return 0.5 * base * height


def triangle_area_heron(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("All sides must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Sides do not form a valid triangle")
    semi_perimeter = (a + b + c) / 2
    return math.sqrt(
        semi_perimeter
        * (semi_perimeter - a)
        * (semi_perimeter - b)
        * (semi_perimeter - c)
    )


def sphere_volume(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return (4 / 3) * math.pi * radius**3


def sphere_surface_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 4 * math.pi * radius**2


def cylinder_volume(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height cannot be negative")
    return math.pi * radius**2 * height


def rectangular_prism_volume(length, width, height):
    if length < 0 or width < 0 or height < 0:
        raise ValueError("All dimensions must be non-negative")
    return length * width * height
