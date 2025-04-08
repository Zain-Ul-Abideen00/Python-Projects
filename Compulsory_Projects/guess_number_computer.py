import random

def computer_guess():
    print("Think of a number between 1 and 100, and I'll try to guess it!")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0

    while True:
        guess = random.randint(low, high)
        attempts += 1

        print(f"\nIs your number {guess}?")
        response = input("Enter 'h' if your number is higher, 'l' if lower, or 'c' if correct: ").lower()

        if response == 'c':
            print(f"\nYay! I guessed your number in {attempts} attempts!")
            break
        elif response == 'h':
            low = guess + 1
        elif response == 'l':
            high = guess - 1
        else:
            print("Please enter 'h', 'l', or 'c'.")
            continue

        if low > high:
            print("\nHmm, it seems like you might have changed your number!")
            break

if __name__ == "__main__":
    computer_guess()
