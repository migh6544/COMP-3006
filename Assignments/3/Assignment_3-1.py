### START:
# Import the 'csv' module to enable functionality related to CSV files.
import csv


def simulate_population_growth(x0, a, d_t, t_end):
    """
    Simulate exponential population growth based on given parameters.

    Parameters:
    - x0 (float): Initial population at time t=0.
    - a (float): Growth rate coefficient.
    - d_t (float): Incremental time step for the simulation.
    - t_end (float): Final time to stop the simulation.

    Returns:
    - list: List of tuples containing time and corresponding population values.
    """

    # Set the initial population from the provided value.
    x = x0
    # Start the simulation time at zero.
    t = 0
    # Create a list to store results, initializing with column headers.
    results = [("Time", "Population")]
    # Continue simulating until the simulation time exceeds the specified end time.

    while t <= t_end:
        # Add the current time and population to the results list.
        results.append((t, x))
        # Calculate the rate of change of the population.
        x_dot = (a * x)
        # Update the population value using the calculated rate and the time step.
        x += (x_dot * d_t)
        # Increment the simulation time by the time step.
        t += d_t
    # Return the list of results.
    return results


def write_to_csv(results, fileName):
    """
    Write the simulation results to a CSV file with consistent spacing.

    Parameters:
    - results (list): List of tuples with simulation time and population values.
    - fileName (str): Desired name for the output CSV file.

    Returns:
    - None
    """

    # Calculate the maximum length of time values to determine spacing in the CSV.
    columnGap = max(len(str(t)) for t, _ in results[1:])

    # Open the specified CSV file for writing.
    with open(fileName, "w") as file:
        # Write the column headers with consistent spacing.
        file.write("Time".ljust(columnGap) + "Population\n")
        # Write each time and population entry with consistent spacing.
        for time, population in results[1:]:
            file.write(f"{time:.2f}".ljust(
                columnGap) + f"{population:.2f}\n")


def main():
    """
    Main execution function. Simulates exponential growth, displays results, and writes them to a CSV.

    Returns:
    - None
    """

    ## Set the initial simulation parameters.
    # Initial population.
    x0 = 100
    # Growth rate coefficient.
    a = 5
    # Simulation time step.
    d_t = 0.1
    # End time for the simulation.
    t_end = 2
    # Obtain the simulation results by calling the simulate_population_growth function.
    results = simulate_population_growth(x0, a, d_t, t_end)

    # Display each simulation result on the console.
    for time, population in results[1:]:
        print(f"Time: {time:.2f}, Population: {population:.2f}")

    # Write the simulation results to a CSV file.
    write_to_csv(results, "Population_Growth_Simulation.csv")


# Ensure the main() function is executed only if the script is run directly.
if __name__ == "__main__":
    main()
### End.