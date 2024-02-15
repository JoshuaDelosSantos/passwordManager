"""
User class that initialises a user's username and password.
"""


class User:
    def __init__(self, user_name, salt, hash_code):
        """Initialise user instance."""
        self.user_name = user_name
        self.salt = salt
        self.hash_code = hash_code

    def __str__(self):
        """Return string representation of user_name and user password."""
        return f"{self.user_name},{self.salt},{self.hash_code}"
