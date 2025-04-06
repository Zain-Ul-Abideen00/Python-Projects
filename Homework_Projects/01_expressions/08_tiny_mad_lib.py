"""
## Problem Statement
Write a program which prompts the user for an adjective, then a noun, then a verb,
and then prints a fun sentence with those words!

Mad Libs is a word game where players are prompted for one word at a time, and
the words are eventually filled into the blanks of a word template to make an
entertaining story!
"""

def main():
    # Constants
    SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

    # Get words from user
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    # Create and print the mad lib
    mad_lib = f"{SENTENCE_START} {adjective} {noun} {verb}!"
    print(mad_lib)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
