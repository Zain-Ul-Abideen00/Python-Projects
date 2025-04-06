# Fahrenheit to Celsius Converter
# This program converts temperature from Fahrenheit to Celsius

def main():
    # Get temperature in Fahrenheit from user
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert to Celsius using the exact formula
    celsius = (fahrenheit - 32) * 5.0/9.0

    # Display result in the specified format
    print(f"Temperature: {fahrenheit}F = {celsius}C")

if __name__ == '__main__':
    main()
