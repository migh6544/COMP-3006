import unittest
import math
import random
from collections import deque, Counter


def simulate_die_rolls():
    """
    Simulate 100 rolls of a fair six-sided die.

    This function simulates rolling a fair six-sided die 100 times and then
    utilizes the Counter class from the collections module to determine the
    three most frequently rolled numbers. The results, along with the count
    of how many times each number appeared, are printed to the console.

    Returns:
    None
    """

    # Simulate 100 rolls of a six-sided die using a list comprehension.
    # For each iteration in the range of 100, a random number between 1 and 6 is generated.
    dieRolls = [random.randint(1, 6) for roll in range(100)]
    # Use the Counter class to count occurrences of each number in dieRolls.
    counter = Counter(dieRolls)
    # Retrieve the three most common numbers rolled.
    mostCommon = counter.most_common(3)
    # Iterate over the three most common numbers and print each one along with its count.
    for number, count in mostCommon:
        print(f"Number {number} appeared {count} times.")


def manipulate_deque():
    """
    Manipulate a deque data structure containing names of movie stars.

    This function:
    - Instantiates a deque with names of movie stars.
    - Inserts new names into the middle, front, and end of the deque.
    - Removes specific names from the original list.
    - Removes names from both the front and the rear of the deque.
    - Prints the deque's state after each major operation.

    Returns:
    None
    """

    # Instantiate a deque with five given names of movie stars.
    movieStars = deque(["Robert Lopez", "John Legend",
                       "Andrew Lloyd Webber", "Tim Rice", "Alan Menken"])
    print("Original deque:")
    print(movieStars)

    # Insert new names
    # Insert "Rita Moreno" in the middle of the deque. The middle position is determined using floor division.
    middleInsert = len(movieStars) // 2
    movieStars.insert(middleInsert, "Rita Moreno")
    # Insert "Whoopi Goldberg" at the front of the deque.
    movieStars.appendleft("Whoopi Goldberg")
    # Insert "Mel Brooks" at the rear of the deque.
    movieStars.append("Mel Brooks")
    print("\nAfter inserting names:")
    print(movieStars)
    # Remove two specific names: "Tim Rice" and "Alan Menken"
    movieStars.remove("Tim Rice")
    movieStars.remove("Alan Menken")
    print("\nAfter removing two names:")
    print(movieStars)
    # Remove the first name (front) and the last name (rear) from the deque.
    movieStars.popleft()
    movieStars.pop()
    print("\nAfter removing front and rear entries:")
    print(movieStars)


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


class TestFunctions(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)  # The unique value where Celsius and Fahrenheit are equal.
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)     # Freezing point of water.
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)  # Boiling point of water.

    def test_simulate_die_rolls(self):
        # Difficult to test randomness, but we can check boundaries and ensure no value is outside the die range.
        dieRolls = [random.randint(1, 6) for _ in range(100)]
        self.assertTrue(all(1 <= roll <= 6 for roll in dieRolls))

        counter = Counter(dieRolls)
        # Check if we have results for each side of the die
        self.assertTrue(all(side in counter for side in range(1, 7)))

    def test_manipulate_deque(self):
        movieStars = deque(["Robert Lopez", "John Legend", "Andrew Lloyd Webber", "Tim Rice", "Alan Menken"])
        self.assertIn("Robert Lopez", movieStars)
        self.assertIn("John Legend", movieStars)
        self.assertIn("Andrew Lloyd Webber", movieStars)

        middleInsert = len(movieStars) // 2
        movieStars.insert(middleInsert, "Rita Moreno")
        self.assertIn("Rita Moreno", movieStars)

        movieStars.appendleft("Whoopi Goldberg")
        self.assertEqual(movieStars[0], "Whoopi Goldberg")

        movieStars.append("Mel Brooks")
        self.assertEqual(movieStars[-1], "Mel Brooks")

    def test_calculate_temperatures_and_sines(self):
        celsiusTemperatures = [-40, -30, -20, -10, 0, 10, 20, 30, 40, 50]
        fahrenheitTemperatures = list(map(celsius_to_fahrenheit, celsiusTemperatures))

        # Check if the conversion is correct
        self.assertEqual(fahrenheitTemperatures[0], -40)
        self.assertEqual(fahrenheitTemperatures[4], 32)
        self.assertEqual(fahrenheitTemperatures[-1], 122)

        sineValues = list(map(lambda x: round(math.sin(math.radians(x)), 1), celsiusTemperatures))
        # Ensure sine values are in the range [-1, 1]
        self.assertTrue(all(-1 <= sine <= 1 for sine in sineValues))

        nonNegativeSines = list(filter(lambda x: x >= 0, sineValues))
        # Ensure all sine values are non-negative
        self.assertTrue(all(sine >= 0 for sine in nonNegativeSines))


if __name__ == "__main__":
    unittest.main()