import unittest
from autompg import AutoMPG, AutoMPGData

car1 = AutoMPG('Amc', 'Pacer', 75, 15.0)
car2 = AutoMPG('Amc', 'Pacer', 76, 16.0)
car3 = AutoMPG('Subaru', 'Crosstrek', 94, 23.0)
car4 = AutoMPG('Amc', 'Pacer', 75, 15.0)
car5 = AutoMPG('Buick', 'Verano', 78, 15.9)
car6 = AutoMPG('Buick', 'Verano', 79, 15.9)


class TestAutoMPG(unittest.TestCase):
    """
    Tests various methods from AutoMPG class
        test_init : test attributes are created correctly
        test_str_repr : test print output of AutoMPG objects
        test_eq : test equality for 2 AutoMPG objects
        test_lt : test less than/greater than using all 4 attributes
        test_hash : test hash implementation
    """
    def test_init(self):
        self.assertEqual(car1.make, 'Amc')
        self.assertEqual(car1.model, 'Pacer')
        self.assertEqual(car1.year, 75)
        self.assertEqual(car1.mpg, 15)
        self.assertEqual(car2.year, 76)
        self.assertEqual(car3.mpg, 23)


    def test_str_repr(self):
        self.assertEqual(car1.__repr__(), 'AutoMPG(Amc, Pacer, 75, 15.0)')
        self.assertEqual(car1.__str__(), 'AutoMPG(Amc, Pacer, 75, 15.0)')
        self.assertEqual(car3.__repr__(), 'AutoMPG(Subaru, Crosstrek, 94, 23.0)')
        self.assertEqual(car3.__str__(), 'AutoMPG(Subaru, Crosstrek, 94, 23.0)')


    def test_eq(self):
        self.assertEqual(car1 == car2, False)
        self.assertEqual(car1 == car4, True)
        self.assertIsNone(car1 == 1)


    def test_lt(self):
        self.assertEqual(car1 < car2, True)
        self.assertEqual(car4 > car2, False)
        self.assertEqual(car4 < car2, True)
        self.assertEqual(car1 < car5, True)
        self.assertIsNone(car1 < 1)

    def test_hash(self):
        self.assertEqual(hash(car1) == hash(car4), True)
        self.assertEqual(hash(car5) == hash(car6), False)


class TestAutoMPGData(unittest.TestCase):
    """
    Tests various methods from AutoMPGData class
        test_data : checks data is created successfully
        test_data_value_attributes : the attributes of random AutoMPG objects
        within the AutoMPGData class
        test__iter : checks iterator was property created properly
    """
    def test_data(self):
        processed_autos = AutoMPGData()

        self.assertEqual(len(processed_autos.data), 398)
        self.assertEqual(processed_autos.data[0], \
                         AutoMPG('Chevrolet', 'Chevelle Malibu', 70, 18.0))
        self.assertEqual(processed_autos.data[-1], \
                         AutoMPG('Chevy', 'S-10', 82, 31.0))

    def test_data_value_attributes(self):
        processed_autos = AutoMPGData()
        self.assertEqual(processed_autos.data[100].make, 'Ford')
        self.assertEqual(processed_autos.data[125].model, 'Duster')
        self.assertEqual(processed_autos.data[150].year, 74)
        self.assertEqual(processed_autos.data[175].mpg, 29.0)

    def test__iter(self):
        processed_autos = AutoMPGData()
        self.assertEqual(type(processed_autos.__iter__()), type(iter(list())))


if __name__ == '__main__':
    unittest.main()






















