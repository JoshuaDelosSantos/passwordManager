"""
This program uses Kivy's built-in app framework to run a Kivy application simulating a user-password interface.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from user_collection import UserCollection
from user import User
import string
import random
import bcrypt


class UserApp(App):
    """User application is a Kivy app that simulates a user-password interface."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.user_collection = UserCollection()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "User interface by Joshua Delos Santos"
        self.root = Builder.load_file('app.kv')
        return self.root

    def generate_random_password(self):
        """Generate a random password."""
        # Define character sets
        uppercase_letters = string.ascii_uppercase
        lowercase_letters = string.ascii_lowercase
        digits = string.digits
        symbols = string.punctuation

        # Ensure at least one character from each set
        uppercase_char = random.choice(uppercase_letters)
        lowercase_char = random.choice(lowercase_letters)
        digit_char = random.choice(digits)
        symbol_char = random.choice(symbols)

        # Combine all character sets
        all_chars = uppercase_letters + lowercase_letters + digits + symbols

        # Set the password length in the range [8, 20]
        password_length = random.randint(8, 20)

        # Generate the remaining characters for the password
        remaining_chars = ''.join(random.choice(all_chars) for _ in range(password_length - 4))

        # Shuffle all characters to create the final password
        final_password = ''.join(
            random.sample(uppercase_char + lowercase_char + digit_char + symbol_char + remaining_chars,
                          password_length))

        return final_password


if __name__ == '__main__':
    UserApp().run()
