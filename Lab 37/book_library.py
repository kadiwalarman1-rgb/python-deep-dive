"""Book constructor, circulation, review, and display examples."""

from datetime import datetime


class Book:
    """Represent a library book with borrowing and review information."""

    def __init__(self, title, author, isbn, publication_year, genre, pages=0, price=0.0):
        for label, value in (("Title", title), ("Author", author), ("ISBN", isbn), ("Genre", genre)):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{label} cannot be empty")
        if not isinstance(publication_year, int) or isinstance(publication_year, bool) or publication_year <= 0:
            raise ValueError("Publication year must be a positive integer")
        if not isinstance(pages, int) or isinstance(pages, bool) or pages < 0:
            raise ValueError("Pages must be a non-negative integer")
        if isinstance(price, bool) or not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number")
        self.title = title.strip()
        self.author = author.strip()
        self.isbn = isbn.strip()
        self.publication_year = publication_year
        self.genre = genre.strip()
        self.pages = pages
        self.price = float(price)
        self.is_available = True
        self.borrowed_date = None
        self.borrower_name = None
        self.rating = 0.0
        self.reviews = []

    def borrow_book(self, borrower_name):
        """Borrow a book if it is available."""
        if not isinstance(borrower_name, str) or not borrower_name.strip():
            return "Borrower name cannot be empty"
        if not self.is_available:
            return f"✗ Book '{self.title}' is currently borrowed by {self.borrower_name}"
        self.is_available = False
        self.borrower_name = borrower_name.strip()
        self.borrowed_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"✓ Book '{self.title}' successfully borrowed by {self.borrower_name}"

    def return_book(self):
        """Return a borrowed book."""
        if self.is_available:
            return f"✗ Book '{self.title}' was not borrowed"
        borrower = self.borrower_name
        self.is_available = True
        self.borrower_name = None
        self.borrowed_date = None
        return f"✓ Book '{self.title}' successfully returned by {borrower}"

    def add_review(self, review, rating):
        """Add a review and recalculate the average rating."""
        if not isinstance(review, str) or not review.strip():
            return "Review text cannot be empty"
        if isinstance(rating, bool) or not isinstance(rating, (int, float)) or not 1 <= rating <= 5:
            return "Rating must be between 1 and 5"
        self.reviews.append({"text": review.strip(), "rating": float(rating)})
        self.rating = sum(item["rating"] for item in self.reviews) / len(self.reviews)
        return f"Review added. Current average rating: {self.rating:.1f}/5.0"

    def display_book_info(self):
        """Print book information, including borrowing status."""
        print("=" * 60)
        print("BOOK INFORMATION")
        print("=" * 60)
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Genre: {self.genre}")
        print(f"Pages: {self.pages}")
        print(f"Price: USD {self.price:.2f}")
        print(f"Rating: {self.rating:.1f}/5.0")
        print(f"Status: {'Available' if self.is_available else 'Borrowed'}")
        if not self.is_available:
            print(f"Borrowed by: {self.borrower_name}")
            print(f"Borrowed on: {self.borrowed_date}")

    def display_reviews(self):
        """Print book reviews and ratings."""
        print("\nREVIEWS:")
        print("-" * 30)
        if not self.reviews:
            print("No reviews available")
        else:
            for index, review in enumerate(self.reviews, 1):
                print(f"{index}. Rating: {review['rating']:.1f}/5 - {review['text']}")


def demo_library():
    """Run constructor, review, and circulation demonstrations."""
    books = [
        Book("Python Crash Course", "Eric Matthes", "978-1593279288", 2019, "Programming", 544, 39.99),
        Book("Clean Code", "Robert Martin", "978-0132350884", 2008, "Programming", 464, 49.99),
        Book("The Pragmatic Programmer", "David Thomas", "978-0135957059", 2019, "Programming", 352, 45.00),
        Book("The Great Novel", "Author Name", "978-1122334455", 2021, "Fiction"),
    ]
    books[0].add_review("Excellent book for beginners!", 5)
    books[0].add_review("Very comprehensive and easy to follow", 4)
    books[0].add_review("Great examples and exercises", 5)
    books[1].add_review("Must-read for every programmer", 5)
    books[1].add_review("Changed how I write code", 4)
    books[2].add_review("Timeless programming wisdom", 5)
    for book in books:
        book.display_book_info()
        book.display_reviews()
        print("\n" + "=" * 60 + "\n")
    print(books[0].borrow_book("Alice Johnson"))
    print(books[0].borrow_book("Bob Smith"))
    print(books[0].return_book())


if __name__ == "__main__":
    demo_library()
