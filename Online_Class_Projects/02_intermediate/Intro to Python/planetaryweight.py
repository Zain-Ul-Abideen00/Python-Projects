"""
Planetary Weight Calculator

This program calculates how much a person would weigh on different planets based on their Earth weight.
Each planet has a different gravitational constant relative to Earth:
- Mercury: 37.6%
- Venus: 88.9%
- Mars: 37.8%
- Jupiter: 236.0%
- Saturn: 108.1%
- Uranus: 81.5%
- Neptune: 114.0%

Sample runs:
Enter a weight on Earth: 120
Enter a planet: Mars
The equivalent weight on Mars: 45.36

Enter a weight on Earth: 150
Enter a planet: Jupiter
The equivalent weight on Jupiter: 354.0
"""

# Dictionary of planetary gravity constants (percentage of Earth's gravity)
GRAVITY_CONSTANTS = {
    "mercury": 0.376,
    "venus": 0.889,
    "mars": 0.378,
    "jupiter": 2.36,
    "saturn": 1.081,
    "uranus": 0.815,
    "neptune": 1.14
}

# Get the Earth weight from user
earth_weight = float(input("Enter a weight on Earth: "))

# Get the target planet from user
planet = input("\nEnter a planet: ")

# Calculate weight on the selected planet
planet_weight = earth_weight * GRAVITY_CONSTANTS[planet.lower()]

# Round to 2 decimal places and print result
planet_weight_rounded = round(planet_weight, 2)
print(f"\nThe equivalent weight on {planet.capitalize()}: {planet_weight_rounded}")
