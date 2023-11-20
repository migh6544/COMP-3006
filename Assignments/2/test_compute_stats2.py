# Import the unittest module for writing and running test cases
import unittest
# Import the compute_stats function from compute_stats2 module
from compute_stats2 import compute_stats


# Define a test class that inherits from unittest.TestCase
class TestComputeStats(unittest.TestCase):

    # Test with a list containing an even number of elements
    def test_even_number_of_elements(self):
        data = [1.0, 2.0, 3.0, 4.0]
        result = compute_stats(data)
        self.assertEqual(result, (1.0, 4.0, 2.5, 2.5))

    # Test with a list containing an odd number of elements
    def test_odd_number_of_elements(self):
        data = [1.0, 2.0, 3.0]
        result = compute_stats(data)
        self.assertEqual(result, (1.0, 3.0, 2.0, 2.0))

    # Test with an empty list (should return None for all values)
    def test_empty_list(self):
        data = []
        result = compute_stats(data)
        self.assertIsNone(result)

    # Test with a list containing a single element (all values should be the same)
    def test_single_element_list(self):
        data = [5.0]
        result = compute_stats(data)
        self.assertEqual(result, (5.0, 5.0, 5.0, 5.0))


# Entry point of the program
if __name__ == '__main__':
    # Run the tests when the script is executed directly
    unittest.main()