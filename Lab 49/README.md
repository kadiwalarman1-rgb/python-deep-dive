# Lab 49: Introduction to Python Decorators

## Objectives
- Write decorators that add behavior to functions.
- Log function execution time with `time.perf_counter()`.
- Guard protected functions with an authorization decorator.
- Chain decorators and validate function inputs.
- Preserve function metadata with `functools.wraps()`.
- Add custom metadata using a parameterized decorator.

## Files
- `decorator_lab.py` — full demonstration script for every lab task.
- `test_decorator_lab.py` — automated tests for the decorator behaviors.

## Requirements
Python 3.8 or newer. No third-party packages are required.

## Run the demonstration
```bash
python3 decorator_lab.py
```

The demonstration includes a two-second timing example and a half-second chained-function example.

## Run automated tests
```bash
python3 -m unittest -v
```

Run these commands from inside the Lab 49 folder.

## Concepts covered
- `time_logger`: logs start and elapsed time, including when a wrapped function raises.
- `requires_authorization`: simulates access control using `current_user` and a small allow-list.
- `input_validator` and `result_formatter`: demonstrate composable wrappers.
- `functools.wraps()`: preserves the wrapped function's name and docstring.
- `advanced_metadata_decorator`: attaches custom attributes to a decorated function.

## Lab note
The authorization users are simulated for learning only. This in-memory example is not a production authentication or authorization system.
