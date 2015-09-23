__author__ = 'Julian'
# NOTE: All function and class definitions can be found in the "juliands" python
# So you can just run the following whenever you re-open this file

from juliands import *

# The implementation of an abstract 'data type' is called a 'data structure'
# The best way to do such an implementation is to define a new class

# STACKS
# An ordered collection of elements elements where items are added/removed from one single end (the top)

# STACK IMPLEMENTATION
# The module "pythonds" has all of these implementations already done for you.
# TO DO THIS, RUN: from pythonds.basic.stack import Stack
# BUT I wrote my own version in the "jythonds" file

class Stack:
    def __init__(self):  # Initialize Stack
        self.items = []

    def isEmpty(self):  # Returns True if Stack is empty
         return self.items == []

    def push(self, item):  # Adds item to top of Stack
        self.items.append(item)

    def pop(self):  # Removes item at top of Stack
        return self.items.pop()

    def peek(self):  # Returns item at top of Stack without removing it
        return self.items[len(self.items)-1]

    def size(self):  # Returns number of items in the Stack
        return len(self.items)

# Now let's create a Stack object and play around
# NOTE: When running multiple lines of code (at least in the console), you must use the print() command
# Otherwise, it will only display the output of the last command you entered

s = Stack()  # Creates Stack object
print(s.isEmpty())  # Returns True
s.push(4)  # Adds 4 to top of Stack
s.push('doge')  # Adds 'doge' to top of Stack
print(s.peek())  # Returns 'doge' (element at top of the Stack)
s.push(True)
print(s.size())  # Returns 3 (length of Stack)
print(s.isEmpty())  # Returns False
s.push(8.4)  # Adds 8.4 to top of the Stack
print(s.pop())  # Returns 8.4 and removes it from the Stack
print(s.pop())  # Returns 'doge' and removes it from the Stack
print(s.size())  # Returns 1


# ALTERNATIVE STACK IMPLEMENTATION
# The top of the Stack is at the beginning, rather than the end
# Reverse order from before
# Call this data type the "RevStack" for "Reverse Stack"

class RevStack:
    def __init__(self):  # Initialize RevStack
        self.items = []

    def isEmpty(self):  # Returns True if RevStack is empty
        return self.items == []

    def push(self, item):  # Inserts item into RevStack and indexes it at position 0
        self.items.insert(0, item)

    def pop(self):  # Pops out item in position 0
        return self.items.pop(0)

    def peek(self):  # Displays item in position 0 without removing it
        return self.items[0]

    def size(self):  # Returns number of items in RevStack
        return len(self.items)

r = RevStack()
r.push('hello')  # Adds 'hello' to RevStack in position 0
r.push('true')  # Adds 'true' to RevStack in position 1
print(r.pop())  # Returns 'true' (pops out element at beginning, i.e. position 0)


# REVSTRING FUNCTION
# Want to write functions that uses a stack to reverse the characters in a string
# Pass-by-referenc is not a problem because strings are not mutable!

def revstring(str):
    s = Stack()
    N = len(str)

    for j in range(0, N):
        s.push(str[N - (j+1)])

    return s

revstring("Guccissimo").items
revstring("Nina Muñoz is awesome").items


# BALANCED PARENTHESES
# We can use Stacks to check whether the left and right parentheses in a string are balanced

def parcheck(str):
    s = Stack()
    bal = True

    for j in range(0, len(str)):
        if str[j] == "(":
            # Adds left parenthesis to the Stack when there is a left parenthesis in the string
            s.push("(")
        elif str[j] == ")":
            if s.isEmpty():
                # Sets bal = False if there is a terminal right parenthesis unbalanced by left parentheses
                bal = False
            else:
                # Pops out a left parenthesis if it finds a right parenthesis/the Stack is not empty
                s.pop()

    if not s.isEmpty():  # If the Stack is not empty, the parentheses are unbalanced
        bal = False

    return bal

# Test it out!
parcheck("()")  # True
parcheck("())")  # False
parcheck("(())")  # True
parcheck("(()")  # False
parcheck("111((qq)a")  # False
parcheck("111((qq)a)")  # True


# GENERALIZED BALANCED PARENTHESES
# Now we want balanced brackets, braces, and parentheses as well


# FUNCTION parcheck2(str)
# PURPOSE: Checks a string for balanced parentheses, brackets, and braces
# INPUTS: String str, the string you want to check
# OUYTPUTS: Boolean bal, True if symbols are balanced

def parcheck2(str):
    s = Stack()
    bal = True

    for j in range(0, len(str)):
        if str[j] in "([{":
            s.push(str[j])
        elif str[j] in ")]}":
            if s.isEmpty():
                bal = False
            else:
                if parmatch(str[j], s):
                    s.pop()

    if not s.isEmpty():
        bal = False

    return bal

# FUNCTION: parmatch(str, stk)
# PURPOSE: Checks to see whether the current (closing) right symbol matches the previous (opening) left symbol
# INPUTS: String str representing current right symbol; Stack object stk representing Stack of left symbols
# OUTPUT: Boolean match, indicates whether str and the top element of stk correspond

def parmatch(str, stk):
    match = False

    if str == ")" and stk.peek() == "(":
        match = True
    elif str == "]" and stk.peek() == "[":
        match = True
    elif str == "}" and stk.peek() == "{":
        match = True

    return match

parcheck2("(())")  # True
parcheck2("(())]")  # False
parcheck2("(([))]")  # False
parcheck2("[(([]))]")  # True
parcheck2("{((})]")  # False
parcheck2("[(({[]}))]")  # True


# CONVERTING DECIMALS TO BINARY
# This is mucho importante for computers
# Can use Stacks

# FUNCTION: DIVIDE-BY-2 ALGORITHM
# PURPOSE: Converts decimal to binary using Stacks
# INPUTS: decInt, positive integer in base 10
# OUTPUTS: binStr, string containing base 2 representation of decInt

def divby2(decInt):
    num = decInt;
    remStack = Stack()

    while num >= 1:
        rem = num%2
        remStack.push(int(rem))
        num = (num-rem)/2

    binStr = ""

    while not remStack.isEmpty():
        binStr += str(remStack.pop())

    return binStr

# Test it out
print(divby2(2))  # Returns 10
print(divby2(10))  # Returns 1010
print(divby2(16))  # Returns 10000
print(divby2(87))  # Returns 1010111


# GENERAL BASE CONVERTER
# Will only do bases up to 36 because we only have 26 letters and 10 numbers
# Pretty straightforward extension from base 2 converter

# FUNCTION: baseconvert(decInt, base)
# PURPOSE: Convert from base 10 to base b
# INPUTS:
#   1) decInt, a positive decimal integer
#   2) b, integer base to convert to, between 2-36
# OUTPUTS
#   1) baseStr, string containing digits in base b

def baseconvert(decInt, b):
    num = decInt
    remStack = Stack()
    # String containing symbols for representation up to base 36
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if int(b) != b or b < 2 or b > 36:
        print("ERROR: Please enter an integral base between 2 and 36")
    else:
        while num >= 1:
            rem = num % b
            remStack.push(int(rem))
            num = (num-rem)/b

        baseStr = ""

        while not remStack.isEmpty():
            # Only major difference from divide-by-2 algorithm
            # Adds corresponding letter/number from digits string instead of number in Stack
            baseStr += digits[remStack.pop()]

        return baseStr

# Test it out!
print(baseconvert(10, 9))  # Returns 10 base 9 = 11
print(baseconvert(867, 16))  # Returns 867 base 16 = 363
print(baseconvert(34, 2.67))  # Error, returns None (how do you make it return nothing?
print(baseconvert(29, 13))  # Returns 29 base 13 = 23
print(baseconvert(8, -4))  # Error, returns None
print(baseconvert(509, 16))  # Returns 509 base 16 = 1FD
print(baseconvert(1337, 10))  # Returns 1337 base 10 = 1337 :)
print(baseconvert(1311, 11))  # Returns 1311 base 11 = A92


# INFIX, PREFIX, AND POSFIX EXPRESSIONS
# Infix expressions are the ones we are used to using. They are ambiguous and require either parentheses or a
# pre-defined order of operations. Postfix and prefix expressions do not. They place operators after and before
# operands, respectively.

# EXAMPLE 1: A + BC + D
# Infix:    ((A + (B * C)) + D)
# Prefix:   + + A * B C D
# Postfix:  A B C * + D +

# EXAMPLE 2: (A + B)*(C + D)
# Infix:    ((A + B) * (C + D))
# Prefix:   * + A B + C D
# Postfix:  A B + C D + *

# EXAMPLE 3: AB + CD
# Infix:
# Prefix:   + * A B * C D
# Postfix:  A B * C D * +

# EXAMPLE 4: A + B + C + D
# Infix:
# Prefix:   + + + A B C D
# Postfix:  A B + C + D +


# FUNCTION: infixToPostfix(infix)
# PURPOSE: convert infix expression to postfix expression
# INPUTS:
#   1) infix: string containing infix expression to be converted; operators, operands, and parentheses must
#      be separated by spaces
# OUTPUTS:
#   2) postfix: string containing converted postfix expression

def infixToPostfix(infix):
    # Creates dictionary to hold order of operators ("precedence values") for infix expressions
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opstack = Stack()  # Stack for storing operators
    postfix = []  # Empty list for storing postfix expression

    for token in infix.split()
        # If token is a letter or number, append to postfix list
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix.append(token)
        # If token is a left parenthesis, append to operator Stack
        elif token == "(":
            opstack.push(token)
        # If token is a right parenthesis, pop operator Stack and add to postfix list until
        # you hit a left parenthesis
        elif token == ")":
            top = opstack.pop()

            while top != "(":
                postfix.append(top)
                top = opstack.pop()
        # Otherwise, pop the operator Stack and append to the postfix list until either the
        # operator Stack is empty or you run into an operator over which the token has precedence
        else:
            while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[token]):
                  postfix.append(opstack.pop())

            opstack.push(token)

    # Pop the operator Stack and add to postfix list until the Stack is empty
    while not opstack.isEmpty():
        postfix.append(opstack.pop())

    # Convert postfix list to string with list elements separated by blank spaces
    postfix = " ".join(postfix)

    return postfix

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A * B ) + C"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))


# FUNCTION: evalPostfix(postfix)
# PURPOSE: evaluates a postfix expression
# INPUTS:
#   1) postfix: string containing postfix expression to be evaluated
# OUTPUTS:
#   1) out: output of evaluated postfix expression

def evalPostfix(postfix):
    operand = Stack()  # Creates operand Stack

    for token in postfix.split():
        # If token is a number, convert it to an integer and push to operand Stack
        if token in "0123456789":
            operand.push(int(token))
        # Otherwise, token must be an operator, so pop the operand Stack twice and
        # evaluate the expression A OPERATOR B using the operandMath() function then
        # push result to operand Stack
        else:
            A = operand.pop()
            B = operand.pop()
            evalAB = operandMath(token, A, B)
            operand.push(evalAB)

    # Pop final result of operand Stack
    out = operand.pop()

    return out


# FUNCTION: operandMath(operator, A, B)
# PURPOSE: evaluate a single binary operator expression "A operator B"
# INPUTS:
#   1) A, B: operand numbers
#   2) operator: operator string
# OUTPUTS:
#   1) "A operator B" evaluated

def operandMath(operator, A, B):

    if operator == "*":
        return A*B
    elif operator == "/":
        return A/B
    elif operator == "+":
        return A+B
    elif operator == "-":
        return A-B
    elif operator == "^":
        return A**B


# Test it out!
print(evalPostfix("3 2 +"))  # Returns: 5
print(evalPostfix("7 8 + 3 2 + /"))  # Returns: 0.3333333333333333
print(evalPostfix("2 4 ^"))


# PRACTICE PROBLEMS
# 1) Convert 10 + 3 * 5 / (16 - 4) to a postfix expression
# CORRECT:      10 3 5 * 16 4 - / +
# INCORRECT:    10 3 5 16 4 - * / +
# The infix expression of the incorrect version is 10 + 5 * (16 - 4) / 3 because
# we have to evaluate everything from left to right without any assumed precedence

# 2) Evaluate 17 10 + 3 * 9 /
# The infix version is (17 + 10) * 3 / 9
# This evaluates to 27*3/9 = 9

# 3) Convert 5 * 3 ^ (4 - 2) to a postfix expression
# The postfix expression is    5 3 4 2 - ^ *
# This time, all the operators do come at the end





