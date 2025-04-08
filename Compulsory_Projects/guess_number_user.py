import random

def user_guess():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"\nCongratulations! You guessed the number in {attempts} attempts!")
                break

            print(f"You have {max_attempts - attempts} attempts remaining.")

        except ValueError:
            print("Please enter a valid number.")

    if attempts == max_attempts and guess != secret_number:
        print(f"\nGame Over! The number was {secret_number}.")

if __name__ == "__main__":
    user_guess()
