"""
## Problem Statement
Write a program that continually reads in mass from the user and then outputs the
equivalent energy using Einstein's mass-energy equivalence formula (E stands for
energy, m stands for mass, and C is the speed of light:

E = m * c**2

Almost 100 years ago, Albert Einstein famously discovered that mass and energy are
interchangeable and are related by the above equation.
"""

def main():
    # Speed of light constant in m/s
    C = 299792458

    # Get mass from user
    mass = float(input("Enter kilos of mass: "))

    # Calculate energy using E = mc^2
    energy = mass * (C ** 2)

    # Print results
    print("\ne = m * C^2...")
    print(f"m = {mass} kg")
    print(f"C = {C} m/s")
    print(f"{energy} joules of energy!")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
