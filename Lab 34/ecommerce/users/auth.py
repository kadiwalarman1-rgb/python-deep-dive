import hashlib
import hmac
import secrets

from ..utils.validators import validate_email


class User:
    iterations = 100_000

    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password_hash = None
        self.is_active = True

    def set_password(self, password):
        if not isinstance(password, str) or len(password) < 8:
            raise ValueError("Password must contain at least 8 characters")
        salt = secrets.token_hex(16)
        digest = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), salt.encode("utf-8"), self.iterations
        )
        self.password_hash = salt + digest.hex()

    def verify_password(self, password):
        if not self.password_hash or not isinstance(password, str):
            return False
        salt = self.password_hash[:32]
        stored_digest = self.password_hash[32:]
        candidate = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), salt.encode("utf-8"), self.iterations
        ).hex()
        return hmac.compare_digest(stored_digest, candidate)


class AuthManager:
    def __init__(self):
        self.users = {}
        self.active_sessions = {}

    def register_user(self, username, email, password):
        username = username.strip() if isinstance(username, str) else ""
        email = email.strip().lower() if isinstance(email, str) else ""
        if not username or not email:
            raise ValueError("Username and email are required")
        if username in self.users:
            raise ValueError("Username already exists")
        if any(user.email == email for user in self.users.values()):
            raise ValueError("Email already exists")
        if not validate_email(email):
            raise ValueError("Invalid email address")
        user = User(len(self.users) + 1, username, email)
        user.set_password(password)
        self.users[username] = user
        return user

    def authenticate(self, username, password):
        user = self.users.get(username)
        if user and user.is_active and user.verify_password(password):
            token = secrets.token_urlsafe(32)
            self.active_sessions[token] = user
            return token
        return None

    def get_user_by_token(self, token):
        return self.active_sessions.get(token)

    def logout(self, token):
        return self.active_sessions.pop(token, None) is not None
