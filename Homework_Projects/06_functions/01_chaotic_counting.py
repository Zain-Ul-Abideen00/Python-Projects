## Problem Statement
# Fill out the chaotic_counting() function, which prints the numbers from 1 to 10,
# but with a catch. We've written a done() function which returns True with likelihood
# DONE_LIKELIHOOD -- at each number, before printing the number, you should call done()
# and check if it returns True or not. If done() returns True, we're done counting.

import random

DONE_LIKELIHOOD = 0.3

def done():
    """Returns True with likelihood DONE_LIKELIHOOD."""
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    """Count from 1 to 10 unless done() returns True."""
    for i in range(1, 11):
        if done():
            return
        print(i)

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done.")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
