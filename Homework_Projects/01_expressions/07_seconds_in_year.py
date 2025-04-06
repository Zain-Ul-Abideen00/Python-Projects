"""
## Problem Statement
Use Python to calculate the number of seconds in a year, and tell the user what
the result is in a nice print statement.
"""

def main():
    # Constants
    DAYS_IN_YEAR = 365
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60
    SECONDS_IN_MINUTE = 60

    # Calculate seconds in a year
    seconds = DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE

    # Print result
    print(f"There are {seconds} seconds in a year!")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
