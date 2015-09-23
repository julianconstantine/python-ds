__author__ = 'Julian'

# CLASS: Fraction
# PURPOSE: Creates data type representing rational numbers
# ATTRIBUTES:
#   1) Numerator (num)
#   2) Denominator (den)
# METHODS:
#   1) Class Constructor: Fraction(p,q)
#   2) Show: .show() prints the fraction p/q
#   3) String: str(frac) converts Fraction object frac to a string


class Fraction:

    # METHOD: __init__()
    # PURPOSE: Class constructor
    # INPUTS: None
    # OUTPUTS: None
    # NOTE: This is the first method implemented by any class. It always is written as __init__
    #       self is a special parameter. It must always be listed first in definitions, but need
    #       not be specified in calls. Instead, create Fractions by doing f = Fraction(p,q)

    def __init__(self, p, q):
        self.num = p  # Creates numerator attribute
        self.den = q  # Creates denominator attribute

    # METHOD: show()
    # PURPOSE: Prints Fraction object to screen as p/q
    # INPUTS: None
    # OUTPUTS: None

    def show(self):
        print(self.num, '/', self.den, sep='')

    # METHOD: __str__()
    # PURPOSE: Converts Fraction(p,q) object to string 'p/q'
    # INPUTS: None
    # OUTPUTS: String self.num/self.den
    # NOTE: This overrides the default __str__ method and str() function for Fraction objects

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    # METHOD: __add__(other)
    # PURPOSE: Adds two Fractions and simplifies
    # INPUTS: Fraction other
    # OUTPUTS: Simplified sum of self + other
    # NOTE: This overwrites the __add__ method and + operator for Fraction objects

    def __add__(self, other):
        a = self.num
        b = self.den
        c = other.num
        d = other.den

        p = a*d + b*c
        q = b*d

        return Fraction(p//gcd(p, q), q//gcd(p, q))

    # METHOD: __sub__(other)
    # PURPOSE: Subtracts two Fractions and simplifies
    # INPUTS: Fraction other
    # OUTPUTS: Simplified difference of self - other
    # NOTE: This overwrites the __sub__ method and - operator for Fraction objects

    def __sub__(self, other):
        a = self.num
        b = self.den
        c = other.num
        d = other.den

        p = a*d - b*c
        q = b*d

        return Fraction(p//gcd(p, q), q//gcd(p, q))

    # METHOD: __mul__(other)
    # PURPOSE: Multiplies two Fractions and simplifies
    # INPUTS: Fraction other
    # OUTPUTS: Simplified product of self*other
    # NOTE: This overwrites the __mul__ method and * operator for Fraction objects

    def __mul__(self, other):
        a = self.num
        b = self.den
        c = other.num
        d = other.den

        p = a*c
        q = b*d

        return Fraction(p//gcd(p, q), q//(gcd(p, q)))

    # METHOD: __truediv__(other)
    # PURPOSE: Divides two Fractions and simplifies
    # INPUTS: Fraction other
    # OUTPUTS: Simplified quotient of self*other
    # NOTE: This overwrites the __div__ method and / operator for Fraction objects

    def __truediv__(self, other):
        a = self.num
        b = self.den
        c = other.num
        d = other.den

        p = a*d
        q = b*c

        return Fraction(p//gcd(p, q), q//gcd(p, q))

    # METHOD: __eq__(other)
    # PURPOSE: Compare two Fractions for equality-by-value
    # INPUTS: Fraction other
    # OUTPUTS: Boolean returning true if two Fractions are equal by value
    # NOTE: If we just have frac1 == frac2, we only get True when frac1 and frac2 are references to the same object
    #       This is called "shallow equality" (equality-by-reference). We re-write the __eq__ method to make it
    #       indicate "deep equality" (equality-by-value).

    def __eq__(self, other):
        x1 = self.num*other.den
        x2 = self.den*other.num

        return x1 == x2

    # METHOD: __lt__(other)
    # PURPOSE: Less-than-by-value operator for Fraction class
    # INPUTS: Fraction other
    # OUTPUTS: Boolean returning true if self < other by-value
    # NOTE: Replaces < operator for Fraction class

    def __lt__(self, other):
        x1 = self.num/self.den
        x2 = other.den/other.den

        return x1 < x2

    # METHOD: __gt__(other)
    # PURPOSE: Greater-than-by-value operator for Fraction class
    # INPUTS: Fraction other
    # OUTPUTS: Boolean returning true if self > other by-value
    # NOTE: Replaces > operator for Fraction class

    def __gt__(self, other):
        x1 = self.num/self.den
        x2 = other.den/other.den

        return x1 > x2
