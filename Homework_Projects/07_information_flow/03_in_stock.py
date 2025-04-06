"""
## Problem Statement

Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit
as a parameter and returns how many of that fruit are in her inventory. Write code in main()
which will:

1. Prompt the user to enter a fruit ("Enter a fruit: ")
2. Call num_in_stock(fruit) to get the number of that fruit that Sophia has in stock
3. Print the number which are in stock if Sophia has that fruit in her inventory
   (there are more than 0 in stock)
4. Print "This fruit is not in stock." if Sophia has none of that fruit in her inventory.
"""

def num_in_stock(fruit):
    # This is a simple inventory system
    inventory = {
        'apple': 500,
        'banana': 200,
        'orange': 300,
        'pear': 1000,
        'grape': 750
    }
    return inventory.get(fruit.lower(), 0)

def main():
    fruit = input("Enter a fruit: ")
    quantity = num_in_stock(fruit)

    if quantity > 0:
        print("\nThis fruit is in stock! Here is how many:\n")
        print(quantity)
    else:
        print("\nThis fruit is not in stock.")

if __name__ == '__main__':
    main()
