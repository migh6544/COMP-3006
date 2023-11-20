## START:
class Base:
    """
    Base Class: Represents the foundational class for derived classes.

    Attributes:
        baseAttr (str): An attribute specific to the base class.
    """

    def __init__(self, baseAttr):
        """
        Constructor for Base class.

        Args:
            baseAttr (str): The attribute to initialize the Base object with.
        """

        self.baseAttr = baseAttr

    def __str__(self):
        """Returns a string representation of the Base class object."""

        return (f"Base Class with Base attribute = {self.baseAttr}")

    def base_method(self):
        """
        A method specific to the Base class.

        Returns:
            str: A message indicating this method belongs to Base.
        """

        return ("This is the base method.")


class Derived(Base):
    """
    Derived Class: Inherits from Base class and has additional functionality.

    Attributes:
        baseAttr (str): An overridden attribute specific to the derived class.
        derivedAttr (str): A new attribute added in the derived class.
    """

    def __init__(self, baseAttr, derivedAttr):
        """
        Constructor for Derived class.

        Args:
            baseAttr (str): The attribute related to the base class.
            derivedAttr (str): The attribute specific to the derived class.
        """

        super().__init__(baseAttr)
        # Overriding the baseAttr for a unique representation in Derived class.
        self.baseAttr = (f"Derived: {baseAttr}")
        self.derivedAttr = derivedAttr

    def __str__(self):
        """Returns a string representation of the Derived class object."""

        return (f"Derived Class with Base attribute = {self.baseAttr}, Derived Attribute = {self.derivedAttr}")

    def base_method(self):
        """
        Overridden method from the Base class.

        Returns:
            str: A message indicating this method is overridden in Derived.
        """

        return ("This method is overridden in the Derived class.")
## END.