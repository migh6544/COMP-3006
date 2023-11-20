## START:


from Programming_Assignment import LinearSolver, GradeSystem, setup_logger
import os
import unittest
import numpy as np
import logging



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

# Optional (although you should always do this):
# Create Unittests for all of your code.

class TestLinearSolver(unittest.TestCase):
    def test_valid_input(self):
        A = np.array([[3, -2, 5], [1, 1, 1], [2, 3, 4]])
        B = np.array([0, 6, 12])
        solver = LinearSolver(A, B)
        solution = [4.5, 3.0, -1.5]
        np.testing.assert_array_almost_equal(solver.solver(), solution)

    def test_non_square_system(self):
        A = np.array([[2, -1], [1, 1], [2, 2]])
        B = np.array([4, 6, 10])
        with self.assertRaises(ValueError):
            LinearSolver(A, B)

    def test_incorrect_constants_dimension(self):
        A = np.array([[2, -1, 1], [1, 1, 1], [2, 2, 2]])
        B = np.array([4, 6])
        with self.assertRaises(ValueError):
            LinearSolver(A, B)

    def test_no_unique_solution(self):
        A = np.array([[2, 4, 6], [1, 2, 3], [3, 6, 9]])
        B = np.array([4, 6, 10])
        solver = LinearSolver(A, B)
        with self.assertRaises(ValueError):
            solver.solver()

class TestLoggerSetup(unittest.TestCase):
    def test_default_debug_level(self):
        logger = setup_logger('testLogger1', 'test1.log')
        self.assertEqual(logger.level, logging.DEBUG)

    def test_custom_level(self):
        logger = setup_logger('testLogger2', 'test2.log', logging.INFO)
        self.assertEqual(logger.level, logging.INFO)

    def test_log_file_creation(self):
        setup_logger('testLogger3', 'test3.log')
        self.assertTrue(os.path.exists('test3.log'))

class TestGradeSystem(unittest.TestCase):
    def setUp(self):
        self.gradesDict = {
            'Math': [80, 89, 93, -1, 84, 85, 74, 64],
            'Science': [94, 76, 88, 78, 88, 92, -1, 85],
            'English': [83, 76, 93, 96, 77, -1, 92, 60],
            'History': [96, 66, 76, 85, 78, 88, 69, -1]
        }
        self.gradeSystem = GradeSystem(self.gradesDict)

    def test_class_stats(self):
        avg, std = self.gradeSystem.class_stats('Math')
        expectedAVG = np.mean([grade for grade in self.gradesDict['Math'] if grade != -1])
        self.assertAlmostEqual(avg, expectedAVG, places = 2)

    def test_student_stats(self):
        studentGrades = [self.gradesDict[subject][0] for subject in self.gradesDict]
        validGrades = [grade for grade in studentGrades if grade != -1]
        expectedSTD = np.std(validGrades, ddof = 1)
        _, std = self.gradeSystem.student_stats(0)
        self.assertAlmostEqual(std, expectedSTD, places = 2)

    def test_check_students(self):
        self.gradeSystem.check_students()
        self.assertEqual(self.gradeSystem.gradesDF.isna().sum().sum(), 0)

    def test_grades_graph(self):
        try:
            self.gradeSystem.grades_graph('Math')
        except Exception as e:
            self.fail(f"grades_graph method failed with an exception: {e}")



if __name__ == '__main__':
    unittest.main()


## END.