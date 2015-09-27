__author__ = 'Julian'

# PROBLEM 4
# Implement the len method (__len__) for the has table Map ADT.

# PROBLEM 5
# Implement the in method (__contains__) for the has table Map ADT.


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
#   8) __len__(): Extends len() operator to HashTable class
#   9) __contains__(item): Extends containment ("in") operator to HashTable class

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

                if self.slots[nextslot] == None:
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

    # Overrides [] operator to our get() function when using it to access values
    def __getitem__(self, key):
        return self.get(key)

    # Overrides [] operator to our put() function when using it to assign values
    def __setitem__(self, key, data):
        return self.put(key, data)

    # PROBLEM 4: Implement the len method (__len__) for the has table Map ADT.
    # Without this, to get the size of H, you have to do H.size; now, you can do len(H).
    def __len__(self):
        return H.size

    # PROBLEM 5: Implement the in method (__contains__) for the has table Map ADT.
    # Without this, you have to do item in H.data; now, you can do item in H
    def __contains__(self, item):
        return item in self.data
