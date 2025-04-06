"""
## Problem Statement

Print 10 random numbers in the range 1 to 100.

Here is an example run:

45
79
61
47
52
10
16
83
19
12

Each time you run your program you should get different numbers.
"""

import random

def main():
    # Print 10 random numbers between 1 and 100
    for _ in range(10):
        number = random.randint(1, 100)
        print(number)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
