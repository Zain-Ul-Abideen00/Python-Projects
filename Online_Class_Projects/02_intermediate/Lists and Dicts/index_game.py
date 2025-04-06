"""
Index Game

A text-based game to practice list operations:
- Accessing elements by index
- Modifying elements at specific indices
- Slicing lists
- Handling out-of-range indices

The game allows users to:
1. Access elements at specific indices
2. Modify elements at specific indices
3. Get slices of the list
"""

def access_element(lst, index):
    """
    Access an element at the specified index.
    Returns the element if index is valid, error message otherwise.
    """
    try:
        return lst[index]
    except IndexError:
        return f"Error: Index {index} is out of range. List has {len(lst)} elements."

def modify_element(lst, index, new_value):
    """
    Modify an element at the specified index.
    Returns True if successful, False otherwise.
    """
    try:
        lst[index] = new_value
        return True
    except IndexError:
        return False

def slice_list(lst, start, end):
    """
    Return a slice of the list from start to end (exclusive).
    Handles out of range indices gracefully.
    """
    try:
        return lst[start:end]
    except IndexError:
        return []

def print_menu():
    """Print the game menu."""
    print("\nList Operations Menu:")
    print("1. Access an element")
    print("2. Modify an element")
    print("3. Slice the list")
    print("4. Quit")

def main():
    # Initialize the list with mixed elements
    my_list = [42, "hello", 3.14, True, "python", 100]

    while True:
        # Show current list state
        print(f"\nCurrent list: {my_list}")
        print(f"List indices: {list(range(len(my_list)))}")

        # Display menu and get user choice
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            # Access element
            index = int(input("Enter the index to access: "))
            result = access_element(my_list, index)
            print(f"Element at index {index}: {result}")

        elif choice == "2":
            # Modify element
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            # Try to convert to int or float if possible
            try:
                new_value = int(new_value)
            except ValueError:
                try:
                    new_value = float(new_value)
                except ValueError:
                    pass

            if modify_element(my_list, index, new_value):
                print(f"Successfully modified element at index {index}")
            else:
                print(f"Error: Index {index} is out of range")

        elif choice == "3":
            # Slice list
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(my_list, start, end)
            print(f"Slice from index {start} to {end}: {result}")

        elif choice == "4":
            # Quit the game
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    print("Welcome to the List Operations Game!")
    print("This game helps you practice working with Python lists.")
    main()
