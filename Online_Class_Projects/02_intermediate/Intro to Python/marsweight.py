"""
Mars Weight Calculator

This program calculates how much a person would weigh on Mars based on their Earth weight.
Mars has weaker gravity than Earth - an Earthling's weight on Mars is 37.8% of their weight on Earth.

Sample runs:
Enter a weight on Earth: 120
The equivalent on Mars: 45.36

Enter a weight on Earth: 186
The equivalent on Mars: 70.31
"""

# Get the Earth weight from user
earth_weight = float(input("Enter a weight on Earth: "))

# Calculate Mars weight (37.8% of Earth weight)
mars_weight = earth_weight * 0.378

# Round to 2 decimal places and print result
mars_weight_rounded = round(mars_weight, 2)
print(f"\nThe equivalent on Mars: {mars_weight_rounded}")
