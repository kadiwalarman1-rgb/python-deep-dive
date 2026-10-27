# Lab 48: Final Project — OOP Library Management System

This lab builds a complete, runnable Library Management System using Python's object-oriented programming features.

## Files

- `library_management_system.py` — application classes and a complete demonstration run.
- `test_library_management_system.py` — automated unit tests for the main workflows and edge cases.

## Requirements

- Python 3.8 or newer
- No third-party packages; the project uses only the Python standard library.

## Run the demonstration

From this folder, run:

```bash
python3 library_management_system.py
```

The demonstration creates a library, registers librarians and users, adds books, processes borrowing and returns, searches the catalog, exercises overloaded operators, and prints reports.

## Run automated tests

```bash
python3 -m unittest -v
```

## OOP concepts demonstrated

- **Encapsulation:** private attributes with properties and validated setters.
- **Inheritance:** `User` and `Librarian` extend `Person`.
- **Polymorphism:** subclasses customize `__str__`; report generation dispatches to report-specific methods.
- **Abstraction:** the `Library` class coordinates catalog and circulation operations through a public interface.
- **Magic methods / operator overloading:** `__str__`, `__repr__`, `__eq__`, `__hash__`, comparisons on `Book`, and `__len__` / `__contains__` on `Library`.
- **Real-world workflows:** registration, book search, borrow/return, fines, membership upgrades, and reports.

## Notes

This is an educational in-memory application. Records reset when the program exits; persistent storage, authentication, and a production UI are outside the scope of this lab.
