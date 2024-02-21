"""
A simple Python password manager program.
"""

from user import User
from user_collection import UserCollection
import string
import random
import bcrypt

MENU = "(R)egister\n(L)ogin\n(Q)uit"
USERS = UserCollection()
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Run the main program simulating a user authentication environment and a password."""

    print("Welcome to the password manager program")
    print(MENU)
    choice = input(">>>")
    while choice.upper() != "Q":
        if choice == "R":
            handle_register()
        elif choice == "L":
            handle_login()
        else:
            print("Invalid input. Try again.")
        choice = input(">>>")

    print("Fin.")


def handle_register():
    """Register a new user and their password"""
    menu = "(G)enerate random password\n(U)se own"
    user_name = get_valid_user_name()
    print(menu)
    choice = input(">>>")
    if choice == "G":
        password = generate_random_password()
        hashed_password, salt = hash_password(password)
    else:
        password = input("> ")
        while not is_valid_password(password):
            print("Invalid password!")
            password = input("> ")
        hashed_password, salt = hash_password(password)
    USERS.add_user(User(user_name, salt, hashed_password))


def get_valid_user_name():
    """Get a non-empty user_name."""
    is_valid_user_name = False

    while not is_valid_user_name:
        user_name = input("Enter a user name: ")
        if user_name == "":
            print("Invalid input. Try again.")
        elif user_name in [user.user_name for user in USERS.users]:
            print("User name already taken. Try again.")
        else:
            is_valid_user_name = True
        user_name = input("Enter a user name: ")
        return user_name


def handle_login():
    """Log user into the system."""
    pass


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < 8:
        print("Password must be at least 8 characters long")
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1

    if count_lower == 0:
        print("Must have lowercase")
        return False
    if count_upper == 0:
        print("Must have uppercase")
        return False
    if count_digit == 0:
        print("Must have digits")
        return False
    if count_special == 0:
        print("Must have special characters")
        return False
    else:
        return True


def generate_random_password():
    """Generate a random password."""
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits

    # Ensure at least one character from each set
    uppercase_char = random.choice(uppercase_letters)
    lowercase_char = random.choice(lowercase_letters)
    digit_char = random.choice(digits)
    symbol_char = random.choice(SPECIAL_CHARACTERS)

    # Combine all character sets
    all_chars = uppercase_letters + lowercase_letters + digits + SPECIAL_CHARACTERS

    # Set the password length in the range [8, 20]
    password_length = random.randint(8, 20)

    # Generate the remaining characters for the password
    remaining_chars = ''.join(random.choice(all_chars) for i in range(password_length - 4))

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


def run_tests():
    print("TEST Random generated password")
    p1 = generate_random_password()
    print(p1)

    print("TEST hasing a password")
    p2, salt = hash_password(p1)
    print(f"Hashed password: {p2}\nSalt: {salt}")

    print("Print users")
    USERS.add_user(User('Hello', 1, 2))
    print(USERS)

    # Test for password
    # p3 = input("> ")
    # while not is_valid_password(p3):
    #     print("Invalid password!")
    #     p3 = input("> ")
    # print(p3)

    # Test for username
    name = get_valid_user_name()


run_tests()

# if __name__ == '__main__':
#     main()
