"""
## Problem Statement

Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have minimum height requirements for safety reasons. Assume for now that the minimum height is 50 of whatever height unit you'd like.
"""

def main():
    # Set minimum height requirement
    MIN_HEIGHT = 50

    # Get user's height
    height = float(input("How tall are you? "))

    # Check if they're tall enough
    if height >= MIN_HEIGHT:
        print("\nYou're tall enough to ride!")
    else:
        print("\nYou're not tall enough to ride, but maybe next year!")


def tall_enough_extension():
    """Extension: Repeatedly ask for heights until user enters nothing"""
    MIN_HEIGHT = 50

    while True:
        # Get user input
        height_str = input("How tall are you? ")

        # Check if user entered nothing
        if height_str == "":
            break

        # Convert to float and check height
        height = float(height_str)
        if height >= MIN_HEIGHT:
            print("\nYou're tall enough to ride!")
        else:
            print("\nYou're not tall enough to ride, but maybe next year!")
        print()  # Add blank line between entries


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
    # Uncomment the line below to run the extension version
    # tall_enough_extension()
