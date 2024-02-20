"""
UserCollection class that stores user data in a list.
"""

import json
from user import User


class UserCollection:
    """Represents a collection of users."""

    FILENAME = "users_data.json"

    def __init__(self):
        """Initialises users."""
        self.users = []

    def __str__(self):
        """Return a string representation of the users."""
        return '\n'.join(str(user) for user in self.users)

    def add_user(self, user):
        """Adds a user to users."""
        self.users.append(user)

    def remove_user(self, user):
        """Removes a user from users."""
        self.users.remove(user)

    def load_songs(self, filename='songs.json'):
        """Load songs from JSON file."""
        with open(filename, 'r', encoding='utf-8') as in_file:
            data = json.load(in_file)

        for datum in data:
            self.add_user(User(**datum))

    def save_users(self, filename="users_data.json"):
        """Saves users to a file."""
        with open(filename, "w", encoding='utf-8') as out_file:
            print(json.dumps(self.users, default=vars), file=out_file)
