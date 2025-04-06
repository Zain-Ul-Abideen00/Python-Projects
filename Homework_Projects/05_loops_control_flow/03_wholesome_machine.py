"""
## Problem Statement

Write a program which prompts the user to type an affirmation of your choice
(we'll use "I am capable of doing anything I put my mind to.") until they type
it correctly. Sometimes, especially in the midst of such uncertain times, we just
need to be reminded that we are resilient, capable, and strong; this little Python
program may be able to help!
"""

def main():
    # The affirmation to be typed
    affirmation = "I am capable of doing anything I put my mind to."

    print(f"Please type the following affirmation: {affirmation}")

    # Keep asking until they type it correctly
    while True:
        user_input = input()
        if user_input == affirmation:
            print("That's right! :)")
            break
        else:
            print("That was not the affirmation.")
            print(f"Please type the following affirmation: {affirmation}")


if __name__ == '__main__':
    main()
