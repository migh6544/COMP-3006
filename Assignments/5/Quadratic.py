## START:
class QuadraticEquation:
    """
    Represents a quadratic equation in the form ax^2 + bx + c = 0.

    Attributes:
        a (int): Coefficient of x^2 term.
        b (int): Coefficient of x term.
        c (int): Constant term.
    """

    def __init__(self, a: int, b: int, c: int) -> None:
        """
        Initializes a QuadraticEquation with given coefficients.

        Args:
            a (int): Coefficient of x^2 term.
            b (int): Coefficient of x term.
            c (int): Constant term.
        """

        # Coefficient of x^2 term
        self.a = a
        # Coefficient of x term
        self.b = b
        # Constant term
        self.c = c

    def __repr__(self) -> str:
        """
        Returns a formal string representation of the QuadraticEquation.

        Returns:
            str: A string like 'QuadraticEquation(a=1, b=-3, c=2)'.
        """

        return (f"QuadraticEquation(a={self.a}, b={self.b}, c={self.c})")


    def __str__(self) -> str:
        """
        Returns a string representation of the quadratic equation.

        This method constructs the equation string based on the coefficients of
        the quadratic equation and formats it to match common mathematical representation.

        Returns:
            str: A string like 'x^2 - 3x + 2 = 0'.
        """

        # Handle the x^2 term:
        # For coefficient values of 1 and -1, just represent as x^2 and -x^2 respectively. Otherwise, represent as ax^2.
        if self.a == 1:
            equationString = "x^2"
        elif self.a == -1:
            equationString = "-x^2"
        else:
            equationString = f"{self.a}x^2"

        # Handle the x term:
        # For coefficient values of 1 and -1, represent as +x and -x. For positive coefficients, represent as +bx and for negative as -bx.
        if self.b == 1:
            equationString += " + x"
        elif self.b == -1:
            equationString += " - x"
        elif self.b > 0:
            equationString += f" + {self.b}x"
        elif self.b < 0:
            equationString += f" - {-self.b}x"

        # Handle the constant term:
        # For positive constants, represent as +c and for negative as -c.
        if self.c > 0:
            equationString += f" + {self.c}"
        elif self.c < 0:
            equationString += f" - {-self.c}"

        # Append the equal sign to complete the equation representation.
        equationString += " = 0"

        return equationString


    def discriminant(self) -> float:
        """
        Computes and returns the discriminant of the equation.

        Returns:
            float: The discriminant value.
        """

        # Discriminant formula: b^2 - 4ac
        return float((self.b ** 2) - (4 * (self.a * self.c)))

    def roots(self):
        """
        Computes and returns the roots of the equation.

        Returns:
            float: Single root as root
            tuple: Two roots as (root1, root2).

        Raises:
            ValueError: If no real roots exist.
        """

        # Handling the linear case where a = 0
        if self.a == 0:
            if self.b == 0:
                if self.c == 0:
                    raise ValueError("The equation is always true for all x.")
                else:
                    raise ValueError("The equation has no solution.")
            return float(-self.c / self.b)

        # Calculate the discriminant
        D = self.discriminant()

        # Based on discriminant value, determine the nature and number of roots
        if D < 0:
            # No real roots if discriminant is negative
            raise ValueError("Discriminant is negative: No real roots.")
        elif D == 0:
            # Single root if discriminant is zero
            root = ((-self.b) / (2 * self.a))
            return root
        else:
            # Two distinct roots if discriminant is positive
            root1 = (((-self.b) + (D ** 0.5)) / (2 * self.a))
            root2 = (((-self.b) - (D ** 0.5)) / (2 * self.a))
            return (root1, root2)
## END.