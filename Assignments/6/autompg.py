## START:
"""
Module for representing and manipulating automobile data from the auto-mpg data set.
"""

import os
import csv
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

        # Check if clean data exists, if not call _clean_data
        if not os.path.exists(cleanFilePath):
            self._clean_data()

        # Define the named tuple for structured data parsing
        Record = namedtuple('Record', ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
                                    'acceleration', 'year', 'origin', 'car_name'])

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


def main(filename: str):
    """
    Main function to instantiate an AutoMPGData object and iterate over it to print each AutoMPG object.
    """

    autoMPGData = AutoMPGData(filename)

    for car in autoMPGData:
        # using __repr__ method to get the desired format
        print(car.__repr__())



if __name__ == "__main__":
    main('auto-mpg.data.txt')


## END.