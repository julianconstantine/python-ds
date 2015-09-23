__author__ = 'Julian'

# FILE: STRFORMAT.PY
# PURPOSE: Learn string print formatting in Python

# The default separator in the print() command is a single space
# So these two both return Hello World
print('Hello World')
print('Hello', 'World')

# Can use multiple arguments
# Returns Hello World, Whats Gucci?
print('Hello', 'World,', 'Whats', 'Gucci?')

print('Hello', 'World', sep='***')  # Returns Hello***World
print('Hello', 'World', end='***')  # Returns Hello World*** but something with the end command messes this up

name = 'Nina'
age = 22

# This prints Nina is 22 years old.
print(name, 'is', age, 'years old.')

# We can do this using the STRING FORMAT OPERATOR (%)
# This also prints Nina is 22 years old.
print('%s is %d years old.' % (name, age))

# STRING FORMATTING CONVERSION CHARACTERS
# The letter after the % operator indicates the type of variable to be converted
#   1) Integer: b, c, d, i, o, x, X, n, None
#      I.    b   base 2 (this gives an error for some reason)
#      II.   c   converts to unicode character
#      III.  d   base 10
#      IV.   i   same as d?
#      V.    o   base 8
#      VI.   x   base 16, using 'abcdef'
#      VII.  X   base 16, using 'ABCDEF'
#      VIII. n   "number," same as d but adds in number separator characters (commas?)
#
#      None is the same as d
#   2) Unsigned integer: u
#   3) Floating point: f, e, E, g
#      I.    e   "m.dddddde+/-x"
#      II.   E   "m.ddddddE+/-x"
#      III.  f   "m.dddddd"
#      IV.   F   "m.dddddd" (same as f)
#      V.    g   "general" (uses some formula for automatically calculating what the best(?) formatting is)
#      VI.   G   "general" (same as g, but uses E instead of e)
#      VII.  n   "number" (same as g, but includes number separator characters)
#      VIII. %   "percentage" (multiples by 100 and then uses f and adds a % sign)
#
#      None is the same as f
#   4) Single character: c
#   5) String: s, None
#      I. s formats a string or any variable that can be cast to a string using the str() command
#      II. None is the same as s, when your variable is a string
#   6) Literal % character: %

# Integers
print('%s is %b years old.' % (name, age))  # This gives an error for some reason :(
print('%s is %o base 8 years old.' % (name, age))  # Nina is 26 base 8 years old.
print('%s is %X base 16 years old.' % (name, age))  # Nina is 16 base 16 years old.

# Floating Points
# NOTE: type(age) = int, but using floating point format operators automatically converts it to a float
print('%s is %f years old.' % (name, age))  # Nina is 22.000000 years old.
print('%s is %e years old.' % (name, age))  # Nina is 2.200000e+01 years old.
print('%s is %g years old.' % (name, age))  # Nina is 22 years old.

# Speed of light (big numbers
c = 299792458
units = 'm/s'

print('The speed of light is %g %s.' % (c, units))  # The speed of light is 2.99792e+08 m/s.
print('The speed of light is %n %s.' % (c, units))  # This gives an error :(
print('The speed of light is %d %s.' % (c, units))  # The speed of light is 299792458 m/s.
print('The speed of light is %f %s.' % (c, units))  # The speed of light is 299792458.000000 m/s.
print('The speed of light is %g %s.' % (c, units))  # The speed of light is 2.99792e+08 m/s.
print('The speed of light is %X %s.' % (c, units))  # The speed of light is 11DE784A m/s.


# STRING FORMATTING OPTIONS
# Will use 20 as a stand-in for any general number and d or f as stand-ins for any general format operator
#   1) Number: %20d, puts base 10 integer in a centered field of width 20
#   2) Left-Justify: %-20d, puts base 10 integer in a left-justified field of width 20
#   3) Right-Justify: %+20d, puts base 10 integer in a right-justified field of width 20
#   4) Zero: %020d, puts base 10 integer in a centered field of width 20, filled in with leading zeroes
#   5) Decimal: $20.2f, puts floating point in a field of 20 characters, with 2 numbers after the decimal point
#   6) Key: %(name)d, gets value supplied by a dictionary, using name as a key

