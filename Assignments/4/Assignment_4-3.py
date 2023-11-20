import math


def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.

    Args:
    celsius (float): Temperature in Celsius.

    Returns:
    float: Temperature converted to Fahrenheit.
    """
    return (celsius * 9/5) + 32


def calculate_temperatures_and_sines():
    """
    Calculate Fahrenheit temperatures and sine values for a list of Celsius temperatures.

    This function:
    - Declares a list of Celsius temperatures.
    - Converts those temperatures to Fahrenheit and prints them.
    - Calculates the sine values of the Celsius temperatures and prints them.
    - Filters and prints only the non-negative sine values.

    Returns:
    None
    """

    # Declare a list of ten numbers representing Celsius temperatures.
    celsiusTemperatures = [-40, -30, -20, -10, 0, 10, 20, 30, 40, 50]

    # Use the map method to convert the Celsius temperatures to Fahrenheit.
    fahrenheitTemperatures = list(
        map(celsius_to_fahrenheit, celsiusTemperatures))
    print("Temperatures in Fahrenheit:", fahrenheitTemperatures)

    # Calculate and print the sine values of the Celsius temperatures.
    # The sine values are rounded to 1 decimal place for clarity.
    sineValues = list(
        map(lambda x: round(math.sin(math.radians(x)), 1), celsiusTemperatures))
    print("\nValues:", sineValues)

    # Filter and print only the non-negative sine values.
    nonNegativeSines = list(filter(lambda x: x >= 0, sineValues))
    print("\nNon-negative Values:", nonNegativeSines)


def main():
    """
    Main function that drives the script.

    Calls the calculate_temperatures_and_sines function to demonstrate various operations on a list of temperatures.

    Returns:
    None
    """
    calculate_temperatures_and_sines()


# Entry point of the script.
if __name__ == "__main__":
    main()