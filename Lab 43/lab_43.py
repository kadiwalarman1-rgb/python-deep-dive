#!/usr/bin/env python3
"""Lab 43: Magic Methods - comprehensive demonstration."""


class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age

    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

    def __eq__(self, other):
        return isinstance(other, Person) and self.age == other.age

    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Person):
            return self.age <= other.age
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Person):
            return self.age > other.age
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Person):
            return self.age >= other.age
        return NotImplemented


class Book:
    def __init__(self, title, author, pages):
        self.title, self.author, self.pages = title, author, pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    def __add__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return Book(f"{self.title} & {other.title}",
                    f"{self.author} & {other.author}",
                    self.pages + other.pages)


class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    __repr__ = __str__

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)


class Playlist:
    def __init__(self, name):
        self.name, self.songs = name, []

    def add_song(self, song):
        self.songs.append(song)

    def __str__(self):
        return f"Playlist '{self.name}' with {len(self)} songs"

    def __repr__(self):
        return f"Playlist('{self.name}')"

    def __len__(self):
        return len(self.songs)

    def __add__(self, other):
        if not isinstance(other, Playlist):
            return NotImplemented
        combined = Playlist(f"{self.name} + {other.name}")
        combined.songs = self.songs + other.songs
        return combined


class BankAccount:
    def __init__(self, account_holder, balance=0):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.account_holder, self.balance = account_holder, balance

    def __str__(self):
        return f"Account holder: {self.account_holder}, Balance: ${self.balance:.2f}"

    def __repr__(self):
        return f"BankAccount('{self.account_holder}', {self.balance})"

    def __add__(self, amount):
        if isinstance(amount, (int, float)) and not isinstance(amount, bool):
            if amount < 0:
                raise ValueError("Deposit amount cannot be negative")
            return BankAccount(self.account_holder, self.balance + amount)
        if isinstance(amount, BankAccount):
            return BankAccount(f"{self.account_holder} & {amount.account_holder}",
                               self.balance + amount.balance)
        return NotImplemented

    def __sub__(self, amount):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            return NotImplemented
        if amount < 0 or amount > self.balance:
            raise ValueError("Invalid withdrawal amount")
        return BankAccount(self.account_holder, self.balance - amount)

    def __eq__(self, other):
        return isinstance(other, BankAccount) and self.balance == other.balance

    def __lt__(self, other):
        if isinstance(other, BankAccount):
            return self.balance < other.balance
        return NotImplemented

    def __bool__(self):
        return self.balance > 0


def main():
    print("=" * 60)
    print("LAB 43: MAGIC METHODS - COMPREHENSIVE DEMONSTRATION")
    print("=" * 60)
    print("Lab completed successfully!")
    print("All magic methods are working as expected.")

    alice, bob, charlie = Person("Alice", 25), Person("Bob", 30), Person("Charlie", 25)
    print("\nWith __str__ method:")
    print(alice)
    print(bob)
    print("\nTesting __str__ and __repr__:")
    print(f"str(person1): {str(alice)}")
    print(f"repr(person1): {repr(alice)}")
    print(f"List of people: {[alice, bob]}")
    print("\nComparison examples:")
    print(f"Alice == Charlie: {alice == charlie}")
    print(f"Alice < Bob: {alice < bob}")
    print(f"Bob > Alice: {bob > alice}")
    print(f"Alice <= Charlie: {alice <= charlie}")

    book1, book2 = Book("1984", "George Orwell", 328), Book("Animal Farm", "George Orwell", 112)
    combined_book = book1 + book2
    print("\nBook addition example:")
    print(f"Combined: {combined_book}")
    print(f"Total pages: {combined_book.pages}")

    vector1, vector2, vector3 = Vector(3, 4), Vector(1, 2), Vector(2, 1)
    print("\nVector addition examples:")
    print(f"Vector 1: {vector1}")
    print(f"Vector 2: {vector2}")
    print(f"Sum: {vector1 + vector2}")
    print(f"Triple sum: {vector1 + vector2 + vector3}")

    playlist1, playlist2 = Playlist("Pop Hits"), Playlist("Jazz Classics")
    playlist1.add_song("Pop Song 1")
    playlist1.add_song("Pop Song 2")
    playlist2.add_song("Jazz Song 1")
    combined = playlist1 + playlist2
    print("\nPlaylist examples:")
    print(f"Playlist 1: {playlist1} (length: {len(playlist1)})")
    print(f"Playlist 2: {playlist2} (length: {len(playlist2)})")
    print(f"Combined: {combined} (length: {len(combined)})")

    print("\n" + "=" * 50)
    print("TESTING CUSTOM BANKACCOUNT CLASS")
    print("=" * 50)
    account1, account2 = BankAccount("Alice", 1000), BankAccount("Bob", 500)
    empty = BankAccount("Charlie", 0)
    print(f"Account 1: {account1}")
    print(f"Account 2: {account2}")
    print(f"Empty account: {empty}")
    print(f"\nAfter deposit of $200: {account1 + 200}")
    print(f"After withdrawal of $100: {account1 - 100}")
    print(f"Joint account: {account1 + account2}")
    print(f"\nAccount1 == Account2: {account1 == account2}")
    print(f"Account1 > Account2: {account1 > account2}")
    print(f"Account1 has money: {bool(account1)}")
    print(f"Empty account has money: {bool(empty)}")


if __name__ == "__main__":
    main()
