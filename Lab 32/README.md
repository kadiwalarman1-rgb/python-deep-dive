# Lab 32: Creating and Using Python Packages

## What You Will Learn

- Organize related functions and classes into reusable Python modules.
- Create a package with __init__.py and expose selected names at package level.
- Use relative imports between a package and its modules.
- Build a class-based geometry module with Circle and Rectangle.
- Create a statistics subpackage with mean, median, mode, range, variance, and standard deviation functions.
- Use package metadata and __all__ to define the public API.
- Import package functions, classes, and submodules in another script.
- Validate behavior with automated unit tests and test invalid inputs.

## Package Structure

    Lab 32/
    ├── mathtools/
    │   ├── __init__.py
    │   ├── basic_operations.py
    │   ├── geometry.py
    │   └── statistics/
    │       ├── __init__.py
    │       └── descriptive.py
    ├── test_mathtools.py
    ├── advanced_test.py
    └── README.md

## Run the Demonstration

From this folder, run:

    python3 test_mathtools.py

## Run the Test Suite

    python3 advanced_test.py

The test suite uses only Python's standard library and needs no third-party dependencies.
