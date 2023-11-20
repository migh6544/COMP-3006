import random
from collections import Counter


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

    ## Simulate 100 rolls of a six-sided die using a list comprehension.
    # For each iteration in the range of 100, a random number between 1 and 6 is generated.
    dieRolls = [random.randint(1, 6) for roll in range(100)]
    # Use the Counter class to count occurrences of each number in dieRolls.
    counter = Counter(dieRolls)
    # Retrieve the three most common numbers rolled.
    mostCommon = counter.most_common(3)
    # Iterate over the three most common numbers and print each one along with its count.
    for number, count in mostCommon:
        print(f"Number {number} appeared {count} times.")


def main():
    """
    Main function that serves as the entry point when script is run.

    Calls the simulate_die_rolls function to execute the primary functionality of this script.

    Returns:
    None
    """
    simulate_die_rolls()


## Ensure that the script's main functionality runs when the script is executed directly.
# It prevents the main() function from running when this module is imported elsewhere.
if __name__ == "__main__":
    main()