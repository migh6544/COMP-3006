## START:
import unittest
from Quadratic import QuadraticEquation
from io import StringIO
import sys


def studentOutput(someFunc, *args, **kwargs):
    """
    Captures the output from student's print statement.

    Args:
        someFunc (module): a given function
        *args: additional arguments needed for the function
        **kwargs: additional keyword arguments for the function

    Return:
        tuple: A tuple containing the returned value of the function and the printed output.
    """

    # A new StringIO object is created. This is an in-memory file-like object.
    # It can be used as a string buffer which can capture the output.
    capturedOutput = StringIO()

    # The standard output is redirected to our `capturedOutput`.
    # This means anything that gets printed will now go to `capturedOutput` instead of the console.
    sys.stdout = capturedOutput

    # The function `someFunc` is called with any provided arguments and its output is stored.
    returnedOutput = someFunc(*args, **kwargs)

    # Standard output is reset to its default value, so future prints will go to the console.
    sys.stdout = sys.__stdout__

    # The content that was "printed" to `capturedOutput` is extracted and returned.
    printedOutput = capturedOutput.getvalue().strip()

    return (returnedOutput, printedOutput)


class TestQuadraticEquation(unittest.TestCase):
    """
    Test suite for the QuadraticEquation class.
    """

    def test_discriminant(self):
        """
        Test the calculation of the discriminant.
        """

        # An instance of QuadraticEquation is created for testing
        equation = QuadraticEquation(1, -3, 2)
        # Assert that the discriminant method returns the correct value
        self.assertEqual(equation.discriminant(), 1)

    def test_normal_roots(self):
        """
        Test case for normal roots.
        """

        # An instance of QuadraticEquation is created for testing
        equation = QuadraticEquation(1, -3, 2)
        # Assert that the roots method returns the correct roots
        self.assertEqual(equation.roots(), (2.0, 1.0))

    def test_identical_roots(self):
        """
        Test case for identical roots.
        """

        # An instance of QuadraticEquation is created for testing
        equation = QuadraticEquation(1, 2, 1)
        # Assert that the roots method returns a single root (since they are identical)
        self.assertEqual(equation.roots(), (-1.0))

    def test_no_real_roots(self):
        """
        Test case for scenarios with no real roots.
        """

        # An instance of QuadraticEquation is created for testing
        equation = QuadraticEquation(1, 0, 1)
        # Here we are testing an exception. We expect a ValueError to be raised.
        with self.assertRaises(ValueError) as context:
            equation.roots()
        # Further assert that the raised exception has the expected error message.
        self.assertEqual(str(context.exception), "Discriminant is negative: No real roots.")

    def test_linear_equation(self):
        """
        Test case for when a = 0, which means the equation is linear.
        """

        # We will use a linear equation: 0x^2 + 3x - 2 = 0 or 3x - 2 = 0 for this test.
        equation = QuadraticEquation(0, 3, -2)
        # The root for the linear equation 3x - 2 = 0 is x = 2/3.
        expectedRoot = (2 / 3)
        # Assert the expected and returned values.
        self.assertEqual(equation.roots(), expectedRoot)

    def test_linear_no_solution(self):
        """
        Test case for when a = 0, b = 0, and c != 0, which means no solution for the linear equation.
        """

        equation = QuadraticEquation(0, 0, 2)

        with self.assertRaises(ValueError) as context:
            equation.roots()

        self.assertEqual(str(context.exception), "The equation has no solution.")

    def test_linear_always_true(self):
        """
        Test case for when a = 0, b = 0, and c = 0, which means the equation is always true for all x.
        """

        equation = QuadraticEquation(0, 0, 0)

        with self.assertRaises(ValueError) as context:
            equation.roots()

        self.assertEqual(str(context.exception),
                         "The equation is always true for all x.")

    def test_str_representation(self):
        """
        Test the informal string representation of the QuadraticEquation.
        """

        # An instance of QuadraticEquation is created for testing
        equation = QuadraticEquation(1, -3, 2)

        # We assert that the string representation of the equation object matches our expectation
        self.assertEqual(str(equation), "x^2 - 3x + 2 = 0")

    def test_str_print_output(self):
        """
        Test the printed output of the informal string representation.
        """

        # An instance of QuadraticEquation is created for testing
        equation = QuadraticEquation(1, -3, 2)
        expectedOutput = "x^2 - 3x + 2 = 0"

        # We utilize the studentOutput function to capture the print output
        printedOutput = studentOutput(print, equation)[1]

        # We assert that the captured print output matches our expectation
        self.assertEqual(printedOutput, expectedOutput)


# This line ensures the unittests are executed when this script is run.
if __name__ == "__main__":
    unittest.main()
## END.