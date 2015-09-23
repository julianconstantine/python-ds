__author__ = 'Julian'

# DEQUES ("DOUBLE-ENDED QUEUES")
# Allows items to be added or removed at BOTH the front or the rear
# Provides all capabilities of Stacks AND Queues in a single data structure


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

d = Deque()
print(d.isEmpty())
d.addRear(4)  # Adds 4o to position 0
d.addRear("dog")  # Adds "dog" to position 0, bumps 4 to position 1
d.addFront("cat")  # Adds "cat" to position 2
d.addFront(True)  # Adds True to position 3

# Returns: ['dog', 4, 'cat', True]
print(d.items)

print(d.size())  # Returns: 4
print(d.isEmpty())  # Returns: False

d.addRear(8.4)  # Adds 8.4 to position 0 and bumps everything else up one position

# Returns: [8.4, 'dog', 4, 'cat', True]
print(d.items)

# Both of these return None
print(d.removeRear())
print(d.removeFront())

# Returns: ['dog', 4, 'cat']
print(d.items)


# PALINDROME CHECKER
# Deques can be used to check if a string is a palindrome

# FUNCTION: palchecker(string)
# PURPOSE: Checks is a string is a palindrome
# INPUTS: string, string to be checked
# OUTPUTS: stillEqual, True is string is a palindrome

def palchecker(string):
    d = Deque()

    for ch in string:
        d.addRear(ch)

    stillEqual = True

    while d.size() > 1 and stillEqual:
        first = d.removeFront()
        last = d.removeRear()

        if first != last:
            stillEqual = False

    return stillEqual

# Test it out!
print(palchecker("lsdkjfskf"))  # Returns False
print(palchecker("radar"))  # Returns True
print(palchecker("amanaplanacanalpanama"))  # Returns True

