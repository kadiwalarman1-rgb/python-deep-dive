# Lab 44: Operator Overloading in Python

This lab demonstrates how Python's magic methods let custom objects support operators naturally.

## Files

- `vector_class.py`: a reusable 2D Vector class with overloaded `+`, `-`, `*`, `/`, `==`, and `<` operators. Multiplication by a number scales a vector; multiplication by another vector calculates the dot product.
- `test_operators.py`: baseline tests for vector creation, chained addition, equality, magnitude comparison, and invalid operations.
- `advanced_tests.py`: scalar arithmetic, dot product, unit-vector calculations, perpendicular vectors, and error handling.
- `physics_demo.py`: projectile motion and a 1D elastic collision that verifies momentum conservation.

## Run the examples

Run commands from this folder:

```bash
python3 vector_class.py
python3 test_operators.py
python3 advanced_tests.py
python3 physics_demo.py
```

No third-party packages are required; the lab uses the Python standard library.

## Key concepts

The `__add__`, `__sub__`, `__mul__`, `__rmul__`, `__truediv__`, `__eq__`, `__lt__`, and `__abs__` methods customize operator behavior. Vector comparisons with `<` use magnitude; equality compares coordinates.

## Execution proof

See [PROOF.md](PROOF.md) for validation notes. Terminal screenshots have not been supplied with this Lab 44 material, so this repository entry does not claim to contain screenshot evidence.
