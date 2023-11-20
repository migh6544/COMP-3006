## START:


import unittest
from homework9 import Distributions, NumpyDistribution



class TestDistributions(unittest.TestCase):
    """
    Test suite for the Distributions class.

    This class tests the functionality of the Distributions class including creation of instances with both valid and invalid parameters,
    correct generation of distributions, and the string representation method.
    """


    def test_normal_distribution_valid(self):
        """
        Test the normal distribution with valid parameters.
        """

        normalDist = Distributions(dist = "normal", mean = 0, std = 1, samples = 100)
        self.assertEqual(normalDist.distribution, "normal")
        self.assertEqual(len(normalDist.data), 100)


    def test_lognormal_distribution_valid(self):
        """
        Test the lognormal distribution with valid parameters.
        """

        lognormalDist = Distributions(dist = "lognormal", mean = 0, std = 1, samples = 100)
        self.assertEqual(lognormalDist.distribution, "lognormal")
        self.assertEqual(len(lognormalDist.data), 100)


    def test_laplace_distribution_valid(self):
        """
        Test the Laplace distribution with valid parameters.
        """

        laplaceDist = Distributions(dist="laplace", mean = 0, std = 1, samples = 100)
        self.assertEqual(laplaceDist.distribution, "laplace")
        self.assertEqual(len(laplaceDist.data), 100)


    def test_distribution_invalid_parameters(self):
        """
        Test distributions with invalid parameters.
        """

        with self.assertRaises(ValueError):
            Distributions(dist = "normal", mean = "invalid", std = 1, samples = 100)
        with self.assertRaises(ValueError):
            Distributions(dist="lognormal", mean = 0, std = -1, samples = 100)
        with self.assertRaises(ValueError):
            Distributions(dist="laplace", mean = 0, std = 1, samples = "Invalid")


    def test_invalid_distribution_type(self):
        """
        Test with an invalid distribution type.
        """

        with self.assertRaises(ValueError):
            Distributions(dist = "Invalid Distribution", mean = 0, std = 1, samples = 100)


    def test_str_method(self):
        """
        Test the __str__ method of the Distributions class.
        """

        normalDist = Distributions(dist = "normal", mean = 0, std = 1, samples = 100)
        expectedStr = "Distributions(Type: normal, Mean: 0, Std: 1, Size: 100)"
        self.assertEqual(str(normalDist), expectedStr)



class TestNumpyDistribution(unittest.TestCase):
    """
    Test suite for the NumpyDistribution class.

    This class tests the functionality of the NumpyDistribution class including creation of instances with both valid and invalid parameters,
    correct generation of distributions, and the string representation method.
    """

    def test_valid_numpy_distributions(self):
        """
        Test NumpyDistribution with valid parameters for different distributions.
        """

        validDists = [('normal', 0, 1), ('lognormal', 0, 1), ('laplace', 0, 1)]
        for distName, mean, std in validDists:
            with self.subTest(distName = distName):
                numpyDist = NumpyDistribution(distName, mean, std, size = 100)
                self.assertEqual(numpyDist.distribution, distName)
                self.assertEqual(len(numpyDist.data), 100)


    def test_invalid_numpy_distribution_type(self):
        """
        Test NumpyDistribution with an invalid distribution type.
        """

        with self.assertRaises(ValueError):
            NumpyDistribution('Invalid Distribution', 0, 1, size = 100)


    def test_invalid_parameters_numpy(self):
        """
        Test NumpyDistribution with invalid parameters.
        """

        with self.assertRaises(TypeError):
            NumpyDistribution('normal', 'invalid', 1, size = 100)
        with self.assertRaises(ValueError):
            NumpyDistribution('lognormal', 0, -1, size = 100)


    def test_str_method_numpy(self):
        """
        Test the __str__ method of the NumpyDistribution class.
        """

        numpyDist = NumpyDistribution('normal', 0, 1, size = 100)
        expectedStr = "NumpyDistribution(Type: normal | (Mean, Std): (0, 1) | Sample: {'size': 100})"
        self.assertEqual(str(numpyDist), expectedStr)



if __name__ == '__main__':
    unittest.main()


## END.