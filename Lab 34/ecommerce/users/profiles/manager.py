from datetime import datetime


class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = str(zip_code)
        self.country = country

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}, {self.country}"


class UserProfile:
    def __init__(self, user_id):
        self.user_id = user_id
        self.first_name = None
        self.last_name = None
        self.phone = None
        self.date_of_birth = None
        self.addresses = []
        self.preferences = {}
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def add_address(self, address):
        if not isinstance(address, Address):
            raise TypeError("address must be an Address instance")
        self.addresses.append(address)
        self.updated_at = datetime.now()

    def set_preference(self, key, value):
        self.preferences[key] = value
        self.updated_at = datetime.now()

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return None


class ProfileManager:
    def __init__(self):
        self.profiles = {}

    def create_profile(self, user_id):
        if user_id in self.profiles:
            raise ValueError(f"Profile for user {user_id} already exists")
        profile = UserProfile(user_id)
        self.profiles[user_id] = profile
        return profile

    def get_profile(self, user_id):
        return self.profiles.get(user_id)

    def update_profile(self, user_id, **kwargs):
        profile = self.profiles.get(user_id)
        if profile is None:
            return False
        permitted = {"first_name", "last_name", "phone", "date_of_birth"}
        for key, value in kwargs.items():
            if key in permitted:
                setattr(profile, key, value)
        profile.updated_at = datetime.now()
        return True
