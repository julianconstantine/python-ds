__author__ = 'Julian'


# FILE: CLASSES.PY
# PURPOSE: Implement a Fraction class in Python

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


# FUNCTION: gcd(a, b)
# PURPOSE: Calculates greatest common divisor of two integers using the Euclidean Algorithm
# INPUTS: positive integers a and b
# OUTPUTS: integer n, re-assigned to be gcd of m and n

def gcd(a, b):
    p = a
    q = b

    while p % q != 0:
        r = p % q

        p = q
        q = r

    return q


# USING FRACTION OBJECTS
# The Fraction class and related functions are defined in the file Fraction.py

from classFraction import *

# Play around with all of this
f1 = Fraction(3, 5)
print(f1.num)  # Returns 3
print(f1.den)  # Returns 5

f1.show()  # Returns 3/5

# Two ways to convert Fractions to strings
# Both return '3/5'
str(f1)  # Original way
f1.__str__()  # New way via class method

f2 = Fraction(7, 8)

f3 = f1.__add__(f2)  # Adds f1 + f2 using new __add__ method

f3.show()  # Returns 59/40
f3.__str__()  # Returns '59/40'

# Overwriting the __add__ method for fraction objects also allows us to use the + operator
ff3 = f1+f2

# Same as f3
ff3.show()  # Returns 59/40
ff3.__str__()  # Returns '59/40'

# SIMPLIFYING FRACTIONS
gcd(20, 10)  # Returns 10


# INHERITANCE AND LOGIC GATES
