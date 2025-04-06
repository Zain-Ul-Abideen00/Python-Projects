"""
## Problem Statement
Ask the user for two numbers, one at a time, and then print the result of
dividing the first number by the second and also the remainder of the division.
"""

def main():
    # Get the two numbers from user
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))

    # Calculate quotient and remainder
    quotient = dividend // divisor
    remainder = dividend % divisor

    # Print result
    print(f"The result of this division is {quotient} with a remainder of {remainder}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
