# Lab 35: Final Project - Building a Package with Python

## What You Will Learn

- Organize arithmetic, algebra, and geometry functionality into a reusable Python package.
- Use __init__.py to expose modules, functions, and package metadata.
- Handle invalid input with exceptions.
- Test package functionality using external scripts.
- Document package structure and usage in a README.

## Project Structure

```text
Lab 35/
├── mathtools/
│   ├── __init__.py
│   ├── arithmetic.py
│   ├── algebra.py
│   └── geometry.py
├── test_mathtools.py
├── example_usage.py
├── validate_package.py
└── README.md
```

## Run the Examples

Run commands from this directory:

```bash
python3 example_usage.py
python3 test_mathtools.py
python3 validate_package.py
```

The package uses only Python's standard library; no third-party installation is needed.

## Example

```python
import mathtools

print(mathtools.add(5, 3))
print(mathtools.circle_area(5))
print(mathtools.solve_linear(2, -6))
```

## Error Handling

Division by zero and invalid equation coefficients raise ValueError. A negative factorial raises ValueError, and a non-integer factorial input raises TypeError. Invalid triangle side lengths are rejected by the Heron formula function.

## Source Note

The uploaded course material ends partway through example_usage.py in Task 3.3. That example has been completed using the functions defined earlier in the lab. The README and validation script provide a practical continuation based on the listed lab objectives; they are not recovered original course pages.
