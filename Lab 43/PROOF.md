# Lab 43 - Magic Methods Execution Proof

## Run command

```bash
python3 lab_43.py
```

## What the terminal run demonstrates

The supplied terminal output shows the lab completed successfully and prints: **"All magic methods are working as expected."**

### Magic methods tested
- `__str__` and `__repr__` produce readable object representations for `Person` and `Book`.
- `__add__` combines vectors, books, playlists, and bank-account balances.
- `__eq__`, `__lt__`, `__le__`, and `__gt__` implement equality and comparisons.
- `__len__` allows the Playlist object to work with `len()`.
- `__bool__` reports whether a bank account has a positive balance.

### Results visible in the terminal evidence
- Vector addition: `Vector(3, 4) + Vector(1, 2) = Vector(4, 6)`.
- Combined book: `'1984 & Animal Farm' by George Orwell & George Orwell`, total **440 pages**.
- Combined playlist: **5 songs**.
- Bank account: $1,000 + $500 creates a joint account with **$1,500.00**.
- Deposit and withdrawal examples return balances of **$1,200.00** and **$900.00**.
- Boolean checks return `True` for a funded account and `False` for an empty account.

## Evidence files

The original terminal screenshots are included in the Lab 42 and Lab 43 evidence ZIP shared in this conversation. They still need to be uploaded as binary image files to this repository before Markdown can embed them directly here.
