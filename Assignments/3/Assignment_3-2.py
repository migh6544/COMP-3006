### START:
# Import the necessary module to handle CSV files.
import csv


def read_elements(file_name):
    """
    Read elements from a CSV file and return a list of rows.

    Parameters:
    - file_name (str): Name of the CSV file to read.

    Returns:
    - list: List of rows where each row is a list of column values.
    """

    # Open the specified CSV file in read mode.
    with open(file_name, 'r') as file:
        # Create a CSV reader object for the opened file.
        reader = csv.reader(file)
        # Return all rows from the CSV file as a list.
        return [row for row in reader]


def main():
    """
    Main execution function. Reads elements from a CSV file, sorts based on atomic number in reverse, 
    and then prints them with proper alignment.

    Returns:
    - None
    """

    # Read the elements from the specified CSV file.
    rows = read_elements('First_Eight_Elements.csv')
    # Calculate the maximum width needed for each column to ensure proper alignment when printing.
    columnWidths = [max(len(row[colIdx]) for row in rows)
        for colIdx in range(len(rows[0]))
    ]

    # Print the header row, ensuring each header aligns with its column width.
    print(' '.join(word.ljust(columnWidths[idx])
          for idx, word in enumerate(rows[0])))

    ## Sort the rows (excluding the header) based on atomic number in reverse order.
    # The lambda function is used to extract the atomic number (as an integer) from each row to serve as the sorting key.
    sortedRows = sorted(rows[1:], key = (lambda x: int(x[0])), reverse = True)

    # Print each sorted row, ensuring columns are properly aligned.
    for row in sortedRows:
        print(' '.join(word.ljust(columnWidths[idx])
              for idx, word in enumerate(row)))


# This conditional ensures that the main function is executed only when this script is run directly (not imported).
if __name__ == "__main__":
    main()
### END.