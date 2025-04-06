"""
## Problem Statement

This program counts the number of times each number appears in a list.
It uses a dictionary to keep track of the information.

An example run of the program looks like this (user input is in blue):

Enter a number: 3
Enter a number: 4
Enter a number: 3
Enter a number: 6
Enter a number: 4
Enter a number: 3
Enter a number: 12
Enter a number:
3 appears 3 times.
4 appears 2 times.
6 appears 1 times.
12 appears 1 times.
"""

def main():
    # Dictionary to store number counts
    number_counts = {}

    while True:
        # Get input from user
        user_input = input("Enter a number: ")

        # If user enters empty string, break the loop
        if user_input == "":
            break

        # Convert input to integer
        number = int(user_input)

        # Update the count in dictionary
        if number in number_counts:
            number_counts[number] += 1
        else:
            number_counts[number] = 1

    # Print the results
    for number, count in number_counts.items():
        print(f"{number} appears {count} times.")


if __name__ == '__main__':
    main()
