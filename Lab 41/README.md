# Lab 41: Encapsulation — Getters, Setters, and Properties

## Objectives

- Understand encapsulation and data hiding in object-oriented programming.
- Use double-underscore attributes and Python name mangling.
- Implement getter methods for controlled access to attributes.
- Validate data with setter methods before updating object state.
- Demonstrate direct-access behavior and the limits of name mangling.
- Use @property and setter decorators for a Pythonic interface.

## Files

| File | Purpose |
|---|---|
| person_class.py | Person class with private-name attributes, getter methods, validated setters, and a birthday method. |
| test_validation.py | Standalone demonstrations of accepted and rejected inputs. |
| test_direct_access.py | Demonstrates direct access, name mangling, and separate attributes created by direct assignment. |
| encapsulation_demo.py | End-to-end demonstration of encapsulation and validation. |
| person_with_properties.py | Alternative PersonWithProperties implementation using property decorators. |
| test_lab41.py | Automated unit tests for both implementations. |

## Run the Lab

Use Python 3.8 or newer. The lab uses only the Python standard library and requires no third-party packages. Run these commands from this directory:

    python3 person_class.py
    python3 test_validation.py
    python3 test_direct_access.py
    python3 encapsulation_demo.py
    python3 person_with_properties.py
    python3 -m unittest -v test_lab41.py

## Concepts Covered

- The double underscore prefix (for example, self.__name) triggers Python name mangling. It helps avoid accidental access and name collisions; it is not a strict security boundary.
- Getters provide a defined way to read internal state.
- Setters validate input and normalize values before updating state.
- Initializing through setters ensures the same rules apply during construction and later updates.
- The property decorator allows attribute-style access while still running validation code.
- Assigning person.__name outside the class creates a separate attribute; it does not overwrite the name-mangled _Person__name attribute.

## Validation Rules

- Names must be strings containing at least two non-whitespace characters. Names are stripped and title-cased before storage.
- Ages must be integers from 0 through 150 inclusive. Booleans, non-integers, negative ages, and ages above 150 are rejected.
- Failed setter calls leave the previously stored value unchanged.

## Why Encapsulation Matters

Encapsulation centralizes validation and business rules, supports data integrity, and gives classes a stable interface. The same techniques can be applied to entities such as bank accounts, students, products, and inventory items.
