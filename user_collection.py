"""
UserCollection class that stores user data in a list.
"""

import csv
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

    def load_users(self, filename='users.csv'):
        """Load users from file."""
        with open(filename, 'r', encoding='utf-8') as in_file:
            reader = csv.reader(in_file)
            for row in reader:
                self.add_user(User(*row[:3]))

    def save_users(self, filename='users.csv'):
        """Save users to CSV file."""
        with open(filename, 'w', encoding='utf-8', newline='') as out_file:
            writer = csv.writer(out_file)
            for user in self.users:
                writer.writerow([user.user_name, user.salt, user.hash_code])
