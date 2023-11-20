## START:
import unittest
from BaseDerived import Base, Derived

class TestBaseDerivedClasses(unittest.TestCase):
    """
    Unit test suite for testing the Base and Derived classes.

    The class inherits from unittest.TestCase which provides utility methods for assertions and test setups.
    """

    def test_base_class(self):
        """
        Test case for validating functionalities of the Base class.

        This method creates an instance of the Base class and checks its attributes and methods
        for expected behavior.
        """

        # Instantiate an object of the Base class
        baseObject = Base("BaseValue")

        # Check if the attribute 'baseAttr' is set correctly
        self.assertEqual(baseObject.baseAttr, "BaseValue", "baseAttr of Base class is not set correctly.")

        # Validate the string representation of the Base class object
        self.assertEqual(str(baseObject), "Base Class with Base attribute = BaseValue", "String representation of Base class is not as expected.")

        # Validate the behavior of the base_method of Base class
        self.assertEqual(baseObject.base_method(), "This is the base method.", "base_method of Base class is not returning the expected value.")

    def test_derived_class(self):
        """
        Test case for validating functionalities of the Derived class.

        This method creates an instance of the Derived class and checks its attributes and methods
        for expected behavior, including overridden behavior from the Base class.
        """

        # Instantiate an object of the Derived class with values for both base and derived attributes
        derivedObject = Derived("BaseValue", "DerivedValue")

        # Check if the attributes 'baseAttr' and 'derivedAttr' are set correctly
        self.assertEqual(derivedObject.baseAttr, "Derived: BaseValue", "baseAttr of Derived class is not overridden/set correctly.")
        self.assertEqual(derivedObject.derivedAttr, "DerivedValue", "derivedAttr of Derived class is not set correctly.")

        # Validate the string representation of the Derived class object
        expectedStr = "Derived Class with Base attribute = Derived: BaseValue, Derived Attribute = DerivedValue"
        self.assertEqual(str(derivedObject), expectedStr, "String representation of Derived class is not as expected.")

        # Validate the overridden behavior of the base_method in Derived class
        self.assertEqual(derivedObject.base_method(), "This method is overridden in the Derived class.", "base_method of Derived class is not returning the overridden value.")


if __name__ == "__main__":
    unittest.main()
## END.