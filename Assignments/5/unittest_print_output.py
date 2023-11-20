#Imports:
from io import StringIO
import sys


def studentOutput(someFunc, *args, **kwargs):
    """
    Captures the output from student's print statement

    Args:
        comeFunc (module): a given function
        *args: additional arguments needed for the function
        **kwargs: additional keyword arguments for the function

    Return:
        str: captured output from a print statement
    """
    #Create string io object to capture print output:
    capturedOutput = StringIO()

    # Redirect stdout to capturedOutput:
    sys.stdout = capturedOutput

    #Function call:
    returnedOutput = someFunc(*args, **kwargs)

    #Reset output redirect after capturing print statement:
    sys.stdout = sys.__stdout__

    #Print output without new line character:
    printedOutput = capturedOutput.getvalue().strip()

    #Return the function's output and the printed value:
    return returnedOutput, printedOutput