"""
## Problem Statement
Simulate rolling two dice, and prints results of each roll as well as the total.
"""

import random

def main():
    # Roll two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    # Calculate total
    total = die1 + die2

    # Print results
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {total}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
