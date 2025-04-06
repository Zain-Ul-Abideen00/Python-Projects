# Square Number Calculator
# This program calculates the square of a number

def main():
    # Get number from user
    number = float(input("Type a number to see its square: "))

    # Calculate square
    square = number * number

    # Display result
    print(f"{number} squared is {square}")

if __name__ == '__main__':
    main()
