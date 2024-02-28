"""
A simple Python password manager program.
"""

from user import User
from user_collection import UserCollection
import string
import random
import bcrypt
import getpass

MENU = "(R)egister\n(L)ogin\n(Q)uit"
USERS = UserCollection()
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Run the main program simulating a user authentication environment and a password."""

    print("Welcome")
    print(MENU)
    USERS.load_users()
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "R":
            handle_register()
        elif choice == "L":
            handle_login()
        else:
            print("Invalid input. Try again.")
        print(MENU)
        choice = input(">>>").upper()

    print("Fin.")


def handle_register():
    """Register a new user and their password"""

    menu = "(G)enerate random password\n(U)se own"

    user_name = get_valid_user_name()
    print(menu)
    choice = input(">>>").upper()
    if choice == "G":
        password = generate_random_password()
        hashed_password, salt = hash_password(password)
    else:
        password = getpass.getpass("Enter password: ")
        while not is_valid_password(password):
            print("Invalid password!")
            password = input("Password > ")
        hashed_password, salt = hash_password(password)

    USERS.add_user(User(user_name, salt, hashed_password))


def get_valid_user_name():
    """Get a non-empty user_name."""
    is_valid_user_name = False

    while not is_valid_user_name:
        user_name = input("User name > ")
        if user_name == "":
            print("Invalid input. Try again.")
        elif user_name in [user.user_name for user in USERS.users]:
            print("User name already taken. Try again.")
        else:
            is_valid_user_name = True

        return user_name


def handle_login():
    """Log user into the system."""
    user_name = input("Enter user name: ")

    # Check if the entered username exists in the user collection
    if user_name not in [user.user_name for user in USERS.users]:
        print("User name not found")
    else:
        password = getpass.getpass("Enter password: ")
        hashed_password, salt = hash_password(password)

        # Find the user with the entered username
        user = next(user for user in USERS.users if user.user_name == user_name)

        # Check if the entered password matches the stored hashed password
        if check_password(password, user.hash_code, user.salt):
            print("Login successful!")
        else:
            print("Incorrect password")


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


def check_password(entered_password, stored_hashed_password, salt):
    """Check if the entered password is correct."""
    # Hash the entered password with the stored salt
    hashed_entered_password = bcrypt.hashpw(entered_password.encode('utf-8'), salt)

    # Compare the stored hashed password with the newly hashed entered password
    return hashed_entered_password == stored_hashed_password


def run_tests():
    """Test codes."""
    # print("TEST Random generated password")
    # p1 = generate_random_password()
    # print(p1)
    #
    # print("TEST hashing a password")
    # p2, salt = hash_password(p1)
    # print(f"Hashed password: {p2}\nSalt: {salt}")

    # print("Print users")
    # USERS.add_user(User('Hello', 1, 2))
    # print(USERS)

    # Test for password
    # p3 = input("> ")
    # while not is_valid_password(p3):
    #     print("Invalid password!")
    #     p3 = input("> ")
    # print(p3)

    # Test for username
    # name = get_valid_user_name()

    # Test for loading users
    # USERS.load_users()
    # print(USERS)

    # Test for hashing password
    # hp, salt = hash_password('Bob')
    # USERS.add_user(User('Sponge', salt, hp))
    #
    # USERS.save_users()

    # Test for acquiring user-names
    # user_names = [user.user_name for user in USERS.users]
    # print(user_names)

    # Test for comparing hashed passwords
    # p1, salt1 = hash_password("Bob")
    # print(salt1)
    # salt1.encode('utf-8')
    # print(salt1)
    # print(p1)
    # p2, salt2 = hash_password("Bob")
    # print(p2)
    # if p1 == p2:
    #     print("Yes")


# run_tests()

if __name__ == '__main__':
    main()
