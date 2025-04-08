import random

def hangman():
    # List of words to choose from
    words = ['python', 'programming', 'computer', 'algorithm', 'database', 'function', 'variable', 'string', 'integer']

    # Select a random word
    word = random.choice(words)
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()

    # Game variables
    lives = 6

    # Game loop
    while len(word_letters) > 0 and lives > 0:
        # Show current state
        print(f"\nYou have {lives} lives left")
        print("Used letters:", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word:", ' '.join(word_list))

        # Get user input
        user_letter = input("Guess a letter: ").lower()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f"Letter {user_letter} is not in the word.")

        elif user_letter in used_letters:
            print("You've already used that letter. Try again.")

        else:
            print("Invalid character. Please try again.")

    # Game over
    if lives == 0:
        print(f"\nYou lost! The word was {word}")
    else:
        print(f"\nCongratulations! You guessed the word {word}!")

if __name__ == "__main__":
    hangman()
