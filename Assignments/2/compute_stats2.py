# Provides access to system-specific parameters and functions
import sys
# Provides statistical functions for data analysis
import statistics
# Import the 'csv' module, which provides functionality for working with CSV (Comma-Separated Values) files.
import csv


# Replace consecutive spaces with a single space
def preprocess_line(line):
    '''
    This function replaces consecutive spaces with a single space, effectively compressing multiple spaces into one.
    This ensures that varying spacing between columns is normalized to a single space.
    '''

    return ' '.join(line.split())

def compute_stats(values):
    '''
    The function reads values from the specified data source and returns the following computed values as a tuple:

    Min: The lowest value
    Max: The highest value
    Avg: The average of the values
    Median: The middle value

    Args:
    values (list): List of values

    returns: (Min, Max, Avg, Median)
    '''

    # Calculate statistics for the valid numeric values
    if values:
        minValue = min(values)
        maxValue = max(values)
        average = statistics.mean(values)
        median = statistics.median(values)

        # Return computed values as a tuple
        return (round(minValue, 1), round(maxValue, 1), round(average, 1), round(median, 1))
    else:
        return None


def input_processing(columnNumber, dataSource):
    '''
    The function reads values from the specified data source and returns a list:

    Args:
    column_number (int): The column number to process
    data_source (str or file): The source of data to read from (either a file name or standard input)

    returns: values (List)
    '''

    # Assigning missing data value as per the data documentation
    missingData = -9999.0 or -99.000 or 'C' or 'U'
    # Initialize an empty list to store valid numeric values
    values = []

    # Check if data_source is a string (file name) or a file object
    if isinstance(dataSource, str):

        # If it's a string, try to open it as a file
        try:
            with open(dataSource, 'r') as file:
                for line in file:
                    line = preprocess_line(line)
                    rowValues = line.split(' ')
                    if columnNumber <= len(rowValues):
                        if columnNumber != 12:
                            value = rowValues[columnNumber - 1]
                        elif columnNumber == 12:
                            value = rowValues[10]
                        else:
                            print("USAGE: python3 compute_stats2.py <column Number> [Data Source] ")
                        try:
                            value = float(value)
                            # If the value is valid (not equal to missingData), append it to the values list
                            if value != missingData:
                                values.append(value)
                            if values == []:
                                print("Column is made of missing values.")
                                break
                        except ValueError:
                            pass
                    else:
                        print("Row values exceeds number of columns.")
                        break
        except FileNotFoundError:
            print(f"File not found: {dataSource}")
            sys.exit(1)
    else:
        # If data_source is not a string, assume it's a file object
        values = dataSource[columnNumber - 1]

    return values


def main():
    if len(sys.argv) < 3:
        print("USAGE: python3 compute_stats2.py <column Number> [Data Source]")
        sys.exit(1)

    try:
        columnNumber = int(sys.argv[1])
    except ValueError:
        print("Column number must be an integer and not null.")
        sys.exit(1)

    if len(sys.argv) == 3:
        dataSource = sys.argv[2]
    #else:
        # Use standard input as the default data source
        #dataSource = sys.stdin

    # Call the compute_stats function to calculate statistics
    results = compute_stats(input_processing(columnNumber, dataSource))

    # Check if there are valid results returned by compute_stats
    if results is not None:
        # Print the minimum value
        print("Min:", results[0])
        # Print the maximum value
        print("Max:", results[1])
        # Print the average value
        print("Avg:", results[2])
        # Print the median value
        print("Median:", results[3])
    else:
        # Handle the case where no valid results were generated
        print("No results were generated!")


# Entry point of the program
if __name__ == "__main__":
    # Call the main function to start the program
    main()