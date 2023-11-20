## START:
"""
Module for representing and manipulating automobile data from the auto-mpg data set.
"""

import os
import sys
import csv
import requests
import argparse
from collections import namedtuple
from collections import defaultdict
import matplotlib.pyplot as plt



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
        Also corrects the makes based on a predefined mapping of typos.
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
            reader = csv.reader(file, delimiter=' ', skipinitialspace=True)
            for row in reader:
                # Parse the record using the namedtuple for better structure
                record = Record(*row)
                # Extract make and model from the car name, correcting the make as needed
                make, *model_parts = record.car_name.replace('"', '').split()
                corrected_make = self._correct_make(make)  # Apply correction to the make
                model = ' '.join(model_parts)
                # Adjust the year to include the century
                year = (int(record.year) + 1900)
                # Convert the mpg to a float for accurate representation
                mpg = float(record.mpg)
                # Append the corrected and structured data to the data list
                self.data.append(AutoMPG(corrected_make, model, year, mpg))


    def _clean_data(self):
        """
        Cleans the raw data by converting tabs to spaces.
        """

        # Read uncleaned file and clean data
        cleanFilePath = self.filename.replace('.data.txt', '.clean.txt')
        with open(self.filename, 'r') as inFile, open(cleanFilePath, 'w') as outfile:
            for line in inFile:
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


    def _correct_make(self, make: str) -> str:
        """
        Corrects the automobile make if it is identified as a known typo.

        Args:
            make (str): The original make of the automobile.

        Returns:
            str: The corrected make of the automobile.
        """

        # Dictionary mapping known incorrect makes to the correct ones.
        corrections = {
            'chevroelt': 'chevrolet',
            'chevy': 'chevrolet',
            'maxda': 'mazda',
            # Hyphenated make corrected
            'mercedes-benz': 'mercedes',
            # Correct make remains unchanged
            'mercedes': 'mercedes',
            'toyouta': 'toyota',
            'vokswagen': 'volkswagen',
            'vw': 'volkswagen'
        }

        # Convert make to lowercase to handle case-insensitivity and get the correction if available.
        return corrections.get(make.lower(), make)


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


    def mpg_by_year(self):
        """
        Calculate the average miles per gallon (MPG) for each year present in the data set.

        Returns:
            A dictionary with years as keys and the average MPG for all cars in that year as values.
        """

        # Initialize a defaultdict to hold the sum of MPGs and count of cars for each year.
        yearData = defaultdict(lambda: {'totalMPG': 0, 'count': 0})
        for car in self.data:
            # Aggregate the total MPG and count the number of cars for each year.
            yearData[car.year]['totalMPG'] += car.mpg
            yearData[car.year]['count'] += 1

        # Calculate the average MPG for each year.
        avg_mpg_by_year = {year: data['totalMPG'] / data['count'] for year, data in yearData.items()}
        return avg_mpg_by_year


    def mpg_by_make(self):
        """
        Calculate the average miles per gallon (MPG) for each make present in the data set.

        Returns:
            A dictionary with makes as keys and the average MPG for all cars of that make as values.
        """

        # Initialize a defaultdict to hold the sum of MPGs and count of cars for each make.
        makeData = defaultdict(lambda: {'totalMPG': 0, 'count': 0})
        for car in self.data:
            # Aggregate the total MPG and count the number of cars for each make.
            makeData[car.make]['totalMPG'] += car.mpg
            makeData[car.make]['count'] += 1

        # Calculate the average MPG for each make.
        avg_mpg_by_make = {make: data['totalMPG'] / data['count'] for make, data in makeData.items()}
        return avg_mpg_by_make



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
    autoMPGData = AutoMPGData('auto-mpg.data.txt')
    # Determine the output stream based on the presence of the outfile argument
    outputStream = open(args.ofile, 'w', newline = '') if args.ofile else sys.stdout
    csvWriter = csv.writer(outputStream)

    if args.command == "print":
        # Only apply sorting if the 'print' command is being executed.
        if args.sort == "year":
            autoMPGData.sort_by_year()
        elif args.sort == "mpg":
            autoMPGData.sort_by_mpg()
        elif args.sort == "default":
            autoMPGData.sort_by_default()

        # Output the data in CSV format
        for car in autoMPGData:
            csvWriter.writerow([car.make, car.model, car.year, car.mpg])

    elif args.command == "mpg_by_year":
        # Get and sort the average mpg by year
        avg_mpg_by_year = dict(sorted(autoMPGData.mpg_by_year().items()))
        # Output in CSV format
        csvWriter.writerow(['Year', 'Average MPG'])
        for year, mpg in avg_mpg_by_year.items():
            csvWriter.writerow([year, mpg])

        if args.plot:
            plot_data(avg_mpg_by_year, 'Year', 'Average MPG', 'Average MPG by Year')

    elif args.command == "mpg_by_make":
        # Get and sort the average mpg by make
        avg_mpg_by_make = dict(sorted(autoMPGData.mpg_by_make().items()))
        # Output in CSV format
        csvWriter.writerow(['Make', 'Average MPG'])
        for make, mpg in avg_mpg_by_make.items():
            csvWriter.writerow([make, mpg])

        if args.plot:
            plot_data(avg_mpg_by_make, 'Make', 'Average MPG', 'Average MPG by Make', horizontal = True)

    # Close the output file if one was opened
    if args.ofile:
        outputStream.close()


def plot_data(data, xlabel, ylabel, title, horizontal = False):
    keys = list(data.keys())
    values = list(data.values())
    plt.figure(figsize = (10, 5))
    if horizontal:
        plt.barh(keys, values, color = 'lightgreen')
        plt.xlabel(ylabel)
        plt.ylabel(xlabel)
    else:
        plt.bar(keys, values, color = 'skyblue')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    # Create a parser object
    parser = argparse.ArgumentParser(description = "Analyze Auto MPG data set")
    # Add the required 'command' positional argument
    parser.add_argument("command", type = str, choices = ["print", "mpg_by_year", "mpg_by_make"], help = "command to execute (print, mpg_by_year, mpg_by_make)")
    # Add the optional 'sort' argument
    parser.add_argument("-s", "--sort", type = str, choices = ["year", "mpg", "default"], default = "default", help = "sorting order for the data")
    # Add optional 'ofile' argument
    parser.add_argument("-o", "--ofile", type = str, help = "output file name")
    # Add optional 'plot' argument
    parser.add_argument("-p", "--plot", action = "store_true", help = "specify to create graphical output")
    # Parse the command-line arguments
    args = parser.parse_args()
    # Execute the main function with the parsed arguments
    main(args)


## END.