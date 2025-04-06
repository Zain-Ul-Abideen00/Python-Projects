"""
## Problem Statement

Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main()
method to call the subtract_seven helper function! If you're stuck, revisit the add_five
example from lecture.
"""

def subtract_seven(num):
    """
    Helper function that subtracts 7 from the input number
    """
    return num - 7

def main():
    # Get a number from the user
    number = int(input("Enter a number: "))

    # Call the helper function and store the result
    result = subtract_seven(number)

    # Print the result
    print(f"{number} - 7 = {result}")

if __name__ == '__main__':
    main()
