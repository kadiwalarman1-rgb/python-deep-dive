# Lab 50: Understanding Python Generators

## Objectives
- Create generator functions with `yield` and consume values using `next()`.
- Handle generator exhaustion and use default values.
- Use generator expressions and lazy processing pipelines.
- Compare list and generator creation time and shallow object size.
- Stream large text files and CSV rows without loading all records into memory.
- Filter data lazily using reusable generator functions.

## Files
- `generators_lab.py` — complete runnable demonstration covering all lab tasks.
- `test_generators_lab.py` — automated tests for Fibonacci, `next()`, text-file and CSV generators.

## Requirements
Python 3.8 or newer. Standard library only.

## Run the lab
```bash
python3 generators_lab.py
```

This runs the demonstrations in sequence. It creates `large_sample.txt` and `employees.csv` locally if they do not already exist. The default full demonstration uses 100,000 text lines and 50,000 CSV records.

## Run automated tests
```bash
python3 -m unittest -v
```

## Key concepts
- `yield` pauses a generator and resumes it on the next request.
- Generators are lazy and usually one-shot; a consumed generator does not automatically reset.
- `next(iterator, default)` returns the default when an iterator is exhausted.
- Generator expressions can chain filtering and transformations without materializing every intermediate list.
- `sys.getsizeof()` reports shallow size only. It does not count every object referenced by a list or the full memory use of a running process.
- Runtime and memory measurements vary by machine and Python build.

## Lab outputs
The sample data files are generated at runtime and do not need to be uploaded to GitHub. The scripts only use local files and the Python standard library.
