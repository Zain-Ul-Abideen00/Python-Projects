"""
## Problem Statement

Write a function that takes a list of numbers and returns the sum of those numbers.
"""

def add_numbers(numbers):
    """Takes a list of numbers and returns their sum"""
    return sum(numbers)

def main():
    # Example usage
    test_list = [1, 2, 3, 4, 5]
    result = add_numbers(test_list)
    print(f"The sum of {test_list} is: {result}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
