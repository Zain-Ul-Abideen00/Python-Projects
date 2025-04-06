"""
## Problem Statement
Simulate rolling two dice, three times.  Prints the results of each die roll.
This program is used to show how variable scope works.
"""

import random

def main():
    # Roll the dice three times
    for i in range(3):
        # Roll two dice
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        # Print the results
        print(f"Roll {i + 1}:")
        print(f"Die 1: {die1}")
        print(f"Die 2: {die2}")
        print()  # Empty line for better readability


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
