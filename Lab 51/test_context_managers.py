"""Unit tests for Lab 51 context managers."""
import os
import sqlite3
import tempfile
import unittest
from pathlib import Path

from context_managers_lab import (
    BasicContextManager, ConfigurationManager, DatabaseConnection,
    ResourceManager, TemporaryDirectory, Timer, error_handler, temporary_file
)


class ContextManagerTests(unittest.TestCase):
    def test_basic_manager_returns_self_and_propagates_exception(self):
        manager = BasicContextManager("test")
        with manager as entered:
            self.assertIs(entered, manager)
        with self.assertRaises(ValueError):
            with BasicContextManager("failure"):
                raise ValueError("expected")

    def test_database_manager_commits_successful_transaction(self):
        with tempfile.TemporaryDirectory() as directory:
            database = str(Path(directory) / "test.db")
            with DatabaseConnection(database) as db:
                db.execute("CREATE TABLE records (value TEXT)")
                db.execute("INSERT INTO records VALUES (?)", ("saved",))
            with DatabaseConnection(database) as db:
                db.execute("SELECT value FROM records")
                self.assertEqual(db.fetchall(), [("saved",)])

    def test_database_manager_rolls_back_failed_transaction(self):
        with tempfile.TemporaryDirectory() as directory:
            database = str(Path(directory) / "test.db")
            with DatabaseConnection(database) as db:
                db.execute("CREATE TABLE records (value TEXT)")
            with self.assertRaises(RuntimeError):
                with DatabaseConnection(database) as db:
                    db.execute("INSERT INTO records VALUES (?)", ("not saved",))
                    raise RuntimeError("rollback")
            with DatabaseConnection(database) as db:
                db.execute("SELECT COUNT(*) FROM records")
                self.assertEqual(db.fetchall()[0][0], 0)

    def test_resource_manager_releases_after_exception(self):
        pool = ResourceManager("test pool", max_connections=1)
        with self.assertRaises(ValueError):
            with pool:
                self.assertTrue(pool.acquired)
                raise ValueError("simulated")
        self.assertFalse(pool.acquired)
        self.assertEqual(pool.active_connections, 0)

    def test_resource_limit_is_enforced(self):
        pool = ResourceManager("limited pool", max_connections=1)
        with pool:
            with self.assertRaises(RuntimeError):
                with pool:
                    pass
        self.assertEqual(pool.active_connections, 0)

    def test_timer_records_elapsed_time_after_exception(self):
        timer = Timer("test")
        with self.assertRaises(ValueError):
            with timer:
                raise ValueError("expected")
        self.assertIsNotNone(timer.get_elapsed_time())
        self.assertGreaterEqual(timer.get_elapsed_time(), 0)

    def test_temporary_directory_cleanup(self):
        with TemporaryDirectory(prefix="lab51_test_") as directory:
            self.assertTrue(directory.exists())
            (directory / "marker.txt").write_text("test", encoding="utf-8")
        self.assertFalse(directory.exists())

    def test_environment_configuration_is_restored(self):
        key = "LAB51_UNIT_TEST_TEMP_VALUE"
        old_value = os.environ.get(key)
        os.environ.pop(key, None)
        try:
            with ConfigurationManager(**{key: "inside"}):
                self.assertEqual(os.environ[key], "inside")
            self.assertNotIn(key, os.environ)
        finally:
            if old_value is not None:
                os.environ[key] = old_value

    def test_temporary_file_is_removed(self):
        with temporary_file("hello", suffix=".txt") as path:
            self.assertTrue(os.path.exists(path))
            with open(path, "r", encoding="utf-8") as file:
                self.assertEqual(file.read(), "hello")
        self.assertFalse(os.path.exists(path))

    def test_error_handler_only_suppresses_requested_errors(self):
        with error_handler(ValueError):
            raise ValueError("handled")
        with self.assertRaises(TypeError):
            with error_handler(ValueError):
                raise TypeError("not handled")


if __name__ == "__main__":
    unittest.main(verbosity=2)
