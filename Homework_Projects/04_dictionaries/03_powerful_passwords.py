"""
## Problem Statement

You want to be safe online and use different passwords for different websites.
However, you are forgetful at times and want to make a program that can match
which password belongs to which website without storing the actual password!

This can be done via something called hashing. Hashing is when we take something
and convert it into a different, unique identifier. This is done using a hash
function.
"""

import hashlib

def hash_password(password):
    """
    Takes a password string and returns its SHA256 hash.
    """
    # Convert the password to bytes and hash it
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    """
    Check if the provided password matches the stored hash for the email.

    Args:
        email: The email to check
        password_to_check: The password to verify
        stored_logins: Dictionary of email -> hashed_password pairs

    Returns:
        True if login successful, False otherwise
    """
    # If email doesn't exist in stored_logins, return False
    if email not in stored_logins:
        return False

    # Hash the provided password
    hashed_password = hash_password(password_to_check)

    # Compare the hashed password with stored hash
    return stored_logins[email] == hashed_password

def main():
    # Example stored logins (email -> hashed_password)
    stored_logins = {
        "alice@email.com": hash_password("alice123"),
        "bob@email.com": hash_password("bob456"),
        "charlie@email.com": hash_password("charlie789")
    }

    # Test the login function
    print("Testing logins:")

    # Should succeed
    print("\nTesting valid credentials:")
    print("alice@email.com with correct password:",
          login("alice@email.com", "alice123", stored_logins))

    # Should fail - wrong password
    print("\nTesting invalid password:")
    print("alice@email.com with wrong password:",
          login("alice@email.com", "wrong_password", stored_logins))

    # Should fail - email doesn't exist
    print("\nTesting non-existent email:")
    print("nonexistent@email.com:",
          login("nonexistent@email.com", "any_password", stored_logins))


if __name__ == '__main__':
    main()
