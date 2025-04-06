## Problem Statement
# Fill out print_multiple(message, repeats), which takes as parameters a string
# message to print, and an integer repeats number of times to print message.

def print_multiple(message, repeats):
    """Print the given message the specified number of times."""
    for _ in range(repeats):
        print(message)

def main():
    # Get input from user
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))

    # Print the message multiple times
    print_multiple(message, repeats)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
