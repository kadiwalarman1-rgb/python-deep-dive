"""Unit tests for Lab 48. Run with: python3 -m unittest -v"""
import unittest
from datetime import datetime, timedelta
from library_management_system import Book, Library, Librarian, Person, User


class LibraryManagementSystemTests(unittest.TestCase):
    def setUp(self):
        self.library = Library("Test Library", "1 Test Street", daily_fine_rate=2.0)
        self.librarian = Librarian("L1", "Lena Staff", "lena@library.test", "123", "E1", "Circulation")
        self.user = User("U1", "Arman Reader", "arman@library.test", "456")
        self.other_user = User("U2", "Sara Reader", "sara@library.test", "789", "premium")
        self.book = Book("ISBN-001", "Python Basics", "A. Author", "Technology", 2024)
        self.library.register_librarian(self.librarian)
        self.library.register_user(self.user)
        self.library.register_user(self.other_user)
        self.library.add_book(self.book)

    def test_duplicate_records_are_rejected(self):
        self.assertFalse(self.library.add_book(Book("ISBN-001", "Duplicate", "Author", "Fiction", 2020)))
        self.assertFalse(self.library.register_user(User("U1", "Other Name", "other@example.com", "000")))
        duplicate = Librarian("L2", "Another Staff", "another@library.test", "111", "E1", "Reference")
        self.assertFalse(self.library.register_librarian(duplicate))

    def test_borrow_and_return(self):
        self.assertEqual(self.library.borrow_book("U1", "ISBN-001"), "Book borrowed successfully")
        self.assertFalse(self.book.is_available)
        self.assertIn("ISBN-001", self.user.borrowed_books)
        self.assertEqual(self.library.borrow_book("U2", "ISBN-001"), "Book is not available")
        self.assertEqual(self.library.return_book("U1", "ISBN-001"), "Book returned successfully")
        self.assertTrue(self.book.is_available)
        self.assertEqual(self.user.borrowed_books, [])

    def test_cannot_return_another_users_book(self):
        self.library.borrow_book("U1", "ISBN-001")
        self.assertEqual(self.library.return_book("U2", "ISBN-001"), "User has not borrowed this book")
        self.assertEqual(self.book.borrowed_by, "U1")

    def test_overdue_return_adds_fine(self):
        self.library.borrow_book("U1", "ISBN-001")
        self.book._Book__due_date = datetime.now() - timedelta(days=2, hours=1)
        self.assertEqual(self.library.return_book("U1", "ISBN-001"), "Book returned with fine: $6.00")
        self.assertEqual(self.user.fine_amount, 6.0)
        self.assertEqual(self.library.generate_report("users")["users_with_fines"], 1)

    def test_fine_must_be_paid_before_borrowing(self):
        self.user.add_fine(5.0)
        self.assertFalse(self.user.can_borrow())
        self.assertEqual(self.user.pay_fine(2.0), 0.0)
        self.assertEqual(self.user.fine_amount, 3.0)
        self.assertEqual(self.user.pay_fine(5.0), 2.0)
        self.assertEqual(self.user.fine_amount, 0.0)
        self.assertTrue(self.user.can_borrow())

    def test_search_sort_operators(self):
        older = Book("ISBN-002", "Older Book", "B. Writer", "Fiction", 1999)
        self.library.add_book(older)
        self.assertEqual(self.library.find_book(title="python")[0], self.book)
        self.assertEqual(sorted([self.book, older])[0], older)
        self.assertEqual(len(self.library), 2)
        self.assertIn(self.book, self.library)
        self.assertIn("U1", self.library)
        self.assertNotIn("missing", self.library)
        self.assertEqual(self.book, Book("ISBN-001", "Different title", "Other", "Other", 2020))

    def test_person_validation(self):
        with self.assertRaises(ValueError): Person("P1", "A", "p@example.com", "123")
        with self.assertRaises(ValueError): Person("P2", "Valid Name", "not-an-email", "123")

    def test_reports_and_membership_upgrade(self):
        self.assertEqual(self.library.generate_report("books")["total_books"], 1)
        self.assertEqual(self.library.generate_report("overdue")["total_overdue"], 0)
        self.assertEqual(self.library.generate_report("unknown")["error"], "Unknown report type: unknown")
        self.assertTrue(self.user.upgrade_membership())
        self.assertEqual(self.user.membership_type, "premium")
        self.assertEqual(self.user.max_books, 5)
        self.assertFalse(self.user.upgrade_membership())


if __name__ == "__main__":
    unittest.main(verbosity=2)
