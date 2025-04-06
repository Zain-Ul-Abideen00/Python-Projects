"""
## Problem Statement

There's a small fruit shop nearby your house that you like to buy from.
Since you buy several fruit at a time, you want to keep track of how much
the fruit will cost before you go. Luckily you wrote down what fruits were
available and how much one of each fruit costs.

Write a program that loops through a dictionary of fruits, prompting the user
to see how many of each fruit they want to buy, and then prints out the total
combined cost of all of the fruits.
"""

def main():
    # Dictionary of fruits and their prices
    fruit_prices = {
        "apple": 0.5,      # $0.50 each
        "durian": 25.0,    # $25.00 each
        "jackfruit": 15.0, # $15.00 each
        "kiwi": 1.0,       # $1.00 each
        "rambutan": 2.5,   # $2.50 each
        "mango": 3.0       # $3.00 each
    }

    total_cost = 0

    # Ask for quantity of each fruit
    for fruit, price in fruit_prices.items():
        while True:
            try:
                quantity = int(input(f"\nHow many ({fruit}) do you want?: "))
                if quantity >= 0:
                    break
                print("Please enter a non-negative number.")
            except ValueError:
                print("Please enter a valid number.")

        # Add cost of this fruit to total
        total_cost += price * quantity

    # Print total cost
    print(f"\nYour total is ${total_cost:.2f}")


if __name__ == '__main__':
    main()
