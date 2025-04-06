## Problem Statement
# Fill out the function count_even(lst) which first populates a list by prompting
# the user for integers until they press enter, and then prints the number of even
# numbers in the list.

def count_even(numbers):
    """Count the number of even numbers in the list."""
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

def get_numbers():
    """Get numbers from user until they press enter."""
    numbers = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid integer.")
    return numbers

def main():
    # Get list of numbers from user
    numbers = get_numbers()

    # Count and display even numbers
    even_count = count_even(numbers)
    print(f"Number of even numbers in the list: {even_count}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
