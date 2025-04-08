import random
import string

def generate_password():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("\nEnter the length of the password (minimum 8): "))
            if length < 8:
                print("Password length must be at least 8 characters.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = lowercase + uppercase + digits + symbols

    # Ensure at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password
    password.extend(random.choice(all_characters) for _ in range(length - 4))

    # Shuffle the password
    random.shuffle(password)

    # Convert list to string
    password = ''.join(password)

    print(f"\nYour generated password is: {password}")
    print("\nPassword strength:")
    if length < 12:
        print("Medium - Consider using a longer password for better security")
    else:
        print("Strong - Good password length and complexity")

if __name__ == "__main__":
    generate_password()
