# Lab 40: Polymorphism — Understanding Polymorphism

## Objectives

- Understand polymorphism in object-oriented programming.
- Create a base class and derived shape classes.
- Override area() to provide class-specific calculations.
- Call a common function with different shape objects.
- Process collections of polymorphic objects.
- Compare shape types and their calculated areas.

## Files

| File | Purpose |
|---|---|
| shapes.py | Complete implementation of Shape, Circle, Rectangle, Triangle, and Square, plus all lab demonstrations. |
| test_lab40.py | Automated tests for areas, inheritance, polymorphism, grouping, and invalid dimensions. |

## Run the Lab

Run the following commands from this directory with Python 3.8 or newer. No third-party packages are required.

    python3 shapes.py
    python3 -m unittest -v test_lab40.py

## Concepts

- Shape.area() defines the shared interface and raises NotImplementedError until implemented by a subclass.
- Circle, Rectangle, and Triangle each implement their own area() method.
- Square inherits from Rectangle, using the same side length for width and height.
- calculate_and_display_area() uses polymorphism by calling area() without needing to know the object's concrete class.
- Mixed collections can be iterated uniformly, grouped by type, and compared by area.

## Input rules

All dimensions must be positive finite numbers. Invalid, zero, negative, boolean, or non-finite dimensions raise ValueError. Area values are based on the mathematical formulae for each represented shape.
