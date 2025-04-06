# Problem Statement:
# Create a number guessing game where the computer picks a random number
# between 0 and 99, and the user tries to guess it with hints.

import random

def main():
    # Generate a random number between 0 and 99
    secret_number = random.randint(0, 99)

    print("I am thinking of a number between 0 and 99...")

    while True:
        # Get user's guess
        guess = int(input("Enter a guess: "))

        # Check if guess is correct
        if guess == secret_number:
            print(f"Congrats! The number was: {secret_number}")
            break
        elif guess > secret_number:
            print("Your guess is too high")
        else:
            print("Your guess is too low")

if __name__ == '__main__':
    main()
