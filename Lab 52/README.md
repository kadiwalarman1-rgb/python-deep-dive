# Lab 52: Iterators and Iterables — Creating and Using Iterators

## Objectives
- Understand the difference between iterables and iterators.
- Implement custom iterators with __iter__() and __next__().
- Generate counter and Fibonacci values on demand.
- Process employee CSV data and calculate department statistics.
- Use list(), next(), sum(), max(), min(), any(), all(), and enumerate() with custom iterators.
- Combine streams using itertools.chain() and related utilities.

## Files
- iterators_lab.py — complete runnable demonstration for all lab tasks.
- test_iterators_lab.py — automated tests for counters, Fibonacci, file cleanup, CSV statistics, and custom iterators.

## Requirements
Python 3.8 or newer. Standard library only.

## Run the complete lab
From inside this Lab 52 folder:

    python3 iterators_lab.py

The script runs the counter, Fibonacci, file iterator, built-in function, iterator exhaustion, itertools, and multiple data-source demonstrations. It creates the employee CSV inside a temporary directory and removes it afterwards.

## Run automated tests

    python3 -m unittest -v

## Key concepts
- An iterable provides an iterator through iter().
- An iterator implements __iter__() and __next__().
- __next__() raises StopIteration when no values remain.
- Iterators are stateful and normally exhausted after one complete traversal.
- File iterators should close their file handles. FileLineIterator supports close() and a with statement for early-exit cleanup.
- itertools includes lazy utilities such as chain(), count(), cycle(), repeat(), islice(), takewhile(), dropwhile(), and filterfalse().
