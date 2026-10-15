import re


def validate_email(email):
    if not isinstance(email, str):
        return False
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.fullmatch(pattern, email.strip()) is not None


def validate_password(password):
    if not isinstance(password, str) or len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit"
    return True, "Password is valid"


def validate_price(price):
    try:
        price_value = float(price)
    except (TypeError, ValueError):
        return False, "Price must be a valid number"
    if price_value <= 0:
        return False, "Price must be a positive number"
    return True, "Price is valid"
