## Start:


import numpy as np
import matplotlib.pyplot as plt



'''
COMP 3006
Homework 9 - Numpy

General Homework Guidelines:
- Homework must be submitted in a .py file. Please do not submit .ipynb files.
- Homework should not use packages or functions that have not yet been discussed in class.
- Use comments to explain what your code is doing.
- Use a consistent coding style.
- Use descriptive variable names.
- Test your code regularly using a variety of different inputs.
- Every function must include a docstring for documentation (see:
   https://realpython.com/documenting-python-code/). This docstring should include:
     - 1 or 2 lines describing what the function does
     - Args: input parameters, their types and what they are for
     - Returns: return data type and what it is
- All tests of your functions should be commented out in your final submission or
  encolosed with an if __name__ == '__main__' codeblock.
- All functions should use return statements to return a value, rather than
  printing some value, unless the instructions specifically say to print.
'''
#--------------------------------------------------------------------------#

#Assignment 9.1
# Create a class, called Distributions, that has the following attributes : distribution, mean, standard deviation and size.
# It should have a constructor, __str__ and the ability to generate a normal distribution, lognormal and laplace distributions
# based on the distribution attribute.
# For example:
# my_distribution = Distributions(dist="lognormal", mean=1, std=5, samples=100)
# should be a lognormal distribution with a mean of 1, standard deviation of 5 and have 100 samples from the distribution

class Distributions:
    """
    A class to represent different statistical distributions.

    Attributes:
        distribution (str): Type of distribution ('normal', 'lognormal', or 'laplace').
        mean (float): The mean of the distribution.
        std (float): The standard deviation of the distribution.
        size (int): The number of samples to generate from the distribution.
        data (ndarray): An array of generated samples.

    Methods:
        generate_distribution(): Generates samples based on the specified distribution.
    """


    def __init__(self, dist, mean, std, samples):
        """
        Constructs all the necessary attributes for the Distributions object.

        Parameters:
            dist (str): Type of distribution ('normal', 'lognormal', or 'laplace').
            mean (float): The mean of the distribution.
            std (float): The standard deviation of the distribution.
            samples (int): The number of samples to generate.
        """

        if not isinstance(mean, (int, float)):
            raise ValueError("\nError: Mean must be a numeric value!\n")
        if not isinstance(std, (int, float)) or std < 0:
            raise ValueError("\nError: Standard deviation must be a non-negative numeric value!\n")
        if not isinstance(samples, int) or samples <= 0:
            raise ValueError("\nError: Samples must be a positive integer!\n")

        self.distribution = dist
        self.mean = mean
        self.std = std
        self.size = samples
        self.data = self.generate_distribution()


    def __str__(self) -> str:
        """
        Provides a human-readable string representation of the Distributions object.

        Returns:
            str: A string representation of the Distributions object.
        """

        return (f"Distributions(Type: {self.distribution}, Mean: {self.mean}, Std: {self.std}, Size: {self.size})")


    def generate_distribution(self):
        """
        Generates samples from the specified distribution using numpy's random methods.

        Returns:
            ndarray: An array of samples from the specified distribution.

        Raises:
            ValueError: If an invalid distribution type is provided.
        """

        if self.distribution == ("normal"):
            return np.random.normal(self.mean, self.std, self.size)
        elif self.distribution == ("lognormal"):
            return np.random.lognormal(self.mean, self.std, self.size)
        elif self.distribution == ("laplace"):
            return np.random.laplace(self.mean, self.std, self.size)
        else:
            raise ValueError("\nInvalid distribution type!\n Try: 'normal', 'lognormal', or 'laplace'.\n")


# Assignment 9.2:
# Repeat the first part, this time calling the class NumpyDistribution, using only numpy methods
# Hint: https://numpy.org/doc/1.22/, you may want to looks at using args and kwargs

class NumpyDistribution:
    """
    A class to generate different statistical distributions using numpy.

    This class allows for the creation of normal, lognormal, and Laplace distributions,
    among other distributions supported by numpy, with specified parameters.

    Attributes:
        distribution (str): The name of the numpy distribution function (e.g., 'normal', 'lognormal').
        args (tuple): Positional arguments for the numpy distribution function.
        kwargs (dict): Keyword arguments for the numpy distribution function.
        data (ndarray): Generated samples from the specified distribution.
    """


    def __init__(self, dist, *args, **kwargs):
        """
        Constructs the NumpyDistribution object with specified distribution and parameters.

        Parameters:
            dist (str): The name of the numpy distribution function (e.g., 'normal', 'lognormal').
            *args: Variable length argument list for the distribution function.
            **kwargs: Arbitrary keyword arguments for the distribution function.
        """

        self.distribution = dist
        self.args = args
        self.kwargs = kwargs
        # Validate args and kwargs
        self.validate_parameters()
        self.data = self.generate_distribution()


    def validate_parameters(self):
        """
        Validate the parameters passed to the distribution function.
        """

        for arg in self.args:
            if not isinstance(arg, (int, float)):
                raise TypeError("\nError: All positional arguments must be numeric!\n")

        for key, value in self.kwargs.items():
            if key == 'size':
                if not isinstance(value, int) or value <= 0:
                    raise ValueError("\nError: 'size' must be a positive integer!\n")
            else:
                if not isinstance(value, (int, float)):
                    raise ValueError(f"\nError: All keyword arguments except 'size' must be numeric. Invalid value for '{key}'!\n")



    def __str__(self):
        """
        Provides a human-readable string representation of the NumpyDistribution object.

        Returns:
            str: A string representation of the NumpyDistribution object.
        """
        return (f"NumpyDistribution(Type: {self.distribution} | (Mean, Std): {self.args} | Sample: {self.kwargs})")


    def generate_distribution(self):
        """
        Generates samples from the specified distribution using numpy's random methods.

        Returns:
            ndarray: An array of samples from the specified distribution.

        Raises:
            ValueError: If an invalid distribution type is provided.
        """

        if hasattr(np.random, self.distribution):
            distributionFunc = getattr(np.random, self.distribution)
            return distributionFunc(*self.args, **self.kwargs)
        else:
            raise ValueError(f"\nInvalid distribution type '{self.distribution}'!\n Please provide a valid numpy distribution function name.\n https://numpy.org/doc/1.22/\n")


# Assignment 9.3:
# Use only methods from numpy and matplotlib.
# Display the plot of one period of both the cosine and sine. They should appear on the same axes. Label the axes and the plot. Provide a grid.
# Display the plot of one period of both the cosine and sine. They should appear on the different axes but share the y-axis. Label the axes and the plot. Provide a grid.
# Display the plot of one period of both the cosine and sine. They should appear on the different axes but share the x-axis. Label the axes and the plot. Provide a grid.

# Define the range for one period (0 to 2Pi)
x = np.linspace(0, (2 * np.pi), 1000)

# Calculate sine and cosine values
ySin = np.sin(x)
yCos = np.cos(x)

# Plot sine and cosine on the same axes
plt.figure(figsize = (10, 6))
plt.plot(x, ySin, label = 'Sine')
plt.plot(x, yCos, label = 'Cosine')
plt.title('Sine and Cosine Dual-Axes')
plt.xlabel('Angle (Radians)')
plt.ylabel('Value')
plt.grid(True)
plt.legend()
plt.show()

# Plot sine and cosine on different axes, sharing the y-axis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 6), sharey = True)

ax1.plot(x, ySin, color = 'blue')
ax1.set_title('Sine')
ax1.set_xlabel('Angle (Radians)')
ax1.set_ylabel('Value')
ax1.grid(True)

ax2.plot(x, yCos, color = 'orange')
ax2.set_title('Cosine')
ax2.set_xlabel('Angle (radians)')
ax2.grid(True)

plt.show()

# Plot sine and cosine on different axes, sharing the x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (10, 10), sharex = True)

ax1.plot(x, ySin, color = 'blue')
ax1.set_title('Sine')
ax1.set_ylabel('Value')
ax1.grid(True)

ax2.plot(x, yCos, color = 'orange')
ax2.set_title('Cosine')
ax2.set_xlabel('Angle (Radians)')
ax2.set_ylabel('Value')
ax2.grid(True)

plt.show()


# Assignment 9.4:
# In a separate file, test_homework9.py, write the necessary unittests for questions 9.1 and 9.2. Take careful consideration to
# test valid and invalid values for the creation of any of the distributions.

def main():
    # Testing Distributions class
    myDistribution = Distributions(dist = "lognormal", mean = 1, std = 5, samples = 100)
    print(myDistribution)

    # Testing NumpyDistribution class
    myNPDistribution = NumpyDistribution('lognormal', 1, 5, size = 100)
    print(myNPDistribution)



if __name__ == '__main__':
    main()


## END.