"""
## Problem Statement

Fill out the function shorten(lst) which removes elements from the end of lst,
which is a list, and prints each item it removes until lst is MAX_LENGTH items long.
If lst is already shorter than MAX_LENGTH you should leave it unchanged.
"""

MAX_LENGTH = 3

def shorten(lst):
    """Remove elements from the end of lst until it's MAX_LENGTH items long"""
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(f"Removing: {removed_item}")

def main():
    # Create a list to store user input
    user_list = []

    # Get list elements from user
    while True:
        value = input("Enter a value (or press enter to finish): ")
        if value == "":
            break
        user_list.append(value)

    print("\nOriginal list:", user_list)
    shorten(user_list)
    print("Shortened list:", user_list)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
