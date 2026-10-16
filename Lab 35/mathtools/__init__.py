from . import arithmetic, algebra, geometry
from .arithmetic import add, subtract, multiply, divide, power, factorial
from .algebra import (
    solve_quadratic,
    solve_linear,
    evaluate_polynomial,
    find_slope,
    distance_between_points,
)
from .geometry import (
    circle_area,
    circle_circumference,
    rectangle_area,
    rectangle_perimeter,
    triangle_area,
    triangle_area_heron,
    sphere_volume,
    sphere_surface_area,
    cylinder_volume,
    rectangular_prism_volume,
)

__version__ = "1.0.0"
__author__ = "Student Lab Project"
__email__ = "student@example.com"

__all__ = [
    "arithmetic", "algebra", "geometry",
    "add", "subtract", "multiply", "divide", "power", "factorial",
    "solve_quadratic", "solve_linear", "evaluate_polynomial",
    "find_slope", "distance_between_points",
    "circle_area", "circle_circumference", "rectangle_area",
    "rectangle_perimeter", "triangle_area", "triangle_area_heron",
    "sphere_volume", "sphere_surface_area", "cylinder_volume",
    "rectangular_prism_volume", "get_package_info", "list_functions",
]


def get_package_info():
    return {
        "name": "mathtools",
        "version": __version__,
        "author": __author__,
        "email": __email__,
        "modules": ["arithmetic", "algebra", "geometry"],
        "description": "A Python package for mathematical operations",
    }


def list_functions():
    return {
        "arithmetic": ["add", "subtract", "multiply", "divide", "power", "factorial"],
        "algebra": [
            "solve_quadratic", "solve_linear", "evaluate_polynomial",
            "find_slope", "distance_between_points",
        ],
        "geometry": [
            "circle_area", "circle_circumference", "rectangle_area",
            "rectangle_perimeter", "triangle_area", "triangle_area_heron",
            "sphere_volume", "sphere_surface_area", "cylinder_volume",
            "rectangular_prism_volume",
        ],
    }
