"""
## Problem Statement

There are times where you are working with lots of different data within a function that you
want to return. While generally, we want to keep functions to have a precise purpose, sometimes
that purpose just deals with multiple bits of data.

To practice this, imagine we are working on a program where the user needs to enters data to
sign up for a website. Fill out the get_user_data() function which:

1. Asks the user for their first name and stores it in a variable
2. Asks the user for their last name and stores it in a variable
3. Asks the user for their email address and stores it in a variable
4. Returns all three of these pieces of data in the order it was asked
"""

def get_user_data():
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")
    return first_name, last_name, email

def main():
    user_data = get_user_data()
    print(f"\nReceived the following user data: {user_data}")

if __name__ == '__main__':
    main()
