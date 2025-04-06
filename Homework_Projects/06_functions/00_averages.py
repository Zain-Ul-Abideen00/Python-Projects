## Problem Statement
# Write a function that takes two numbers and finds the average between the two.

def calculate_average(num1, num2):
    """Calculate the average of two numbers."""
    return (num1 + num2) / 2

def main():
    # Get input from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Calculate and display the average
    average = calculate_average(num1, num2)
    print(f"The average of {num1} and {num2} is: {average}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
