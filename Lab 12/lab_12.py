class InvalidAgeError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

def parse_age(value):
    try:
        age = int(value)
    except (ValueError, TypeError) as error:
        raise InvalidAgeError("Age must be a whole number") from error
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120")
    return age

def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Withdrawal amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

def main():
    for value in ["25", "abc", "150"]:
        try:
            print("Age:", parse_age(value))
        except InvalidAgeError as error:
            print("Age error:", error)

    for amount in [20, 120, -5]:
        try:
            print("Balance after withdrawal:", withdraw(100, amount))
        except (InvalidAmountError, ValueError) as error:
            print("Withdrawal error:", error)

    resource_open = True
    try:
        print("Processing resource")
    finally:
        resource_open = False
        print("Cleanup completed:", not resource_open)

if __name__ == "__main__":
    main()
