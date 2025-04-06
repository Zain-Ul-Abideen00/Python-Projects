"""
## Problem Statement

In the information flow lesson, we discussed using a variable storing a number as an example of scope.
We saw that changes we made to the number inside a function did not stay unless we returned it.
This is true for what we call immutable data types which include things like numbers and strings.

However, there are also mutable data types where changes stay even if we don't return anything.
Some examples of mutable data types are lists and dictionaries.
"""

def add_three_copies(lst, data):
    """Adds three copies of data to the list without returning anything"""
    for _ in range(3):
        lst.append(data)

def main():
    # Get input from user
    message = input("Enter a message to copy: ")

    # Create empty list and show it
    my_list = []
    print("\nList before:", my_list)

    # Add three copies of the message
    add_three_copies(my_list, message)

    # Show the modified list
    print("\nList after:", my_list)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
