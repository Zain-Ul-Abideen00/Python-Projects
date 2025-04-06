# Problem Statement:
# Write a program that asks a user to enter a number, then doubles that number
# and prints the result repeatedly until the value is 100 or greater.

def main():
    # Get initial number from user
    curr_value = int(input("Enter a number: "))

    # Keep doubling until we reach 100 or more
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

if __name__ == '__main__':
    main()
