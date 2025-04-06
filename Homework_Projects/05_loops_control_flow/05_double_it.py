"""
## Problem Statement

Write a program that asks a user to enter a number. Your program will then double
that number and print out the result. It will repeat that process until the value
is 100 or greater.

For example if the user enters the number 2 you would then print:

4
8
16
32
64
128

Note that:
2 doubled is 4
4 doubled is 8
8 doubled is 16
and so on.

We stop at 128 because that value is greater than 100.
"""

def main():
    try:
        # Get the starting number from user
        curr_value = float(input("Enter a number: "))

        # Keep doubling until we reach or exceed 100
        while curr_value < 100:
            curr_value = curr_value * 2
            print(int(curr_value) if curr_value.is_integer() else curr_value)

    except ValueError:
        print("Please enter a valid number.")


if __name__ == '__main__':
    main()
