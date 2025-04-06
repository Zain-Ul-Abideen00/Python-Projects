"""
## Problem Statement
Converts feet to inches. Feet is an American unit of measurement.
There are 12 inches per foot. Foot is the singular, and feet is the plural.
"""

def main():
    # Get feet from user
    feet = float(input("Enter number of feet: "))

    # Convert to inches (1 foot = 12 inches)
    inches = feet * 12

    # Handle singular/plural form
    foot_word = "foot" if feet == 1 else "feet"
    inch_word = "inch" if inches == 1 else "inches"

    # Print result
    print(f"{feet} {foot_word} equals {inches} {inch_word}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
