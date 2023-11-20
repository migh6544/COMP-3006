import os
import sys
import csv
import collections
from typing import Iterator


print(sys.argv)


#Files:
# original_file = '/path/to/your/file'
original_file = './auto_mpg/auto-mpg.data.txt'
clean_file = './auto_mpg/auto-mpg.clean.txt'


class AutoMPG:
    """
    This class stores the make, model, year and mpg for cars

    Attributes:
    -----------
        make (str) : manufacturer. Uses .title() to avoid uppercase/lowercase issues
        model (str) : car model. Uses .title() to avoid uppercase/lowercase issues
        year (int) : manufacturing year
        mpg (float) : miles per gallon
    
    Methods:
    ---------
        __repr__ : returns string representation of an AutoMPG object
        
        __str__ : returns string representation using __repr__ method
        
        __eq__ : checks equality between two AutoMPG objects using make, 
        model, year and mpg.
        
        __lt__ : checks inequality between two AutoMPG objects using make, 
        model, year and mpg.
        
        __hash__ : implements a hashing method for AutoMPG objects
    """
    
    def __init__(self, make: str, model: str, year: int, mpg: float) -> None:
        self.make = make.title()
        self.model = model.title()
        self.year = int(year)
        self.mpg = float(mpg)

    def __repr__(self) -> str:
        return f"AutoMPG({self.make}, {self.model}, {self.year}, {self.mpg})"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __eq__(self, other):
        """Checks if two AutoMPG objects have the same make, model, year and mpg"""
        if (type(self) == AutoMPG) and (type(other) == AutoMPG):
            if (self.make == other.make) \
            and (self.model == other.model) \
            and (self.year == other.year) and (self.mpg == other.mpg):
                return True
            else:
                return False
        else:
            return NotImplemented
        
    def __lt__(self, other):
        """Compares 2 AutoMPG objects by make, model, year and then mpg"""
        if (type(self) == AutoMPG) and (type(other) == AutoMPG):
            if self.make == other.make:
                if self.model == other.model:
                    if self.year == other.year:
                        if self.mpg <= other.mpg:
                            return True
                        else:
                            return False
                    elif self.year < other.year:
                        return True
                    else:
                        return False
                elif self.model < other.model:
                    return True
                else:
                    return False
            elif self.make < other.make:
                return True
            else:
                return False
        else:
            return NotImplemented
        
    def __hash__(self) -> int:
        return int(self.year + self.mpg)
        

class AutoMPGData:
    """
    Class is a container of AutoMPG objects

    Attributes:
    -----------
        data (List[AutoMPG]) : list of AutoMPG class objects
    
    Methods:
    ----------
        __iter__ : returns an iterator of the AutoMPG list
        
        _load_data : loads data and creates a list of AutoMPG objects
        
        _clean_data : loads original data (auto-mpg.data.txt) and creates 
        a clean data file (auto-mpg.clean.txt)
    """

    def __init__(self) -> None:
        """Constructor"""
        self.data = []

        self._load_data(clean_file)

    def __iter__(self) -> Iterator:
        """Returns an iterator of the list of AutoMPG objects"""
        return iter(self.data)
    
    @staticmethod
    def _clean_data(file: str) -> None:
        """
        Loads in original data file and creates a clean data file

        Args:
            file (str): path+file where clean data should be
        
        Return:
            None
        """
        with open(file, 'r') as orig_data:
            path = file.rsplit("/", maxsplit=1)
            with open(path[0] + '/auto-mpg.clean.txt', 'w') as clean_data:
                for line in orig_data.readlines():
                    clean_data.write(line.expandtabs())
        return


    def _load_data(self, file: str) -> None:
        """
        Loads cleaned data file, parses data and add it to the list 
        of AutoMPG

        Args:
            file (str): file name of cleaned data
        
        Return:
            None
        """
        #Check if clean data file exists
        if not os.path.exists(file):
            #Retrieve path given for clean file.
            #Assumes auto-mpg.data.txt is in the same directory
            path = file.rsplit("/", maxsplit=1) 
            #Clean original file and create auto-mpg.clean.txt
            self._clean_data(path[0] + '/auto-mpg.data.txt')
        
        #Create empty list to store AutoMPG objects:
        if self.data is None:
            self.data = []

        #Open clean data file and read in data:
        with open(file, 'r') as car_file:
            cars = csv.reader(car_file, delimiter=" ", skipinitialspace=True)

            #Create namedtuple object:
            car_record = collections.namedtuple('Record', ['mpg', 'cylinders', \
                                'displacement','horsepower', 'weight', 'acceleration', \
                                'year', 'origin', 'make_model'])

            for row in cars:
                car = car_record(float(row[0]), row[1], row[2], row[3], row[4], \
                                 row[5], int(row[6]), row[7], row[8])
                
                #Use try/except to handle cars that only have make but
                #no model
                try:
                    #split car name to get make and model
                    make_model = car.make_model.split()
                    #get make
                    make = make_model[0]
                    #join model name
                    model = " ".join(make_model[1:])
                    #Create and append AutoMPG objects to data list:
                    self.data.append(AutoMPG(make, model, car.year, car.mpg))
                except IndexError:
                    pass
        return  


def main():
    my_auto_object = AutoMPGData()
    
    for a in my_auto_object:
        # continue
        print(a)


if __name__=="__main__":
    main()
















