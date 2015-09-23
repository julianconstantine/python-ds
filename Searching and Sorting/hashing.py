__author__ = 'Julian'

# HASHING
# Allows us to build a data structure that can be searched in O(1) (constant) time!
# Basically, the idea is to create a function (a hash function) which for each item calculate some value
# that tells you "where" (i.e. which index) the item is at.
# Hashed items are stored in a slot in hash table

# EXAMPLE #1: The "Remainder" Method
# Say you have a vector of size m. Define h(x) := x mod m
# Then, item x will be stored in position x % m, starting from 0

# Say you want to store x = (44, 1, 5, 23, 67) (m = 5)

# h(44) = 44 mod 5 = 4
# h(1) = 1 mod 5 = 1
# h(5) = mod 5 = 0
# h(23) = 23 mod 5 = 3
# h(67) = 67 mod 5 = 2

# So h(x) = (5, 1, 67, 23, 44) (ignore the parentheses. This isn't a tuple)


# EXAMPLE #2: Collisions
# What if you want to store x = (45, 1, 5, 23, 67)?

# PROBLEM: h(45) = 0 AND h(5) = 0.

# #5 and 45 get mapped to the same index because h is not one-to-one. This is called a "collision."

# A one-to-one hash function is called a "perfect" has function. Clearly, we won't always have this
# luxury. One way to avoid collisions is to have a bigger hash table (so things are less likely to
# "bump into each other"), but then we start to lose the gains in efficiency of a has function, which
# was why we used it in the first place.

# So we want to have some kind of back-up method when collisions do occur, which is called "collision resolution"


# EXAMPLE #3: The Folding Method
# (1) Divide the item into equal-sized pieces (except the very last piece)
# (2) Add the numerical value (or some derived numerical value) of the pieces together
# (3) Take the remainder modulo the size of your hash table

# Consider phone numbers: (630) 696-7024 and (847) 254-4190 (bae)

# Break up into three-digit pieces and sum:
# h(6306967024) = (630 + 696 + 702 + 4) mod 11 = 2032 mod 11 = 8
# h(8472544190) = (847 + 254 + 419 + 0) mod 11 = 1620 mod 11 = 3

# So we store my number in positions 8 and Nina's in position 3


# EXAMPLE #4: The Folding Method, using Ordinal Values
# Extends folding methods to strings
# (1) Break up a string into its constituent letters
# (2) Calculate the ordinal value (what is this???) of each and su
# (3) Take the remainder modulo the size of your has table

# Consider strings "Julian" and "Nina"

# Break up into individual letters and sum:
# h("Julian") = (ord("J") + ord("u") + ord("l") + ord("i") + ord("a") + ord("n")) mod 11
#             = (74 + 117 + 108 + 105 + 97 + 110) mod 11 = 611 mod 11
# h("Julian") = 6

# h("Nina") = (ord("N") + ord("i") + ord("n") + ord("a")) mod 11
#           = (78 + 105 + 110 + 97) mod 11 = 390 mod 11
# h("Nina") = 5

# NOTE: Anagrams will always map to the same value with this method!
# One way around this is to use the position of the character as a weight.


# Here is a functional definition of this method:
def ordinalHash(hashString, tableSize):
    sum = 0

    for j in range(len(hashString)):
        sum += ord(hashString[j])

    return sum % tableSize

print(ordinalHash("Julian", 11))  # Returns 6
print(ordinalHash("Nina", 11))  # Returns 5
print(ordinalHash("Matt Matt", 11))  # Returns 8


# IMPLEMENTING THE MAP ABSTRACT DATA TYPE
# A Map is an unordered collection of associations between a key and a data value

# CLASS: HashTable
# PURPOSE: Implement the Map ADT
# ATTRIBUTES:
#   1) size: Number of key:value pairs, MUST BE PRIME
#   2) slots: List holding keys
#   3) data: List holding values
# METHODS:
#   1) __init__(p): Class constructor, creates HashTable of prime size p
#   2) put(key, data): Stores data object in HashTable at position calculated by key
#   3) hashfunction(key, size): Calculates hashvalue for data to be stored by key
#   4) rehash(oldhash, size): Re-calculates hashvalue in event of a collision
#   5) get(key): Returns item corresponding to a given key value
#   6) __getitem__(key): Overwrites getitem() with user-defined get() function
#   7) __setitem__(key, data): Overwrites setitem() with user-defined put() function

class HashTable:
    def __init__(self, p):
        self.size = p  # Length of HashTable, must be prime!
        self.slots = [None]*self.size  # self.slots holds key values
        self.data = [None]*self.size  # self.data holds the data values

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        #
        else:
            # Replace
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))

                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(hashvalue, len(self.slots))

                if self.slot[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                # Otherwise, replace whatever is in the next slot
                else:
                    self.data[nextslot] = data

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))

                if position == startslot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        return self.put(key, data)


# Test it out!
H = HashTable(23)











