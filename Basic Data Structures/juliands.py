# CLASS: Stack
# PURPOSE: Implements a stack in Python
# METHODS:
#   1) isEmpty(), returns True is Stack is empty
#   2) push(item), adds item to top of Stack
#   3) pop(), returns item at top of Stack and removes it from the Stack
#   4) peek(), returns item at top of Stack without removing it
#   5) size(), returns number of items in Stack
# ATTRIBUTES:
#   1) items, list of elements stored in stack, where .items[0] is the bottom

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


# CLASS: RevStack
# PURPOSE: Implements a stack in reverse order
# METHODS:
#   1) isEmpty(), returns True is RevStack is empty
#   2) push(item), adds item to top of RevStack
#   3) pop(), returns item at top of RevStack and removes it from the RevStack
#   4) peek(), returns item at top of RevStack without removing it
#   5) size(), returns number of items in RevStack
# ATTRIBUTES:
#   1) items, list of elements in RevStack, with .items[0] corresponding to top of RevStack

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


# CLASS: Queue
# PURPOSE: Implement queue ADT (abstract data type)
# ATTIRBUTES:
#   1) items, list of elements in Queue
# METHODS
#   1) __init__(), class constructor
#   2) isEmpty(), returns True if Queue is empty
#   3) enqueue(item), adds item to "rear" (position 0) of Queue
#   4) dequeue(), removes element at "front" of Queue
#   5) size(), returns number of items inside Queue

class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# FUNCTION: revstring(str)
# PURPOSE: Uses Stack to reverse the characters in a string
# INPUTS:
#    1) str, string to be reversed
# OUTPUTS:
#    1) s, Stack containing characters of reversed string

def revstring(str):
    s = Stack()
    N = len(str)

    for j in range(0, N):
        s.push(str[N - (j+1)])

    return s


# FUNCTION: parcheck(str)
# PURPOSE: Checks a string for balanced parentheses
# INPUTS:
#    1) str, string you want to check
# OUTPUTS:
#    1) bal, Boolean returning True if str is balanced

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


# FUNCTION parcheck2(str)
# PURPOSE: Checks a string for balanced parentheses, brackets, and braces
# INPUTS:
#    1) str, string you want to check
# OUYTPUTS:
#    1) bal, Boolean returning True if symbols are balanced

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
# INPUTS:
#    1) str, string representing current right symbol
#    2) stk, Stack containing (heretofore unbalanced) left symbols
# OUTPUT:
#    1) match, Boolean indicating whether str and the top element of stk correspond

def parmatch(str, stk):
    match = False

    if str == ")" and stk.peek() == "(":
        match = True
    elif str == "]" and stk.peek() == "[":
        match = True
    elif str == "}" and stk.peek() == "{":
        match = True

    return match


# FUNCTION: divby2(decInt)
# PURPOSE: Implements divide-by-2 algorithm for converting decimals to binary
# INPUTS: decInt, positive integer in base 10
# OUTPUTS: binStr, string containing base 2 representation of decInt

def divby2(decInt):
    num = decInt;  # Initialize number to decimal you want to convert
    remStack = Stack()  # Stack containing remainders

    # Divide by 2 until all powers have been divided out
    while num >= 1:
        rem = num % 2
        remStack.push(int(rem))
        num = (num-rem)/2

    binStr = ""

    # Converts remStack into string variable containing binary representation of decInt
    while not remStack.isEmpty():
        binStr += str(remStack.pop())

    return binStr


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


# CLASS: Deque
# PURPOSE: Implement deque ("double-ended queue") ADT in Python; rear is at position 0
# ATTRIBUTES:
#   1) items, list of items contained in Deque
# METHODS:
#   1) __init__(): class constructor
#   2) isEmpty()
#   3) addFront(item): adds item to front of Deque; uses append() b/c adds to end of list
#   4) addRear(item): adds item to rear of Deque; uses insert() b/c rear is at position 0
#   5) removeFront(): removes item at front of Deque; uses pop() b/c defaults to removing final item
#   6) removeRear(): removes item at rear of Deque; uses pop(0) to specify removing element at position 0
#   7) size(): returns number of elements in list

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # Add item to front (end of list). Running time is O(1)
    def addFront(self, item):
        self.items.append(item)

    # Adds item to rear (position 0). Running time is O(N)
    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


# FUNCTION: palchecker(string)
# PURPOSE: Checks is a string is a palindrome
# INPUTS: string, string to be checked
# OUTPUTS: stillEqual, True is string is a palindrome

def palchecker(string):
    chardeque = Deque()

    for ch in string:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()

        if first != last:
            stillEqual = False

    return stillEqual


