"""Automated unit tests for Lab 49 decorators."""
import contextlib
import io
import unittest

import decorator_lab as lab


class DecoratorLabTests(unittest.TestCase):
    def setUp(self):
        lab.current_user = None

    def test_time_logger_returns_result_and_preserves_metadata(self):
        @lab.time_logger
        def sample(value):
            """Sample function docstring."""
            return value * 2

        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(sample(4), 8)
        self.assertIn("Starting execution of sample", output.getvalue())
        self.assertIn("executed in", output.getvalue())
        self.assertEqual(sample.__name__, "sample")
        self.assertEqual(sample.__doc__, "Sample function docstring.")

    def test_authorization_denies_anonymous_and_guest(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertIsNone(lab.delete_user("alice"))
            lab.current_user = "guest"
            self.assertIsNone(lab.delete_user("alice"))
        self.assertIn("No user logged in", output.getvalue())
        self.assertIn("not authorized", output.getvalue())

    def test_authorization_allows_admin(self):
        lab.current_user = "admin"
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(lab.delete_user("alice"), "User alice has been deleted")

    def test_input_validator_rejects_none(self):
        lab.current_user = "admin"
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertIsNone(lab.process_user_data(None, "update"))
            self.assertEqual(
                lab.process_user_data("U1", "update"),
                "[FORMATTED] Processed action 'update' for user U1",
            )

    def test_result_formatter_leaves_none_unchanged(self):
        @lab.result_formatter
        def no_result():
            return None
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertIsNone(no_result())

    def test_wraps_preserves_metadata(self):
        self.assertEqual(lab.function_with_good_decorator.__name__, "function_with_good_decorator")
        self.assertIn("preserved", lab.function_with_good_decorator.__doc__)
        self.assertEqual(lab.function_with_bad_decorator.__name__, "wrapper")

    def test_parameterized_metadata_and_factorial(self):
        self.assertEqual(lab.factorial.decorator_description, "Calculates factorial of a number")
        self.assertTrue(lab.factorial.is_decorated)
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(lab.factorial(5), 120)
        with self.assertRaises(ValueError):
            lab.factorial(-1)

    def test_current_user_can_be_switched(self):
        lab.current_user = "developer"
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(
                lab.modify_system_settings("log_level", "debug"),
                "System setting 'log_level' changed to 'debug'",
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
