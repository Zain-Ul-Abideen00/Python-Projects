import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter 'r' for Rock, 'p' for Paper, or 's' for Scissors")
    print("Enter 'q' to quit the game")

    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("\nYour choice: ").lower()

        if user_choice == 'q':
            print("\nFinal Score:")
            print(f"User: {user_score}")
            print(f"Computer: {computer_score}")
            if user_score > computer_score:
                print("You won the game!")
            elif computer_score > user_score:
                print("Computer won the game!")
            else:
                print("It's a tie!")
            break

        if user_choice not in choices:
            print("Invalid choice. Please enter 'r', 'p', or 's'.")
            continue

        computer_choice = random.choice(list(choices.keys()))

        print(f"\nYou chose: {choices[user_choice]}")
        print(f"Computer chose: {choices[computer_choice]}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'r' and computer_choice == 's') or \
             (user_choice == 'p' and computer_choice == 'r') or \
             (user_choice == 's' and computer_choice == 'p'):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"\nCurrent Score - User: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    rock_paper_scissors()
