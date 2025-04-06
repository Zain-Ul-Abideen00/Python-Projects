"""
## Problem Statement

Write a program which continuously asks the user to enter values which are added
one by one into a list. When the user presses enter without typing anything,
print the list.

Sample run:
Enter a value: 1
Enter a value: 2
Enter a value: 3
Enter a value:
Here's the list: ['1', '2', '3']
"""

def main():
    # Create an empty list to store values
    values = []

    # Keep asking for values until user enters empty string
    while True:
        value = input("Enter a value: ")
        if value == "":
            break
        values.append(value)

    # Print the final list
    print("Here's the list:", values)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
