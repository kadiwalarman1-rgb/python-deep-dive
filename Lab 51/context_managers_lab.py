#!/usr/bin/env python3
"""Lab 51: Context Managers — complete standard-library demonstrations."""
import os
import shutil
import sqlite3
import tempfile
import threading
import time
from contextlib import ExitStack, contextmanager, suppress
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# Task 1: Traditional file handling and the recommended with statement
# ---------------------------------------------------------------------------

def read_file_traditional(filename: str) -> None:
    """Show manual cleanup; finally is required to cover failure paths."""
    file = None
    try:
        file = open(filename, "r", encoding="utf-8")
        print("File content:", file.read())
    except FileNotFoundError:
        print(f"File {filename!r} not found.")
    except OSError as error:
        print(f"I/O error: {error}")
    finally:
        if file is not None:
            file.close()
            print("File manually closed.")


def read_file_with_context(filename: str) -> None:
    """Read a file and let its context manager close it automatically."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print("File content:", file.read())
        print("File closed automatically.")
    except FileNotFoundError:
        print(f"File {filename!r} not found.")
    except OSError as error:
        print(f"I/O error: {error}")


def write_file_with_context(filename: str, content: str) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Successfully wrote to {filename}")


def risky_file_operation(filename: str) -> None:
    """Raise after opening a file to demonstrate exception-safe cleanup."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print("File opened successfully.")
            if len(content) > 10:
                raise ValueError("Content too long — simulated error")
            print("Content:", content)
    except ValueError as error:
        print("ValueError caught:", error)
        print("The with statement closed the file despite the exception.")
    except FileNotFoundError:
        print(f"File {filename!r} not found.")


def demo_file_operations() -> None:
    print("\n=== TASK 1: FILE CONTEXT MANAGERS ===")
    with tempfile.TemporaryDirectory(prefix="lab51_files_") as directory:
        sample = os.path.join(directory, "sample.txt")
        write_file_with_context(sample, "Hello, World!\nContext managers clean up resources.")
        print("\nTraditional approach:")
        read_file_traditional(sample)
        print("\nRecommended with approach:")
        read_file_with_context(sample)
        print("\nException cleanup demonstration:")
        risky_file_operation(sample)
        print("\nMissing-file handling:")
        read_file_with_context(os.path.join(directory, "missing.txt"))


# ---------------------------------------------------------------------------
# Task 2: Custom protocol manager and SQLite transaction manager
# ---------------------------------------------------------------------------

class BasicContextManager:
    """Simple context manager demonstrating __enter__ and __exit__."""
    def __init__(self, name: str):
        self.name = name
        print(f"Initializing context manager: {self.name}")

    def __enter__(self):
        print(f"Entering context: {self.name}")
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        print(f"Exiting context: {self.name}")
        if exc_type is None:
            print("No exceptions occurred.")
        else:
            print(f"Exception occurred: {exc_type.__name__}: {exc_value}")
        # False means the exception is not suppressed.
        return False


class DatabaseConnection:
    """SQLite context manager: commit on success and roll back on failure."""
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection: Optional[sqlite3.Connection] = None
        self.cursor: Optional[sqlite3.Cursor] = None

    def __enter__(self):
        print(f"Connecting to database: {self.db_name}")
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            print("Database connection established.")
            return self
        except sqlite3.Error:
            if self.connection is not None:
                self.connection.close()
            self.connection = None
            self.cursor = None
            raise

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        connection, cursor = self.connection, self.cursor
        try:
            if connection is not None:
                if exc_type is None:
                    print("Committing transaction.")
                    connection.commit()
                else:
                    print(f"Exception occurred: {exc_type.__name__}: {exc_value}")
                    print("Rolling back transaction.")
                    connection.rollback()
        finally:
            if cursor is not None:
                cursor.close()
                print("Database cursor closed.")
            if connection is not None:
                connection.close()
                print("Database connection closed.")
            self.cursor = None
            self.connection = None
        return False

    def execute(self, query: str, params=None):
        if self.cursor is None:
            raise RuntimeError("No active database connection.")
        return self.cursor.execute(query, params or ())

    def fetchall(self):
        if self.cursor is None:
            raise RuntimeError("No active database connection.")
        return self.cursor.fetchall()


def demo_basic_context_manager() -> None:
    print("\n=== TASK 2: BASIC CUSTOM CONTEXT MANAGER ===")
    with BasicContextManager("Demo Manager") as manager:
        print("Inside the with block:", manager.name)
    try:
        with BasicContextManager("Error Demo"):
            raise ValueError("This is a test exception")
    except ValueError as error:
        print("Caught outside context manager:", error)


def demo_database_context_manager() -> None:
    print("\n=== TASK 2: SQLITE DATABASE CONTEXT MANAGER ===")
    with tempfile.TemporaryDirectory(prefix="lab51_db_") as directory:
        db_name = os.path.join(directory, "test.db")
        with DatabaseConnection(db_name) as db:
            db.execute("""
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            """)
            users = [
                ("Alice Johnson", "alice@example.com"),
                ("Bob Smith", "bob@example.com"),
                ("Carol Davis", "carol@example.com"),
            ]
            for name, email in users:
                db.execute(
                    "INSERT INTO users (name, email) VALUES (?, ?)",
                    (name, email),
                )
            print("Sample users inserted.")

        print("\nReading committed data:")
        with DatabaseConnection(db_name) as db:
            db.execute("SELECT id, name, email FROM users ORDER BY id")
            for user in db.fetchall():
                print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

        print("\nRollback demonstration:")
        try:
            with DatabaseConnection(db_name) as db:
                db.execute(
                    "INSERT INTO users (name, email) VALUES (?, ?)",
                    ("Temporary User", "temporary@example.com"),
                )
                raise RuntimeError("Simulated database error")
        except RuntimeError as error:
            print("Handled exception:", error)

        with DatabaseConnection(db_name) as db:
            db.execute("SELECT COUNT(*) FROM users WHERE email = ?",
                       ("temporary@example.com",))
            print("Temporary rows after rollback:", db.fetchall()[0][0])
    print("Temporary database removed.")


# ---------------------------------------------------------------------------
# Task 3: Resource acquisition and automatic cleanup
# ---------------------------------------------------------------------------

class ResourceManager:
    """Thread-safe shared simulated resource pool."""
    def __init__(self, resource_name: str, max_connections: int = 3):
        if max_connections < 1:
            raise ValueError("max_connections must be at least 1")
        self.resource_name = resource_name
        self.max_connections = max_connections
        self.active_connections = 0
        self.lock = threading.Lock()
        self.acquired = False

    def __enter__(self):
        print(f"Attempting to acquire resource: {self.resource_name}")
        with self.lock:
            if self.active_connections >= self.max_connections:
                raise RuntimeError(
                    f"Maximum connections ({self.max_connections}) reached "
                    f"for {self.resource_name}"
                )
            self.active_connections += 1
            self.acquired = True
            print(
                f"Resource acquired: {self.resource_name} "
                f"({self.active_connections}/{self.max_connections})"
            )
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if self.acquired:
            with self.lock:
                self.active_connections -= 1
                self.acquired = False
                print(
                    f"Resource released: {self.resource_name} "
                    f"({self.active_connections}/{self.max_connections})"
                )
        if exc_type is not None:
            print(f"Cleanup completed after {exc_type.__name__}.")
        else:
            print("Resource cleanup completed successfully.")
        return False

    def do_work(self, duration: float = 1.0) -> None:
        if not self.acquired:
            raise RuntimeError("Resource has not been acquired.")
        if duration < 0:
            raise ValueError("duration must be non-negative")
        print(f"Working with {self.resource_name} for {duration:.2f}s...")
        time.sleep(duration)
        print(f"Work completed with {self.resource_name}.")


def demo_resource_manager() -> None:
    print("\n=== TASK 3: RESOURCE CLEANUP ===")
    with ResourceManager("Database Connection Pool") as resource:
        resource.do_work(0.1)

    try:
        with ResourceManager("File Handle Pool") as resource:
            resource.do_work(0.05)
            raise ValueError("Simulated processing error")
    except ValueError as error:
        print("Exception handled:", error)

    print("\nConcurrent access to a shared pool:")
    pool = ResourceManager("Shared Resource Pool", max_connections=2)
    results = []

    def worker(worker_id: int) -> None:
        try:
            with pool:
                pool.do_work(0.15)
                results.append((worker_id, "success"))
        except RuntimeError as error:
            print(f"Worker {worker_id}: {error}")
            results.append((worker_id, "rejected"))

    threads = [threading.Thread(target=worker, args=(index,)) for index in range(4)]
    for thread in threads:
        thread.start()
        time.sleep(0.02)
    for thread in threads:
        thread.join()
    print("Worker outcomes:", sorted(results))
    print("Active resources after completion:", pool.active_connections)


# ---------------------------------------------------------------------------
# Task 4: Timing context managers and a decorator
# ---------------------------------------------------------------------------

class Timer:
    """Measure a with block using a monotonic performance clock."""
    def __init__(self, description: str = "Code block", precision: int = 4):
        if precision < 0:
            raise ValueError("precision must be non-negative")
        self.description = description
        self.precision = precision
        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None
        self.elapsed_time: Optional[float] = None

    def __enter__(self):
        print(f"Starting timer for: {self.description}")
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if self.start_time is None:
            raise RuntimeError("Timer was not started.")
        self.end_time = time.perf_counter()
        self.elapsed_time = self.end_time - self.start_time
        if exc_type is not None:
            print(f"Timer stopped due to exception: {exc_type.__name__}")
        print(
            f"Elapsed time for '{self.description}': "
            f"{self.elapsed_time:.{self.precision}f} seconds"
        )
        return False

    def get_elapsed_time(self) -> Optional[float]:
        return self.elapsed_time


class DetailedTimer:
    """Detailed timer with optional console output and log-file output."""
    def __init__(self, description: str = "Code block",
                 show_start_end: bool = True,
                 log_to_file: Optional[str] = None):
        self.description = description
        self.show_start_end = show_start_end
        self.log_to_file = log_to_file
        self.start_time: Optional[float] = None
        self.elapsed_time: Optional[float] = None

    def _log(self, message: str) -> None:
        if self.show_start_end:
            print(message)
        if self.log_to_file:
            with open(self.log_to_file, "a", encoding="utf-8") as file:
                file.write(message + "\n")

    def __enter__(self):
        self.start_time = time.perf_counter()
        self._log(f"[{time.strftime('%H:%M:%S')}] Starting: {self.description}")
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if self.start_time is None:
            raise RuntimeError("Timer was not started.")
        self.elapsed_time = time.perf_counter() - self.start_time
        if self.elapsed_time < 1:
            duration = f"{self.elapsed_time * 1000:.2f} ms"
        elif self.elapsed_time < 60:
            duration = f"{self.elapsed_time:.4f} seconds"
        else:
            duration = f"{int(self.elapsed_time // 60)}m {self.elapsed_time % 60:.2f}s"
        status = "COMPLETED" if exc_type is None else f"FAILED ({exc_type.__name__})"
        self._log(
            f"[{time.strftime('%H:%M:%S')}] {status}: "
            f"{self.description} - Duration: {duration}"
        )
        return False


def timed_function(description: Optional[str] = None):
    """Create a decorator that times a function with the Timer manager."""
    def decorator(function):
        import functools

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            label = description or f"Function '{function.__name__}'"
            with Timer(label):
                return function(*args, **kwargs)
        return wrapper
    return decorator


@timed_function("Fibonacci calculation")
def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number iteratively."""
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def demo_timing_context_managers() -> None:
    print("\n=== TASK 4: TIMING CONTEXT MANAGERS ===")
    with Timer("Fast operation") as timer:
        time.sleep(0.05)
    with Timer("Slow operation", precision=2) as timer:
        time.sleep(0.1)
    print(f"Last operation took: {timer.get_elapsed_time():.2f} seconds")

    with DetailedTimer("File processing simulation", log_to_file="timing_log.txt"):
        print("Processing files...")
        time.sleep(0.05)
        print("Files processed successfully.")

    try:
        with DetailedTimer("Operation that fails"):
            raise ValueError("Simulated processing error")
    except ValueError as error:
        print("Handled exception:", error)

    with Timer("Complete workflow"):
        with Timer("Step 1: Data loading"):
            time.sleep(0.02)
        with Timer("Step 2: Data processing"):
            time.sleep(0.02)
        with Timer("Step 3: Data saving"):
            time.sleep(0.02)

    print("Fibonacci(25) =", fibonacci(25))
    print("Detailed timing entries are in timing_log.txt.")


# ---------------------------------------------------------------------------
# Task 5: Temporary directories, environment configuration, and contextlib
# ---------------------------------------------------------------------------

class TemporaryDirectory:
    """Create a temporary directory and optionally remove it on exit."""
    def __init__(self, prefix: str = "temp_", suffix: str = "",
                 base_dir: Optional[str] = None, cleanup: bool = True):
        self.prefix = prefix
        self.suffix = suffix
        self.base_dir = base_dir
        self.cleanup = cleanup
        self.temp_dir: Optional[str] = None

    def __enter__(self) -> Path:
        self.temp_dir = tempfile.mkdtemp(
            prefix=self.prefix, suffix=self.suffix, dir=self.base_dir
        )
        print(f"Created temporary directory: {self.temp_dir}")
        return Path(self.temp_dir)

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        if self.temp_dir and self.cleanup:
            shutil.rmtree(self.temp_dir)
            print(f"Cleaned up temporary directory: {self.temp_dir}")
        elif self.temp_dir:
            print(f"Temporary directory preserved: {self.temp_dir}")
        return False


class ConfigurationManager:
    """Temporarily set environment variables and restore their prior state."""
    def __init__(self, **config_changes):
        self.config_changes = config_changes
        self.original_values = {}

    def __enter__(self):
        print("Applying temporary configuration changes:")
        for key, value in self.config_changes.items():
            self.original_values[key] = os.environ.get(key)
            os.environ[key] = str(value)
            print(f"  {key}: {self.original_values[key]} -> {value}")
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        print("Restoring original configuration:")
        for key, original_value in self.original_values.items():
            if original_value is None:
                os.environ.pop(key, None)
                print(f"  {key}: removed (was not set)")
            else:
                os.environ[key] = original_value
                print(f"  {key}: restored")
        return False


@contextmanager
def simple_timer(description: str):
    """Generator-based timer implemented with contextlib.contextmanager."""
    print(f"Starting: {description}")
    start = time.perf_counter()
    try:
        yield start
    finally:
        elapsed = time.perf_counter() - start
        print(f"Completed: {description} in {elapsed:.4f} seconds")


@contextmanager
def temporary_file(content: str = "", suffix: str = ".txt"):
    """Create a temporary file and delete it after the context exits."""
    path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=suffix, encoding="utf-8", delete=False
        ) as file:
            file.write(content)
            path = file.name
        print(f"Created temporary file: {path}")
        yield path
    finally:
        if path and os.path.exists(path):
            os.unlink(path)
            print(f"Cleaned up temporary file: {path}")


@contextmanager
def error_handler(error_types):
    """Suppress and report only the supplied exception type(s)."""
    try:
        yield
    except error_types as error:
        print(f"Handled error: {type(error).__name__}: {error}")


def demo_temporary_directory_and_configuration() -> None:
    print("\n=== TASK 5: TEMPORARY DIRECTORY ===")
    with TemporaryDirectory(prefix="lab51_demo_") as temp_dir:
        (temp_dir / "test.txt").write_text(
            "Temporary content.", encoding="utf-8"
        )
        sub_dir = temp_dir / "subdir"
        sub_dir.mkdir()
        (sub_dir / "nested.txt").write_text("Nested content.", encoding="utf-8")
        for item in temp_dir.rglob("*"):
            print(" ", item.relative_to(temp_dir))

    print("\n=== CONFIGURATION MANAGER ===")
    print("Before:", os.environ.get("LAB51_TEST_VAR", "NOT SET"))
    with ConfigurationManager(
        LAB51_TEST_VAR="temporary_value",
        LAB51_DEMO_MODE="true",
        LAB51_DEBUG_LEVEL="verbose",
    ):
        print("Inside:", os.environ.get("LAB51_TEST_VAR"))
        print("Demo mode:", os.environ.get("LAB51_DEMO_MODE"))
    print("After:", os.environ.get("LAB51_TEST_VAR", "NOT SET"))

    print("\n=== COMBINED CONTEXT MANAGERS ===")
    with TemporaryDirectory(prefix="config_test_") as temp_dir, ConfigurationManager(
        LAB51_WORKSPACE=str(temp_dir), LAB51_LOG_LEVEL="DEBUG"
    ):
        config_file = temp_dir / "app.conf"
        config_file.write_text(
            "[settings]\n"
            f"workspace = {os.environ.get('LAB51_WORKSPACE')}\n"
            f"log_level = {os.environ.get('LAB51_LOG_LEVEL')}\n",
            encoding="utf-8",
        )
        print(config_file.read_text(encoding="utf-8"))


def demo_contextlib() -> None:
    print("\n=== CONTEXTLIB: @contextmanager ===")
    with simple_timer("Short operation") as started:
        print("Timer started at:", started)
        time.sleep(0.03)

    print("\n=== CONTEXTLIB: TEMPORARY FILE ===")
    with temporary_file("Sample content\nSecond line", suffix=".log") as path:
        with open(path, "r", encoding="utf-8") as file:
            print(file.read())
        print("File size:", os.path.getsize(path), "bytes")
    print("File exists after exit:", os.path.exists(path))

    print("\n=== CONTEXTLIB: ERROR HANDLER ===")
    with error_handler((ValueError, TypeError)):
        raise ValueError("This error is intentionally handled.")
    print("Execution continues after the handled error.")

    operations = [lambda: int("123"), lambda: int("abc"), lambda: 10 / 0]
    for index, operation in enumerate(operations, start=1):
        try:
            with error_handler((ValueError, TypeError)):
                print(f"Operation {index} result:", operation())
        except ZeroDivisionError as error:
            print("Unhandled error:", error)

    print("\n=== CONTEXTLIB: EXITSTACK ===")
    with ExitStack() as stack:
        stack.enter_context(simple_timer("Operation 1"))
        paths = []
        for index in range(3):
            path = stack.enter_context(
                temporary_file(f"Content for file {index + 1}", suffix=f"_{index + 1}.txt")
            )
            paths.append(path)
        stack.enter_context(simple_timer("Operation 2"))
        for index, path in enumerate(paths, start=1):
            with open(path, "r", encoding="utf-8") as file:
                print(f"File {index}:", file.read().strip())
        time.sleep(0.03)

    print("\n=== CONTEXTLIB: SUPPRESS ===")
    with suppress(FileNotFoundError):
        with open("lab51_nonexistent_file.txt", "r", encoding="utf-8") as file:
            print(file.read())
    print("Execution continued after FileNotFoundError was suppressed.")


def main() -> None:
    print("LAB 51: CONTEXT MANAGERS — COMPLETE DEMONSTRATION")
    print("=" * 64)
    demo_file_operations()
    demo_basic_context_manager()
    demo_database_context_manager()
    demo_resource_manager()
    demo_timing_context_managers()
    demo_temporary_directory_and_configuration()
    demo_contextlib()
    print("\n" + "=" * 64)
    print("LAB COMPLETED SUCCESSFULLY!")


if __name__ == "__main__":
    main()
