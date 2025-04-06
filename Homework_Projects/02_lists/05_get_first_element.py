"""
## Problem Statement

Fill out the function get_first_element(lst) which takes in a list lst as a parameter
and prints the first element in the list. The list is guaranteed to be non-empty.
"""

def get_first_element(lst):
    """Print the first element of the given list"""
    print(lst[0])

def main():
    # Create a list to store user input
    user_list = []

    # Get list elements from user
    while True:
        value = input("Enter a value (or press enter to finish): ")
        if value == "":
            break
        user_list.append(value)

    if user_list:  # Check if list is not empty
        print("\nFirst element is:", end=" ")
        get_first_element(user_list)
    else:
        print("No elements were entered.")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
