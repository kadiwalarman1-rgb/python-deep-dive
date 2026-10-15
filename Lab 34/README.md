# Lab 34: Advanced Package Usage

## What You Will Learn

- Organize a larger Python project into packages, subpackages, and modules.
- Use relative imports to share functionality between package modules.
- Build product catalog, category, inventory, authentication, profile, order, and simulated payment components.
- Validate data, write logs, and save JSON data.
- Expose package classes through __init__.py files.
- Install optional third-party dependencies with pip and define package metadata in setup.py.
- Build source and wheel distributions and test package behavior with unittest.

## Files

- ecommerce/ — package source, including nested modules and relative imports.
- main_demo.py — demonstrates the package components working together.
- third_party_demo.py — prepares a request with the optional requests package without sending a network request.
- advanced_test.py — automated tests for imports and core functionality.
- setup.py and requirements.txt — package metadata and dependency example.

## Run

Run these commands from this folder:

    python3 main_demo.py
    python3 -m unittest advanced_test.py -v

To install the optional third-party dependency and run its demo:

    python3 -m pip install -r requirements.txt
    python3 third_party_demo.py

To install this package in editable mode and build distributions:

    python3 -m pip install --upgrade setuptools wheel
    python3 -m pip install -e .
    python3 setup.py sdist bdist_wheel

Package builds are written to dist/. The payment processor is a simulation only; it does not charge real payment methods.

## Source Note

The provided Lab 34 source ends during search_products_by_category() in Task 3.1. The method has been completed, and the remaining examples covering API-style imports, third-party dependencies, and package distribution are a practical continuation based on the lab objectives, not a verbatim recovery of missing course pages.
