"""
## Problem Statement

In this program we show an example of using dictionaries to keep track of
information in a phonebook.
"""

def main():
    # Create an empty phonebook dictionary
    phonebook = {}

    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Look up Contact")
        print("3. Display All Contacts")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            phonebook[name] = number
            print(f"Added {name} to phonebook.")

        elif choice == "2":
            name = input("Enter name to look up: ")
            if name in phonebook:
                print(f"{name}'s number is {phonebook[name]}")
            else:
                print(f"No contact found for {name}")

        elif choice == "3":
            if phonebook:
                print("\nAll Contacts:")
                for name, number in phonebook.items():
                    print(f"{name}: {number}")
            else:
                print("Phonebook is empty!")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
