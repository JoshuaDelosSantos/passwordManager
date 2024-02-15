"""
A simple Python password manager program.
"""

import user
import user_collection
import string
import random
import bcrypt

MENU = "(R)egister\n(L)ogin\n(Q)uit"


def main():
    """Run the main program simulating a user authentication environment and a password."""

    users = user_collection.UserCollection
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "R":
            handle_register()
        elif choice == "L":
            handle_login()
        else:
            print("Invalid input. Try again.")
        choice = input(">>>").upper()


def handle_register():
    """Register a new user and their password"""
    pass


def handle_login():
    """Log user into the system."""
    pass


def get_password():
    """Get a password from the user."""
    pass


def generate_random_password():
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
        random.sample(uppercase_char + lowercase_char + digit_char + symbol_char + remaining_chars, password_length))

    return final_password


def hash_password(password):
    """Hash a password."""
    # Generate a random salt
    salt = bcrypt.gensalt()

    # Combine the password with the salt and hash
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password, salt


if __name__ == '__main__':
    main()
