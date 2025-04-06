## Problem Statement
# Write the helper function print_divisors(num), which takes in a number and prints
# all of its divisors (numbers that divide evenly into the input number).

def print_divisors(num):
    """Print all divisors of the given number."""
    print(f"Here are the divisors of {num}")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

def main():
    # Get input from user
    num = int(input("Enter a number: "))

    # Print all divisors
    print_divisors(num)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
