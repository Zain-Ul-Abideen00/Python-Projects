## Problem Statement
# Fill out the double(num) function to return the result of multiplying num by 2.

def double(num):
    """Return the input number multiplied by 2."""
    return num * 2

def main():
    # Get input from user
    num = float(input("Enter a number: "))

    # Calculate and display the doubled value
    result = double(num)
    print(f"Double that is {result}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
