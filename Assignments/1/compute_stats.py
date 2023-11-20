# Provides access to system-specific parameters and functions
import sys
# Provides statistical functions for data analysis
import statistics

# Initialize an empty list to store valid numeric values
values = []
# Assigning missing data value as per the data documentation
missingData = -9999.0

# Loop through each line of input from the standard input (piped input)
for line in sys.stdin:
    value = float(line.strip())
    # If the value is valid (not equal to missingData), append it to the values list
    if value != missingData:
        values.append(value)

# Calculate statistics for the valid numeric values
if values:
    minValue = min(values)
    maxValue = max(values)
    average = statistics.mean(values)
    median = statistics.median(values)

# Print computed values as per the format in HW sample
print(f"min: {minValue:.1f}, max: {maxValue:.1f}, average: {average:.13f}, median: {median:.2f}")