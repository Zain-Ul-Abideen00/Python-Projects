"""
High-Low Game

A number guessing game where the player competes against the computer.
The player needs to guess if their number is higher or lower than the computer's number.
Points are awarded for correct guesses, and the game continues for a set number of rounds.

Rules:
- Two random numbers (1-100) are generated for player and computer
- Player can see their number but not the computer's
- Player guesses if their number is higher or lower than computer's
- Points awarded for correct guesses
- Game continues for set number of rounds
- In case of equal numbers, computer wins
"""

import random

def get_valid_choice():
    """Get and validate user input for higher/lower choice."""
    while True:
        choice = input("Do you think your number is higher or lower than the computer's?: ").lower()
        if choice in ['higher', 'lower']:
            return choice
        print("Please enter either higher or lower: ", end='')

def check_win(player_num, computer_num, player_choice):
    """
    Check if the player won the round.
    Returns True if player won, False otherwise.
    """
    if player_num == computer_num:  # Computer wins on ties
        return False

    if player_choice == 'higher':
        return player_num > computer_num
    else:  # player_choice == 'lower'
        return player_num < computer_num

def get_ending_message(score, num_rounds):
    """Generate appropriate ending message based on score."""
    if score == num_rounds:
        return "Wow! You played perfectly!"
    elif score >= num_rounds // 2:
        return "Good job, you played really well!"
    else:
        return "Better luck next time!"

def play_game():
    NUM_ROUNDS = 5
    score = 0

    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")

        # Generate random numbers for player and computer
        player_num = random.randint(1, 100)
        computer_num = random.randint(1, 100)

        print(f"Your number is {player_num}")

        # Get player's guess
        player_choice = get_valid_choice()

        # Check if player won and update score
        if check_win(player_num, computer_num, player_choice):
            print(f"You were right! The computer's number was {computer_num}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")

        print(f"Your score is now {score}")

        # Add blank line between rounds
        if round_num < NUM_ROUNDS:
            print()

    # Print ending message
    print()
    print(get_ending_message(score, NUM_ROUNDS))

if __name__ == "__main__":
    play_game()
