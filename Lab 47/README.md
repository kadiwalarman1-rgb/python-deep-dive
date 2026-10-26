# Lab 47: Multiple Inheritance in Python

## Objectives
- Create classes that inherit from multiple parent classes.
- Understand method overriding and Method Resolution Order (MRO).
- Use `super()` and explore the diamond problem.
- Run practical examples with animals and an electric autonomous car.

## Run
```bash
python3 multiple_inheritance_lab.py
```

## Key concepts
- **Multiple inheritance:** `class Dog(Animal, Mammal)`
- **MRO:** inspect the lookup order with `Dog.__mro__`.
- **super():** follows the MRO; it does not simply mean “call the first parent”.
- **Diamond problem:** Python uses C3 linearization so each class appears once in the MRO.

## Files
- `multiple_inheritance_lab.py` — complete runnable demonstrations.
