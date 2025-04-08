def mad_libs():
    print("Welcome to Mad Libs!")
    print("Please enter the following words when prompted:")

    # Get user input
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    adverb1 = input("Enter an adverb: ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter another noun: ")
    adjective3 = input("Enter another adjective: ")
    verb2 = input("Enter another verb: ")
    adverb2 = input("Enter another adverb: ")
    verb3 = input("Enter another verb: ")
    adjective4 = input("Enter another adjective: ")

    # Create the story
    story = f"""
    Today I went to the zoo. I saw a(n) {adjective1} {noun1} jumping up and down in its tree.
    He {verb1} {adverb1} through the large tunnel that led to its {adjective2} {noun2}.
    I got some peanuts and passed them through the cage to a gigantic gray {noun3}
    towering above my head. Feeding that animal made me hungry. I went to get a {adjective3}
    scoop of ice cream. It filled my stomach. Afterwards I had to {verb2} {adverb2} to catch our bus.
    When I got home I {verb3} my mom for a {adjective4} day at the zoo.
    """

    print("\nHere's your story:")
    print(story)

if __name__ == "__main__":
    mad_libs()
