## START:
"""
Module for representing and manipulating automobile data from the auto-mpg data set.
"""

import os
import csv
import requests
import argparse
from collections import namedtuple



class AutoMPGData:
    def __init__(self, filename: str):
        """
        Initializes the AutoMPGData object by loading the data from the given file.

        Args:
            filename (str): Path to the raw data file.
        """

        self.filename = filename
        self.data = []
        self._load_data()


    def __iter__(self):
        """
        Returns an iterator over the data.
        """

        return iter(self.data)


    def _load_data(self):
        """
        Load the cleaned data from file or clean the raw data if necessary.
        """

        cleanFilePath = self.filename.replace('.data.txt', '.clean.txt')

        # Check if clean data exists, if not check if raw data exists or get it
        if not os.path.exists(cleanFilePath):
            if not os.path.exists(self.filename):
                # Download data if original file doesn't exist
                self._get_data()
            self._clean_data()

        # Define the named tuple for structured data parsing
        Record = namedtuple('Record', ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'year', 'origin', 'car_name'])

        # Load the cleaned data and instantiate AutoMPG objects
        with open(cleanFilePath, 'r') as file:
            reader = csv.reader(file, delimiter = ' ', skipinitialspace=True)
            for row in reader:
                record = Record(*row)
                make, *model_parts = record.car_name.replace('"', '').split()
                model = ' '.join(model_parts)
                year = (int(record.year) + 1900)
                mpg = float(record.mpg)
                self.data.append(AutoMPG(make, model, year, mpg))


    def _clean_data(self):
        """
        Cleans the raw data by converting tabs to spaces.
        """

        # Read uncleaned file and clean data
        cleanFilePath = self.filename.replace('.data.txt', '.clean.txt')
        with open(self.filename, 'r') as infile, open(cleanFilePath, 'w') as outfile:
            for line in infile:
                # Convert tabs to spaces
                cleanedLine = line.expandtabs()
                outfile.write(cleanedLine)


    def _get_data(self):
        """
        Downloads the AutoMPG dataset from the UCI Machine Learning Repository.

        If the original data file doesn't exist, this method will fetch the data from the
        UCI repository and save it as 'auto-mpg.data.txt' locally.
        """

        # URL for the AutoMPG dataset from the UCI repository
        url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"

        # Use requests to fetch the data
        response = requests.get(url)

        # Ensure we received a successful response
        response.raise_for_status()

        # Write the data to the local file
        with open(self.filename, 'wb') as file:
            file.write(response.content)



    def sort_by_default(self):
        """
        Sorts the list of AutoMPG objects in place using the default sorting order.

        The default sorting is determined by the less-than operator (__lt__) of the AutoMPG class.
        This results in sorting by mpg, year, make, and then model.
        """

        # Use the built-in sort method of the list to sort in place.
        # Since no custom key is provided, it will use the default sorting order defined by the __lt__ method of AutoMPG.
        self.data.sort()


    def sort_by_year(self):
        """
        Sorts the list of AutoMPG objects in place based on year primarily and then by make, model, and mpg.

        Overrides the default sorting to ensure the data is ordered by year first.
        """

        # Use the built-in sort method of the list to sort in place.
        # Provide a custom key using a lambda function that returns a tuple.
        # The tuple orders attributes by year, make, model, and then mpg.

        self.data.sort(key = lambda car: (car.year, car.make, car.model, car.mpg))


    def sort_by_mpg(self):
        """
        Sorts the list of AutoMPG objects in place based on mpg primarily and then by make, model, and year.

        Overrides the default sorting to ensure the data is ordered by mpg first.
        """

        # Use the built-in sort method of the list to sort in place.
        # Provide a custom key using a lambda function that returns a tuple.
        # The tuple orders attributes by mpg, make, model, and then year.

        self.data.sort(key = lambda car: (car.mpg, car.make, car.model, car.year))



class AutoMPG:
    """
    Class representing automobile data from the auto-mpg data set.

    Attributes:
        make (str): Automobile manufacturer.
        model (str): Automobile model.
        year (int): Year of manufacture.
        mpg (float): Miles per gallon.
    """

    def __init__(self, make: str, model: str, year: int, mpg: float):
        """
        Initializes the attributes of the AutoMPG object.

        Args:
            make (str): Automobile manufacturer.
            model (str): Automobile model.
            year (int): Year of manufacture.
            mpg (float): Miles per gallon.
        """

        self.make = make
        self.model = model
        self.year = year
        self.mpg = mpg


    def __repr__(self) -> str:
        """
        Return a formal representation of the object.
        """

        return (f"AutoMPG({self.make!r}, {self.model!r}, {self.year}, {self.mpg})")


    def __str__(self) -> str:
        """
        Return a string representation of the object for end users.
        """

        return (f"{self.make} {self.model} ({self.year}) - {self.mpg} mpg")


    def __eq__(self, other) -> bool:
        """
        Check equality between two AutoMPG objects.
        """

        if not isinstance(other, AutoMPG):
            return NotImplemented
        return (self.make, self.model, self.year, self.mpg) == (other.make, other.model, other.year, other.mpg)


    def __lt__(self, other) -> bool:
        """
        Less-than comparison between two AutoMPG objects.
        """

        if not isinstance(other, AutoMPG):
            return NotImplemented
        return (self.mpg, self.year, self.make, self.model) < (other.mpg, other.year, other.make, other.model)


    def __hash__(self) -> int:
        """
        Return the hash value of the object.
        """

        return hash((self.make, self.model, self.year, self.mpg))


def main(args):
    """
    Main function to instantiate an AutoMPGData object, sort the data based on the provided
    argument, and iterate over it to print each AutoMPG object.
    """

    autoMPGData = AutoMPGData('auto-mpg.data.txt')

    # Use the provided sorting argument to sort the data
    if args.sort == "year":
        autoMPGData.sort_by_year()
    elif args.sort == "mpg":
        autoMPGData.sort_by_mpg()
    elif args.sort == "default":
        autoMPGData.sort_by_default()

    # If the command is "print", print the data
    if args.command == "print":
        for car in autoMPGData:
            print(car.__repr__())


if __name__ == "__main__":
    # Create a parser object
    parser = argparse.ArgumentParser(description = "analyze Auto MPG data set")
    # Add the required 'command' positional argument
    parser.add_argument("command", type = str, help = "command to execute")
    # Add the optional 'sort' argument
    parser.add_argument("-s", "--sort", type = str, choices = ["year", "mpg", "default"], default = "default", help = "sorting order for the data")
    # Parse the command-line arguments
    args = parser.parse_args()
    # Execute the main function with the parsed arguments
    main(args)


## END.