'''
COMP 3006
Homework 10 - Pandas

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

# Assignment 10.1:
# Create a class, LinearSolver, which applies Cramer's Rule to solve simultaneous linear
# equations of 3 unknowns. The class must implement the following methods: contructor, __str__,
# check_system and solver.
# -The check_system method should verify that the linear system of equations is 3x3 and that
# the constants is 3x1.
# -The solver method should implement Cramer's Rule and return the solution to the linear
# system as a 1d array.
# It must also contain the attributes : system (this is the linear system of equations) and
# contants (this is a 1-d array with the coefficients).
#
# An example of what the coefficient matrix A looks like:
# A = np.array([[5, -14, -3], [1, 2, 2], [-7, 4, 5]]),
# and the constants are: -39, -2, and -29.
# Hint: For the determinant of matrix A use np.linalg.det(A).

# Assignment 10.2:
# Create 2 custom loggers, systemLogger and solutionLogger, which write to linearSystem.log and
# solution.log respectively. Use argparser to include the ability to set the logging level for each
# logger but by default both loggers must have a default level of DEBUG. They must also implement
# the following format:
# Time when the LogRecord was created : logging level : line number : message
# (You will need to read the documentation at https://docs.python.org/3/library/logging.html)

# Assignment 10.3:
# Create a class, GradeSytem, which holds the grades for a number of classes and a certain number
# of students. The class must implement the following methods: constructor, __str__, __repr__,
# class_stats, class_summary, student_stats, check_students and grades_graph.
# -class_stats should calculate the average and standard deviation of the grades in the class.

# -student_stats should calculate a student's average grade and standard deviation of their grades. To
# make this easier, you may assume that a student is in the same location in each grades list. So the
# student in the first entry in the Math class will also be the first entry in the Science class and so on.

# -check_students must verify that every class has the same number of entries for the students list. It must
# be possible for each class to have a different number of students, i.e. Math might have 20 students whilst
# English might have 16 students. Hint: think of using a filler value like -1 and make sure to handle that
# case in your stats.

# -grades_graph should create a bar plot of the grades either for a class (x-axis should be the student, you can
# simply use the student's location in the grades list to represent them) or for a student (x-axis should be
# the class name). All plots must have appropriate title and axis labels.

# The class must implement a Pandas DataFrame in order to store all the data and compute all the required
# statistics using the built-in DataFrame functions (this is why the length of the grades list must be the
# same for all classes. The 5 number summary could be done using methods not built-in to DataFrames).
# This is a sample of a dictionary that could be used to create a Pandas DataFrame for 8 students (Note: this
# is a sort of base case where all classes have the same number of students and this won't always be the case)
# Eight students' grades in their respective courses are given via this dictionary: {'Math' : [80, 89, 93, 66, 84, 85, 74, 64],
# 'Science' : [94, 76, 88, 78, 88, 92, 60, 85], 'English' : [83, 76, 93, 96, 77, 85, 92, 60], 'History' : [96, 66, 76, 85, 78, 88, 69, 99]}
# Upload a zip of your source file(s).

# Optional (although you should always do this):
# Create Unittests for all of your code.