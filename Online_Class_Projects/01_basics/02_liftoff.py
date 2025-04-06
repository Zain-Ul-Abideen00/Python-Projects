# Problem Statement:
# Write a program that prints out a countdown from 10 to 1 and then outputs "Liftoff!"

import time

def main() -> None:
    print("Starting countdown sequence...")
    time.sleep(1)  # Pause for 1 second before starting

    # Count down from 10 to 1
    for i in range(10, 0, -1):
        print(f"{i}...")
        time.sleep(1)  # Pause for 1 second between numbers

    # Print Liftoff with some excitement!
    print("\nLIFTOFF! 🚀")
    print("We have liftoff! The spacecraft is now on its way to the stars!")

if __name__ == '__main__':
    main()
