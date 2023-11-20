## START:
"""
Unit tests for the autompg.py module.
"""

import os
import unittest
from autompg import AutoMPG, AutoMPGData



class TestAutoMPG(unittest.TestCase):
    """
    Test cases for the AutoMPG class.
    """

    def setUp(self):
        """
        Set up the test data for each test case.
        """

        self.car1 = AutoMPG("Toyota", "Corolla", 1980, 30.5)
        self.car2 = AutoMPG("Toyota", "Corolla", 1980, 30.5)
        self.car3 = AutoMPG("Honda", "Civic", 1981, 32.4)


    def test_repr(self):
        """
        Test the __repr__ method.
        """

        self.assertEqual(repr(self.car1), "AutoMPG('Toyota', 'Corolla', 1980, 30.5)")


    def test_str(self):
        """
        Test the __str__ method.
        """

        self.assertEqual(str(self.car1), "Toyota Corolla (1980) - 30.5 mpg")


    def test_eq(self):
        """
        Test the __eq__ method.
        """

        self.assertEqual(self.car1, self.car2)
        self.assertNotEqual(self.car1, self.car3)


    def test_lt(self):
        """
        Test the __lt__ method.
        """

        self.assertTrue(self.car1 < self.car3)
        self.assertFalse(self.car3 < self.car1)
        # Both cars are equal
        self.assertFalse(self.car1 < self.car2)


    def test_hash(self):
        """
        Test the __hash__ method.
        """

        # As car1 and car2 are equal, they should have the same hash
        self.assertEqual(hash(self.car1), hash(self.car2))
        self.assertNotEqual(hash(self.car1), hash(self.car3))



class TestAutoMPGData(unittest.TestCase):
    """
    Test cases for the AutoMPGData class.
    """

    def setUp(self):
        """
        Set up the test data for each test case.
        """

        # Provide the path to your test file
        self.data = AutoMPGData('auto-mpg.data.txt')


    def test_data_loaded(self):
        """
        Test that data is correctly loaded into the AutoMPGData class.
        """

        # Ensuring data is loaded
        self.assertTrue(len(self.data.data) > 0)
        # Checking if the loaded data is of AutoMPG type
        self.assertIsInstance(self.data.data[0], AutoMPG)


    def test_clean_file_creation(self):
        """
        Test that the clean file is correctly created by the _clean_data method.
        """

        cleanFilePath = 'auto-mpg.clean.txt'
        self.assertTrue(os.path.exists(cleanFilePath))


    def test_iter(self):
        """
        Test the __iter__ method to ensure it returns an iterator of AutoMPG objects.
        """

        for car in self.data:
            self.assertIsInstance(car, AutoMPG)



if __name__ == "__main__":
    unittest.main()


## END.