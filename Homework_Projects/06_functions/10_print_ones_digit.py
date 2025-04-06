## Problem Statement
# Write a function called print_ones_digit, which takes as a parameter an integer
# num and prints its ones digit using the modulo operator (%).

def print_ones_digit(num):
    """Print the ones digit of the given number."""
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")

def main():
    # Get input from user
    num = int(input("Enter a number: "))

    # Print the ones digit
    print_ones_digit(num)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
