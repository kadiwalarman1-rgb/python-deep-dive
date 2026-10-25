# Lab 46: Composition vs Inheritance

This lab contrasts the **has-a** relationship (composition) with the **is-a** relationship (inheritance) using car and engine examples.

## Files
- `engine_car_composition.py`: `Engine` and `Car` classes, composition demonstrations, and direct engine access.
- `inheritance_example.py`: base `Vehicle`, derived `ElectricCar` and `GasCar`, method overrides, battery/fuel behavior, and an inheritance demo.
- `main_demo.py`: side-by-side comparison, runtime engine swapping, polymorphism, relationship analysis, and selection guidelines.
- `interactive_test.py`: interactive car menu and batch object-creation tests.
- `PROOF.md`: run commands and validation notes.

## Run
Run these commands from this folder:

```bash
python3 engine_car_composition.py
python3 inheritance_example.py
python3 main_demo.py
python3 interactive_test.py
```

The interactive script prompts for car details. Press Enter to use defaults, and choose option 8 to exit the menu and continue batch tests. No third-party dependencies are required.

## Main concepts
Composition models a **has-a** relationship such as Car has an Engine. Inheritance models an **is-a** relationship such as ElectricCar is a Vehicle. Choose based on the relationship and the flexibility the design needs.
