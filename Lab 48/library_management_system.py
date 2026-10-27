#!/usr/bin/env python3
"""Lab 48: Complete OOP Library Management System. Python 3.8+, standard library only."""
from datetime import datetime, timedelta
from math import ceil
from typing import Dict, List, Optional


class Person:
    """Base class with encapsulated identity and validated properties."""
    def __init__(self, person_id: str, name: str, email: str, phone: str):
        if not person_id or not person_id.strip():
            raise ValueError("Person ID cannot be empty")
        self.__person_id = person_id.strip()
        self.__created_date = datetime.now()
        self.__phone = phone.strip() if phone else ""
        self.__name = self.__email = ""
        self.name, self.email = name, email

    @property
    def person_id(self) -> str: return self.__person_id
    @property
    def name(self) -> str: return self.__name
    @name.setter
    def name(self, value: str) -> None:
        if not value or len(value.strip()) < 2:
            raise ValueError("Name must be at least 2 characters long")
        self.__name = value.strip()
    @property
    def email(self) -> str: return self.__email
    @email.setter
    def email(self, value: str) -> None:
        value = value.strip() if value else ""
        if "@" not in value or "." not in value.rsplit("@", 1)[-1]:
            raise ValueError("Invalid email format")
        self.__email = value
    @property
    def phone(self) -> str: return self.__phone
    @property
    def created_date(self) -> datetime: return self.__created_date
    def __str__(self) -> str: return f"{type(self).__name__}: {self.name} ({self.person_id})"
    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.person_id!r}, {self.name!r}, {self.email!r}, {self.phone!r})"
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Person) and self.person_id == other.person_id
    def __hash__(self) -> int: return hash(self.person_id)


class Book:
    """Catalog entity with loan state and publication-year comparison operators."""
    def __init__(self, isbn: str, title: str, author: str, genre: str, publication_year: int):
        for label, value in (("ISBN", isbn), ("Title", title), ("Author", author), ("Genre", genre)):
            if not value or not value.strip(): raise ValueError(label + " cannot be empty")
        if not isinstance(publication_year, int) or publication_year < 0:
            raise ValueError("Publication year must be a non-negative integer")
        self.__isbn, self.__title = isbn.strip(), title.strip()
        self.__author, self.__genre = author.strip(), genre.strip()
        self.__publication_year = publication_year
        self.__is_available, self.__borrowed_by, self.__due_date = True, None, None
        self.__borrow_count = 0

    @property
    def isbn(self) -> str: return self.__isbn
    @property
    def title(self) -> str: return self.__title
    @property
    def author(self) -> str: return self.__author
    @property
    def genre(self) -> str: return self.__genre
    @property
    def publication_year(self) -> int: return self.__publication_year
    @property
    def is_available(self) -> bool: return self.__is_available
    @property
    def borrowed_by(self) -> Optional[str]: return self.__borrowed_by
    @property
    def due_date(self) -> Optional[datetime]: return self.__due_date
    @property
    def borrow_count(self) -> int: return self.__borrow_count

    def borrow(self, user_id: str, days: int = 14) -> bool:
        if not self.__is_available or not user_id or days <= 0: return False
        self.__is_available, self.__borrowed_by = False, user_id
        self.__due_date = datetime.now() + timedelta(days=days)
        self.__borrow_count += 1
        return True

    def return_book(self) -> bool:
        if self.__is_available: return False
        self.__is_available, self.__borrowed_by, self.__due_date = True, None, None
        return True

    def is_overdue(self) -> bool:
        return bool(not self.__is_available and self.__due_date and datetime.now() > self.__due_date)
    def __str__(self) -> str:
        state = "Available" if self.__is_available else "Borrowed by " + str(self.__borrowed_by)
        return f"'{self.__title}' by {self.__author} ({self.__publication_year}) - {state}"
    def __repr__(self) -> str:
        return f"Book({self.__isbn!r}, {self.__title!r}, {self.__author!r}, {self.__genre!r}, {self.__publication_year})"
    def __eq__(self, other: object) -> bool: return isinstance(other, Book) and self.isbn == other.isbn
    def __hash__(self) -> int: return hash(self.isbn)
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Book): return NotImplemented
        return (self.publication_year, self.title.casefold()) < (other.publication_year, other.title.casefold())
    def __le__(self, other: object) -> bool:
        if not isinstance(other, Book): return NotImplemented
        return self == other or self < other
    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Book): return NotImplemented
        return not self <= other
    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Book): return NotImplemented
        return not self < other


class User(Person):
    """Library member with borrowing limits, history, membership, and fines."""
    def __init__(self, person_id: str, name: str, email: str, phone: str, membership_type: str = "standard"):
        super().__init__(person_id, name, email, phone)
        membership_type = membership_type.strip().lower()
        if membership_type not in {"standard", "premium"}:
            raise ValueError("Membership type must be standard or premium")
        self.__membership_type = membership_type
        self.__borrowed_books: List[str] = []
        self.__borrow_history: List[dict] = []
        self.__fine_amount = 0.0
        self.__max_books = 3 if membership_type == "standard" else 5

    @property
    def membership_type(self) -> str: return self.__membership_type
    @property
    def borrowed_books(self) -> List[str]: return self.__borrowed_books.copy()
    @property
    def borrow_history(self) -> List[dict]: return [item.copy() for item in self.__borrow_history]
    @property
    def fine_amount(self) -> float: return self.__fine_amount
    @property
    def max_books(self) -> int: return self.__max_books
    def can_borrow(self) -> bool:
        return len(self.__borrowed_books) < self.__max_books and self.__fine_amount <= 0
    def borrow_book(self, isbn: str) -> bool:
        if not self.can_borrow() or isbn in self.__borrowed_books: return False
        self.__borrowed_books.append(isbn)
        self.__borrow_history.append({"isbn": isbn, "borrowed_date": datetime.now(), "returned_date": None})
        return True
    def return_book(self, isbn: str) -> bool:
        if isbn not in self.__borrowed_books: return False
        self.__borrowed_books.remove(isbn)
        for record in reversed(self.__borrow_history):
            if record["isbn"] == isbn and record["returned_date"] is None:
                record["returned_date"] = datetime.now()
                break
        return True
    def add_fine(self, amount: float) -> None:
        if amount < 0: raise ValueError("Fine cannot be negative")
        self.__fine_amount = round(self.__fine_amount + amount, 2)
    def pay_fine(self, amount: float) -> float:
        if amount < 0: raise ValueError("Payment cannot be negative")
        paid = min(amount, self.__fine_amount)
        self.__fine_amount = round(self.__fine_amount - paid, 2)
        return round(amount - paid, 2)
    def upgrade_membership(self) -> bool:
        if self.__membership_type == "premium": return False
        self.__membership_type, self.__max_books = "premium", 5
        return True
    def __str__(self) -> str:
        return f"User: {self.name} ({self.person_id}) - {self.__membership_type.title()} Member"


class Librarian(Person):
    """Librarian staff member with simple activity reporting."""
    def __init__(self, person_id: str, name: str, email: str, phone: str, employee_id: str, department: str):
        super().__init__(person_id, name, email, phone)
        if not employee_id or not employee_id.strip() or not department or not department.strip():
            raise ValueError("Employee ID and department cannot be empty")
        self.__employee_id, self.__department = employee_id.strip(), department.strip()
        self.__books_processed, self.__users_helped = 0, set()
    @property
    def employee_id(self) -> str: return self.__employee_id
    @property
    def department(self) -> str: return self.__department
    @property
    def books_processed(self) -> int: return self.__books_processed
    @property
    def users_helped_count(self) -> int: return len(self.__users_helped)
    def process_book(self) -> None: self.__books_processed += 1
    def help_user(self, user_id: str) -> None: self.__users_helped.add(user_id)
    def generate_report(self) -> dict:
        return {"employee_id": self.__employee_id, "name": self.name, "department": self.__department,
                "books_processed": self.__books_processed, "users_helped": len(self.__users_helped),
                "efficiency_score": round(self.__books_processed * 0.5 + len(self.__users_helped) * 0.3, 2)}
    def __str__(self) -> str:
        return f"Librarian: {self.name} ({self.employee_id}) - {self.__department} Department"


class Library:
    """Coordinates catalog, members, loans, returns, fines, and reporting."""
    def __init__(self, name: str, address: str, daily_fine_rate: float = 1.0):
        if not name or not name.strip() or not address or not address.strip():
            raise ValueError("Library name and address cannot be empty")
        if daily_fine_rate < 0: raise ValueError("Fine rate cannot be negative")
        self.__name, self.__address = name.strip(), address.strip()
        self.__books: Dict[str, Book] = {}
        self.__users: Dict[str, User] = {}
        self.__librarians: Dict[str, Librarian] = {}
        self.__daily_fine_rate = float(daily_fine_rate)
    @property
    def name(self) -> str: return self.__name
    @property
    def address(self) -> str: return self.__address
    @property
    def total_books(self) -> int: return len(self.__books)
    @property
    def total_users(self) -> int: return len(self.__users)
    @property
    def available_books_count(self) -> int: return sum(book.is_available for book in self.__books.values())
    def get_book(self, isbn: str) -> Optional[Book]: return self.__books.get(isbn)
    def get_user(self, user_id: str) -> Optional[User]: return self.__users.get(user_id)
    def get_librarian(self, employee_id: str) -> Optional[Librarian]: return self.__librarians.get(employee_id)
    def add_book(self, book: Book, librarian: Optional[Librarian] = None) -> bool:
        if not isinstance(book, Book) or book.isbn in self.__books: return False
        self.__books[book.isbn] = book
        if librarian: librarian.process_book()
        return True
    def remove_book(self, isbn: str, librarian: Optional[Librarian] = None) -> bool:
        book = self.__books.get(isbn)
        if book is None or not book.is_available: return False
        del self.__books[isbn]
        if librarian: librarian.process_book()
        return True
    def find_book(self, **criteria) -> List[Book]:
        allowed = {"title", "author", "genre", "available", "isbn", "publication_year"}
        unknown = set(criteria) - allowed
        if unknown: raise ValueError("Unsupported search criteria: " + ", ".join(sorted(unknown)))
        result = []
        for book in self.__books.values():
            matched = True
            for key, value in criteria.items():
                if key in {"title", "author", "genre", "isbn"}:
                    matched = str(value).casefold() in getattr(book, key).casefold()
                elif key == "available": matched = book.is_available == value
                elif key == "publication_year": matched = book.publication_year == value
                if not matched: break
            if matched: result.append(book)
        return result
    def register_user(self, user: User, librarian: Optional[Librarian] = None) -> bool:
        if not isinstance(user, User) or user.person_id in self.__users: return False
        self.__users[user.person_id] = user
        if librarian: librarian.help_user(user.person_id)
        return True
    def register_librarian(self, librarian: Librarian) -> bool:
        if not isinstance(librarian, Librarian) or librarian.employee_id in self.__librarians: return False
        self.__librarians[librarian.employee_id] = librarian
        return True
    def borrow_book(self, user_id: str, isbn: str, librarian: Optional[Librarian] = None) -> str:
        user = self.__users.get(user_id)
        if user is None: return "User not found"
        if not user.can_borrow(): return "User cannot borrow more books or has outstanding fines"
        book = self.__books.get(isbn)
        if book is None: return "Book not found"
        if not book.is_available: return "Book is not available"
        if isbn in user.borrowed_books: return "User has already borrowed this book"
        if book.borrow(user_id) and user.borrow_book(isbn):
            if librarian:
                librarian.process_book()
                librarian.help_user(user_id)
            return "Book borrowed successfully"
        return "Failed to borrow book"
    def return_book(self, user_id: str, isbn: str, librarian: Optional[Librarian] = None) -> str:
        user, book = self.__users.get(user_id), self.__books.get(isbn)
        if user is None or book is None: return "User or book not found"
        if isbn not in user.borrowed_books or book.borrowed_by != user_id:
            return "User has not borrowed this book"
        fine = 0.0
        if book.is_overdue() and book.due_date:
            seconds = (datetime.now() - book.due_date).total_seconds()
            fine = round(max(1, ceil(seconds / 86400)) * self.__daily_fine_rate, 2)
        if not book.return_book() or not user.return_book(isbn): return "Failed to return book"
        if fine: user.add_fine(fine)
        if librarian:
            librarian.process_book()
            librarian.help_user(user_id)
        return "Book returned with fine: $" + format(fine, ".2f") if fine else "Book returned successfully"
    def __len__(self) -> int: return len(self.__books)
    def __contains__(self, item: object) -> bool:
        if isinstance(item, str): return item in self.__books or item in self.__users
        if isinstance(item, Book): return item.isbn in self.__books
        if isinstance(item, User): return item.person_id in self.__users
        return False
    def __str__(self) -> str:
        return f"{self.__name} Library - {len(self.__books)} books, {len(self.__users)} users"
    def __repr__(self) -> str: return f"Library({self.__name!r}, {self.__address!r})"
    def generate_report(self, report_type: str) -> dict:
        reports = {"books": self._books_report, "users": self._users_report,
                   "overdue": self._overdue_report, "librarians": self._librarians_report}
        generator = reports.get(report_type.casefold())
        return generator() if generator else {"error": f"Unknown report type: {report_type}"}
    def _books_report(self) -> dict:
        available = self.available_books_count
        genres: Dict[str, int] = {}
        for book in self.__books.values(): genres[book.genre] = genres.get(book.genre, 0) + 1
        return {"report_type": "Books Report", "total_books": len(self.__books),
                "available_books": available, "borrowed_books": len(self.__books) - available,
                "genre_distribution": genres, "generated_at": datetime.now().isoformat(timespec="seconds")}
    def _users_report(self) -> dict:
        users, memberships = list(self.__users.values()), {}
        for user in users: memberships[user.membership_type] = memberships.get(user.membership_type, 0) + 1
        return {"report_type": "Users Report", "total_users": len(users),
                "active_borrowers": sum(bool(user.borrowed_books) for user in users),
                "users_with_fines": sum(user.fine_amount > 0 for user in users),
                "membership_distribution": memberships, "generated_at": datetime.now().isoformat(timespec="seconds")}
    def _overdue_report(self) -> dict:
        overdue = []
        for book in self.__books.values():
            if book.is_overdue() and book.due_date:
                days = max(1, ceil((datetime.now() - book.due_date).total_seconds() / 86400))
                overdue.append({"isbn": book.isbn, "title": book.title, "borrowed_by": book.borrowed_by,
                                "due_date": book.due_date.isoformat(timespec="seconds"), "days_overdue": days,
                                "fine_amount": round(days * self.__daily_fine_rate, 2)})
        return {"report_type": "Overdue Books Report", "total_overdue": len(overdue), "overdue_books": overdue,
                "total_fines": round(sum(row["fine_amount"] for row in overdue), 2),
                "generated_at": datetime.now().isoformat(timespec="seconds")}
    def _librarians_report(self) -> dict:
        stats = [item.generate_report() for item in self.__librarians.values()]
        return {"report_type": "Librarians Performance Report", "total_librarians": len(stats),
                "librarian_stats": stats, "generated_at": datetime.now().isoformat(timespec="seconds")}


def test_library_system() -> None:
    """Full demo covering registration, borrowing, searching, operators, and reports."""
    print("=" * 64)
    print("LIBRARY MANAGEMENT SYSTEM - COMPREHENSIVE DEMONSTRATION")
    print("=" * 64)
    library = Library("Central City Library", "123 Main Street, Central City")
    librarian1 = Librarian("L001", "Alice Johnson", "alice@library.com", "555-0101", "EMP001", "Circulation")
    librarian2 = Librarian("L002", "Bob Smith", "bob@library.com", "555-0102", "EMP002", "Reference")
    library.register_librarian(librarian1)
    library.register_librarian(librarian2)
    books = [
        Book("978-0-123456-78-9", "Python Programming", "John Doe", "Technology", 2023),
        Book("978-0-987654-32-1", "Data Structures", "Jane Smith", "Technology", 2022),
        Book("978-0-456789-01-2", "Machine Learning", "AI Expert", "Technology", 2024),
        Book("978-0-789012-34-5", "The Great Novel", "Famous Author", "Fiction", 2021),
        Book("978-0-345678-90-1", "History of Science", "Science Writer", "Science", 2020),
    ]
    for book in books: print("Adding", book.title, library.add_book(book, librarian1))
    users = [User("U001", "Charlie Brown", "charlie@email.com", "555-1001"),
             User("U002", "Diana Prince", "diana@email.com", "555-1002", "premium"),
             User("U003", "Edward Norton", "edward@email.com", "555-1003")]
    for user in users: print("Registering", user, library.register_user(user, librarian2))
    print("\nBorrowing transactions:")
    for user_id, isbn in [("U001", books[0].isbn), ("U002", books[1].isbn),
                          ("U001", books[2].isbn), ("U003", books[3].isbn), ("U001", books[4].isbn)]:
        user, book = library.get_user(user_id), library.get_book(isbn)
        print(user.name, "->", book.title, ":", library.borrow_book(user_id, isbn, librarian1))
    print("\nSearch by author:", library.find_book(author="John Doe"))
    print("Available technology books:", library.find_book(genre="Technology", available=True))
    print("\nBook comparison:", books[0].title, "newer than", books[1].title, "=", books[0] > books[1])
    print("Sorted books:", [(book.publication_year, book.title) for book in sorted(books)])
    print("\nLibrary operators: len =", len(library), "| book present =", books[0] in library, "| U001 present =", "U001" in library)
    print("\nReports:")
    for kind in ("books", "users", "overdue", "librarians"): print(kind, "=>", library.generate_report(kind))
    print("\nReturns:")
    print(library.return_book("U001", books[0].isbn, librarian2))
    print(library.return_book("U002", books[1].isbn, librarian2))
    charlie = library.get_user("U001")
    print("\nMembership before:", charlie.membership_type, charlie.max_books)
    charlie.upgrade_membership()
    print("Membership after:", charlie.membership_type, charlie.max_books)
    print("\nFinal status:", library, "| available:", library.available_books_count, "/", library.total_books)
    print("repr(book):", repr(books[0]))
    print("\nLAB COMPLETED SUCCESSFULLY!")


if __name__ == "__main__":
    test_library_system()
