#!/usr/bin/env python3
"""Lab 49: Python decorators — timing, authorization, chaining, and metadata."""
import functools
import time
from typing import Any, Callable, Optional

current_user: Optional[str] = None
authorized_users = {"admin", "manager", "developer"}


def time_logger(func: Callable) -> Callable:
    """Log a function's start and execution time while preserving metadata."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        print(f"Starting execution of {func.__name__}")
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            print(f"Function {func.__name__} executed in {elapsed:.4f} seconds")
    return wrapper


def requires_authorization(func: Callable) -> Callable:
    """Permit execution only when the simulated current user is authorized."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if current_user is None:
            print(f"Access denied to {func.__name__}: No user logged in")
            return None
        if current_user not in authorized_users:
            print(f"Access denied to {func.__name__}: User '{current_user}' not authorized")
            return None
        print(f"Access granted to {func.__name__} for user '{current_user}'")
        return func(*args, **kwargs)
    return wrapper


def input_validator(func: Callable) -> Callable:
    """Reject calls with None values in positional or keyword arguments."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Validating inputs for {func.__name__}")
        for index, argument in enumerate(args):
            if argument is None:
                print(f"Validation failed: Argument {index} is None")
                return None
        for key, value in kwargs.items():
            if value is None:
                print(f"Validation failed: Keyword argument '{key}' is None")
                return None
        print("Input validation passed")
        return func(*args, **kwargs)
    return wrapper


def result_formatter(func: Callable) -> Callable:
    """Prefix non-None results with a small formatting marker."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        result = func(*args, **kwargs)
        if result is not None:
            print(f"Result formatted by {func.__name__}")
            return f"[FORMATTED] {result}"
        return None
    return wrapper


@time_logger
def slow_function() -> str:
    """A function that intentionally takes about two seconds."""
    time.sleep(2)
    return "Task completed"


@time_logger
def fast_function() -> int:
    """A quick sum calculation."""
    return sum(range(1000))


@time_logger
def calculation_function(n: int) -> int:
    """Return the sum of squares from zero through n-1."""
    if n < 0:
        raise ValueError("n must be non-negative")
    return sum(i * i for i in range(n))


@requires_authorization
def delete_user(username: str) -> str:
    """Example of a protected operation."""
    return f"User {username} has been deleted"


@requires_authorization
def view_sensitive_data() -> str:
    """Return simulated sensitive data only to an authorized user."""
    return "Confidential data: Account balances, personal information"


@requires_authorization
def modify_system_settings(setting: str, value: str) -> str:
    """Example of a protected settings operation."""
    return f"System setting '{setting}' changed to '{value}'"


@result_formatter
@input_validator
@requires_authorization
@time_logger
def process_user_data(user_id: str, action: str) -> str:
    """Demonstrate four decorators applied to one function."""
    time.sleep(0.5)
    return f"Processed action '{action}' for user {user_id}"


@time_logger
@requires_authorization
def simple_chained_function(message: str) -> str:
    """A small example combining timing and authorization."""
    return f"Message processed: {message}"


def bad_decorator(func: Callable) -> Callable:
    """A decorator that does not preserve the wrapped function's metadata."""
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print("Bad decorator applied to some function")
        return func(*args, **kwargs)
    return wrapper


def good_decorator(func: Callable) -> Callable:
    """A decorator that preserves the wrapped function's metadata."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Good decorator applied to {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@bad_decorator
def function_with_bad_decorator() -> str:
    """This function's metadata will be lost."""
    return "Bad decorator result"


@good_decorator
def function_with_good_decorator() -> str:
    """This function's metadata will be preserved."""
    return "Good decorator result"


def original_function() -> str:
    """The original function without any decorator."""
    return "Original function result"


def advanced_metadata_decorator(description: str = "") -> Callable:
    """Create a decorator that preserves metadata and attaches custom attributes."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print(f"Executing {func.__name__}: {description}")
            result = func(*args, **kwargs)
            print(f"Completed {func.__name__}")
            return result
        wrapper.decorator_description = description
        wrapper.is_decorated = True
        return wrapper
    return decorator


@advanced_metadata_decorator("Calculates factorial of a number")
def factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n must be a non-negative integer")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def test_time_logger() -> None:
    print("\n=== Testing Time Logger Decorator ===")
    print("\n1. Testing slow function:")
    print("Result:", slow_function())
    print("\n2. Testing fast function:")
    print("Result:", fast_function())
    print("\n3. Testing calculation function:")
    print("Result:", calculation_function(10000))


def test_authorization() -> None:
    global current_user
    print("\n=== Testing Authorization Decorator ===")
    current_user = None
    print("\n1. No user logged in:")
    print("Result:", delete_user("john_doe"))
    current_user = "guest"
    print("\n2. Unauthorized user:")
    print("Result:", view_sensitive_data())
    current_user = "admin"
    print("\n3. Authorized user:")
    print("Result:", delete_user("john_doe"))
    print("Result:", view_sensitive_data())
    print("Result:", modify_system_settings("debug_mode", "enabled"))
    current_user = "developer"
    print("\n4. Switch to developer:")
    print("Result:", modify_system_settings("log_level", "debug"))


def test_decorator_chaining() -> None:
    global current_user
    print("\n=== Testing Decorator Chaining ===")
    current_user = "admin"
    print("\n1. Valid input:")
    print("Final result:", process_user_data("12345", "update_profile"))
    print("\n2. Invalid input:")
    print("Final result:", process_user_data(None, "delete_account"))
    print("\n3. Simpler chained function:")
    print("Final result:", simple_chained_function("Hello World"))


def test_metadata_preservation() -> None:
    print("\n=== Testing Metadata Preservation ===")
    for label, func in (
        ("Original function", original_function),
        ("Bad decorator", function_with_bad_decorator),
        ("Good decorator", function_with_good_decorator),
    ):
        print(f"\n{label}:")
        print("Name:", func.__name__)
        print("Docstring:", func.__doc__)
        print("Module:", func.__module__)
    print("\nFunction call results:")
    print("Bad decorator:", function_with_bad_decorator())
    print("Good decorator:", function_with_good_decorator())


def test_advanced_metadata() -> None:
    print("\n=== Testing Advanced Metadata ===")
    print("Function name:", factorial.__name__)
    print("Function docstring:", factorial.__doc__)
    print("Custom description:", factorial.decorator_description)
    print("Is decorated:", factorial.is_decorated)
    print("\nCalculating factorial of 5:")
    print("Result:", factorial(5))


def main() -> None:
    """Run every demonstration in the lab."""
    print("Python Decorators Lab - Complete Test Suite")
    print("=" * 50)
    test_time_logger()
    test_authorization()
    test_decorator_chaining()
    test_metadata_preservation()
    test_advanced_metadata()
    print("\n" + "=" * 50)
    print("Lab completed successfully!")


if __name__ == "__main__":
    main()
