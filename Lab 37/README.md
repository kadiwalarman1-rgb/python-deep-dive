# Lab 37: Constructor and Initialization — Using the __init__ Method

## Objectives
- Understand how __init__ initializes a new instance.
- Pass arguments to constructors and store them as instance attributes.
- Display object data in a formatted way.
- Create multiple independent Student, Book, Vehicle, Product, and Employee objects.
- Use default parameter values and validate input.

## Files
| File | Purpose |
|---|---|
| student_class.py | Student constructor, default major, courses, credits, GPA, and profiles. |
| book_library.py | Book constructor, borrowing, returning, reviews, and ratings. |
| vehicle_system.py | Vehicle constructor, default mileage, engine, fuel, and maintenance. |
| inventory_system.py | Product constructor, default quantity/supplier, sales, and stock reports. |
| default_parameters.py | Employee constructor with optional department, position, salary, date, and email. |
| test_lab37.py | Unit tests for constructors, defaults, object independence, and core methods. |

## Run from this directory
Use Python 3.10 or newer. No third-party packages are needed.

    python3 student_class.py
    python3 book_library.py
    python3 vehicle_system.py
    python3 inventory_system.py
    python3 default_parameters.py
    python3 -m unittest -v test_lab37.py

## Key concepts
- __init__ runs automatically when an instance is created.
- self refers to the current object, so instances keep independent attributes.
- Required parameters must be passed; optional parameters provide defaults.
- Mutable fields such as lists should be initialized per instance.
- Constructors establish valid initial state; methods subsequently modify it.
- The default Employee email is derived from the employee's name when no email is supplied.

## Note about the supplied lab text
The attachment ends partway through Employee.calculate_average_rating. I completed that missing section consistently with the visible example by adding average-rating calculation, profile output, employee activation status, project listing, and a runnable demo. These are in-memory examples; no database or file persistence is implemented.
