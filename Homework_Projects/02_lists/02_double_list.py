"""
## Problem Statement

Write a program that doubles each element in a list of numbers. For example, if you start with this list:
numbers = [1, 2, 3, 4]
You should end with this list:
numbers = [2, 4, 6, 8]
"""

def double_list(numbers):
    """Takes a list of numbers and doubles each element"""
    for i in range(len(numbers)):
        numbers[i] *= 2
    return numbers

def main():
    # Example usage
    numbers = [1, 2, 3, 4]
    print("Original list:", numbers)
    doubled_numbers = double_list(numbers)
    print("Doubled list:", doubled_numbers)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
