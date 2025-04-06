## Problem Statement
# Implement the helper function make_sentence(word, part_of_speech) which will
# take a string word and an integer part_of_speech as parameters and generate
# sentences based on the part of speech (0: noun, 1: verb, 2: adjective).

def make_sentence(word, part_of_speech):
    """Generate a sentence based on the word and its part of speech."""
    if part_of_speech == 0:  # noun
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:  # verb
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:  # adjective
        print(f"Looking out my window, the sky is big and {word}!")

def main():
    # Get input from user
    word = input("Please type a noun, verb, or adjective: ")
    print("Is this a noun, verb, or adjective?")
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))

    # Generate and print the sentence
    make_sentence(word, part_of_speech)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
