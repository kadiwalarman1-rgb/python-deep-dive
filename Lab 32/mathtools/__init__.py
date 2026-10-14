from .basic_operations import add, subtract, multiply, divide, power, PI
from .geometry import Circle, Rectangle, calculate_triangle_area
from . import statistics

__version__ = "1.1.0"
__author__ = "Python Deep Dive learner"
__description__ = "A mathematical utilities package for Python"

__all__ = [
    "add", "subtract", "multiply", "divide", "power", "PI",
    "Circle", "Rectangle", "calculate_triangle_area", "statistics",
    "get_package_info",
]


def get_package_info():
    return {
        "name": "mathtools",
        "version": __version__,
        "author": __author__,
        "description": __description__,
        "modules": ["basic_operations", "geometry", "statistics"],
    }
