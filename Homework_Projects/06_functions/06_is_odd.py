## Problem Statement
# Write a function that determines if a number is odd or even and prints the result.

def is_odd(num):
    """Return True if number is odd, False if even."""
    return num % 2 == 1

def main():
    # Print numbers from 10 to 19 with odd/even status
    for num in range(10, 20):
        status = "odd" if is_odd(num) else "even"
        print(f"{num} {status}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
