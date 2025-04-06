"""
## Problem Statement
Write a program that asks the user for the lengths of the two perpendicular sides
of a right triangle and outputs the length of the third side (the hypotenuse)
using the Pythagorean theorem!

The Pythagorean theorem states that in a right triangle:
BC ** 2 = AB ** 2 + AC ** 2
"""

import math

def main():
    # Get the lengths of the two perpendicular sides
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse using the Pythagorean theorem
    bc = math.sqrt(ab ** 2 + ac ** 2)

    # Print the result
    print(f"The length of BC (the hypotenuse) is: {bc}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
