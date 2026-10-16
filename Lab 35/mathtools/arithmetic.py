def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base, exponent):
    return base ** exponent


def factorial(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Factorial input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result
