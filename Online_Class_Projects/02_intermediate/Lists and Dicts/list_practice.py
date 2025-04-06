"""
List Practice

This program demonstrates basic list operations in Python:
- Creating a list
- Getting list length
- Adding elements to a list
- Printing list contents
"""

def main():
    # Create a list called `fruit_list` that contains the following fruits:
    # 'apple', 'banana', 'orange', 'grape', 'pineapple'
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the length of the list
    print(f"The list contains {len(fruit_list)} fruits")

    # Add 'mango' at the end of the list
    fruit_list.append('mango')

    # Print the updated list
    print(f"Updated fruit list: {fruit_list}")

if __name__ == "__main__":
    main()
