__author__ = 'Julian'

# Exercises

# EXERCISE 3: Implement the binary search using recursion without the slice operator. Recall that you will need to
# pass the list along with the starting and ending index values for the sublist. Generate a random, ordered list
# of integers and do a benchmark analysis.


# FUNCTION: binarySearch3()
# PURPOSE: Implement binary search algorithm recursively without using the slice operator
# INPUTS: xlist, ordered list to be sorted
# OUTPUTS: True if item is found, False if not

def binarySearch3(xlist, item, startpoint=0, endpoint=-1):
    # Initialize endpoint to -1, then re-set to the last position in the list
    if endpoint == -1:
        endpoint = len(xlist) - 1

    # End program if start and end-points converge to the same point and item is
    # not there
    if startpoint == endpoint and xlist[startpoint] != item:
        return False
    # Otherwise, keep calling the function recursively
    else:
        midpoint = (startpoint + endpoint)//2

        if xlist[midpoint] == item:
            return True
        else:
            if item < xlist[midpoint]:
                start = startpoint
                end = midpoint
            else:
                start = midpoint + 1
                end = endpoint

            return binarySearch3(xlist, item, start, end)


mylist = [1, 4, 5, 6, 89, 1337, 1000000000]
binarySearch3(mylist, item=7)  # Returns False

# Yaaaay my function works
mylist2 = [-11, -5.552, 1.05, 3, 4, 5, 6, 89, 99.9, 123.456, 1337, 1338]
binarySearch3(mylist2, item=123)  # Returns False
binarySearch3(mylist2, item=123.456)  # Returns True
binarySearch3(mylist2, item=-11)  # Returns True

# Now do the benchmark analysis
import random

for j in range(1000):
    jlist = random.sample(range(1000000), 100)
    # binarySearch3(jlist, )


# EXERCISE 4: Implement the len method (__len__) for the has table Map ADT.
# EXERCISE 5: Implement the in method (__contains__) for the has table Map ADT.

class HashTable4and5:
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

    def __getitem__(self, key):
        return self.get(key)

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


# EXERCISE 8: Implement quadratic probing as a rehashing technique

class HashTable8:
    def __init__(self, p):
        self.size = p  # Length of HashTable, must be prime!
        self.slots = [None]*self.size  # self.slots holds key values
        self.data = [None]*self.size  # self.data holds the data values

    # EXERCISE 8
    # Implement quadratic probing as a rehashing technique
    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        # If the input key hashes to an empty slot, store data there
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        # Otherwise, rehash
        else:
            # Replace
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                count = 0

                nextslot = self.rehash(hashvalue, len(self.slots), (count+1)**2)

                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    # Comment out the count += 1 incrementation statement to return to linear
                    # probing; then, gap will always be equal to (0+1)*2 = 1
                    count += 1

                    # Implement quadratic of linear probing based on the above
                    nextslot = self.rehash(hashvalue, len(self.slots), (count+1)**2)

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                # Otherwise, replace whatever is in the next slot
                else:
                    self.data[nextslot] = data

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size, gap):
        return (oldhash + gap) % size

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

    def __len__(self):
        return H.size

    def __contains__(self, item):
        return item in self.data

drgdfg


# EXERCISE 10: Implement the bubble sort using simultaneous assignment

# FUNCTION: bubbleSort10()
# PURPOSE: Implements bubble sort algorithm taking advantage of Python's simultaneous
# assignment capabilities
# RUNTIME: Quadratic, O(N^2)
# INPUTS: xlist, list to be sorted

def bubbleSort10(xlist):
    # Print original list
    print(xlist)

    for n in range(len(xlist)-1, 0, -1):
        for i in range(n):
            if xlist[i] > xlist[i+1]:
                # Using simultaneous assignment, we can replace:
                #   temp = a
                #   a = b
                #   b = temp
                # with the following:
                #   a, b = b, a
                # This will swap the values of a and b
                xlist[i], xlist[i+1] = xlist[i+1], xlist[i]

                # For learning purposes, print out the list each time we swap elements
                print(xlist)

mylist = [87000, 1, 4, 1337, 365.25, 12, 9, 128, 256, 64, 2048]

bubbleSort10(mylist)


# EXERCISE 12: Implement the selection sort using simultaneous assignment

# FUNCTION: selectionSort12()
# PURPOSE: Implement selection sort algorithm using simultaneous assignment
# RUNTIME: Quadratic, O(N^2), but typically faster than bubble sort
# INPUTS: xlist, a list of objects to be sorted in ascending order

def selectionSort12(xlist):
    # Iterate over every position in xlist
    for fillslot in range(len(xlist)-1, 0, -1):
        maxPosition = 0

        # Print original list
        print(xlist)

        # For every such position, sweep once through the sublist whose terminal position is the
        # current position of the loop
        for location in range(1, fillslot+1):
            printlist = False

            if xlist[location] > xlist[maxPosition]:
                maxPosition = location
                printlist = True

        # Swap the maximal element with the terminal element of the current sub-list using simultaneous
        # assignment instead of temporary variables
        xlist[fillslot], xlist[maxPosition] = xlist[maxPosition], xlist[fillslot]

        # For learning purposes, print the list each time it gets changed
        if printlist:
            print(xlist)

mylist = [87000, 1, 4, 1337, 365.25, 12, 9, 128, 256, 64, 2048]

selectionSort12(mylist)


# EXERCISE 14: Implement the mergeSort function without using the slice operaor

def mergeSort14(xlist):
    print("Splitting", xlist)

    # Split list and perform merge sort algorithm recursively until each sub-list is of length 1, in which
    # case, begin merging them

    if len(xlist) > 1:
        # Split (sub-)list into left and right halves
        mid = len(xlist)//2
        lefthalf = xlist[:mid]
        righthalf = xlist[mid:]

        # Recursively run mergeSort() on each half
        mergeSort(lefthalf)
        mergeSort(righthalf)

        # Initialize counters to zero
        i = 0
        j = 0
        k = 0

        # Iterate over the now-sorted left and right halves to merge them into a single
        # sorted super-list
        while i < len(lefthalf) and j < len(righthalf):

            if lefthalf[i] < righthalf[j]:
                xlist[k] = lefthalf[i]
                i += 1
            else:
                xlist[k] = righthalf[j]
                j += 1

            k += 1

        # If the left list is longer than the right list, iterate over all its remaining elements
        # to sort them into the new super-list
        while i < len(lefthalf):
            xlist[k] = lefthalf[i]
            i += 1
            k += 1

        # Alternatively, do the same for the right half of the list
        while j < len(righthalf):
            xlist[k] = righthalf[j]
            j += 1
            k += 1

        print("Merging", xlist)