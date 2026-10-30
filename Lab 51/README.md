# Lab 51: Context Managers — Using with Statements and Custom Context Managers

## Objectives
- Use built-in context managers for safe file operations.
- Implement custom context managers with the enter and exit protocol.
- Commit or roll back SQLite transactions and always close resources.
- Demonstrate cleanup after exceptions and thread-safe resource limits.
- Measure code duration with basic and detailed timer context managers.
- Manage temporary directories, environment configuration, and contextlib helpers.

## Files
- context_managers_lab.py — complete runnable script covering all lab tasks.
- test_context_managers.py — automated unit tests for cleanup, transactions, resource limits, timers, and contextlib helpers.

## Requirements
Python 3.8 or newer. Standard library only.

## Run the complete demonstration
From inside this Lab 51 folder:

    python3 context_managers_lab.py

The script demonstrates file handling, custom context managers, SQLite commit/rollback, thread-safe simulated resource use, timing, temporary directories, environment restoration, temporary files, ExitStack, and suppress.

## Run automated tests

    python3 -m unittest -v

## Core concepts
- A with statement delegates cleanup to a context manager even if its block raises an exception.
- __enter__ prepares/acquires the resource and returns the value bound by as.
- __exit__ performs cleanup. Returning True suppresses the active exception; returning False or None propagates it.
- The SQLite example commits on success and rolls back on failure.
- contextlib.contextmanager turns a generator with one yield into a context manager.
- ExitStack manages a dynamic number of context managers and exits them in reverse order.
- suppress intentionally ignores only the specified exception types.

Temporary data is created locally by the demonstrations. No third-party package or network access is required.
