from collections import Counter
import re
from datetime import datetime
import math

def demonstrate_format_method():
    name, age, city = "Alice", 25, "Ahmedabad"
    print("=== format() ===")
    print("Hello, my name is {} and I am {} years old.".format(name, age))
    print("I live in {2}; my name is {0}, age {1}.".format(name, age, city))
    print("Hello {person}, you are {years} and live in {place}.".format(person=name, years=age, place=city))
    price = 1234.56789
    print("Original: {}".format(price))
    print("Two decimals: {:.2f}".format(price))
    print("Thousands separator: {:,.2f}".format(price))
    print("Percentage: {:.1%}".format(0.85))
    for label, specification in (("Left", "<10"), ("Right", ">10"), ("Center", "^10"), ("Zero padded", "0>10")):
        print(f"{label}: '{format('Python', specification)}'")

def demonstrate_f_strings():
    name, age, salary = "Bob", 30, 75000.50
    now = datetime.now()
    total = 3 * 999.99
    invoice = f"""Invoice Details:
Product: Laptop
Quantity: 3
Unit price: {999.99:.2f} USD
Subtotal: {total:.2f} USD
Tax (8.5%): {total * 0.085:.2f} USD
Grand total: {total * 1.085:.2f} USD"""
    print("\n=== f-strings ===")
    print(f"Hello, I'm {name} and I'm {age} years old.")
    print(f"Annual salary: {salary:,.2f} USD; monthly: {salary / 12:,.2f} USD")
    print(f"Square root of 16: {math.sqrt(16)}")
    print(f"Date: {now:%Y-%m-%d}; time: {now:%H:%M:%S}")
    print(f"Scientific notation: {1234567.89:e}")
    print(invoice)

def demonstrate_slicing():
    text = "Python Programming Language"
    email = "user.name@example.com"
    phone = "+1-555-123-4567"
    print("\n=== Slicing ===")
    print("Original:", text)
    print("First six:", text[:6])
    print("Last eight:", text[-8:])
    print("Every second character:", text[::2])
    print("Reversed:", text[::-1])
    print("Email username:", email.split("@", 1)[0])
    print("Email domain:", email.split("@", 1)[1])
    print("Phone digits:", "".join(character for character in phone if character.isdigit()))

def demonstrate_character_frequency():
    text = "Python makes string processing practical!"
    frequencies = Counter(character.lower() for character in text if character.isalpha())
    print("\n=== Character frequency ===")
    for character, count in sorted(frequencies.items()):
        print(f"{character}: {count}")
    print("Most common:", frequencies.most_common(5))

def demonstrate_regular_expressions():
    text = "Contact alice@example.com or bob.smith@company.org. Call +1-555-123-4567."
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    phones = re.findall(r"\+?\d[\d -]{7,}\d", text)
    normalized = re.sub(r"\s+", " ", "  Python   uses   regular expressions.  ")
    masked = re.sub(r"(?<=.).(?=[^@]*?@)", "*", "alice@example.com")
    multiline = "First line\nSecond line\tTabbed"
    print("\n=== Regular expressions and escape sequences ===")
    print("Emails:", emails)
    print("Phone-like values:", phones)
    print("Normalized whitespace:", normalized.strip())
    print("Masked email example:", masked)
    print("Multiline text:", multiline)

def main():
    demonstrate_format_method()
    demonstrate_f_strings()
    demonstrate_slicing()
    demonstrate_character_frequency()
    demonstrate_regular_expressions()

if __name__ == "__main__":
    main()
