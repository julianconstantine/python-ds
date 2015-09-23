__author__ = 'Julian'

# EXCEPTION HANDLING
# When an exception occurs, it has been "raised"
# You "handle" the exception by using a try statement

# TYPES OF ERRORS
#   1) Syntax: programmer has made a mistake in the structure of a statement or expression
#   2) Logic: program executes but gives wrong result

# EXAMPLE: Square Roots
import math

num = int(input("Please enter an integer "))

try:
    print(math.sqrt(num))
except:
    print("Bad value for square root")
    print("Using absolute value instead")
    print(math.sqrt(abs(num)))

# EXAMPLE 2: Runtime Errors
# Alternatively, you can use the raise command to have a user-defined "runtime error"
num = int(input("Please enter an integer "))

if num < 0:
    raise RuntimeError("You can't use a negative number")
else:
    print(math.sqrt(num))


