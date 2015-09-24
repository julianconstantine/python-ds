__author__ = 'Julian'

# BUBBLE SORT
# The bubble sort algorithm "sweeps" through a list, compares adjacent elements pairwise, and swaps them if they are
# not in order. The "sweeps" then repeat until all the elements are sorted (in ascending order, here)

# A bubble sort is often considered the most inefficient sorting method since it must exchange items
# before the final location is known.


# FUNCTION: bubbleSort(xlist)
# PURPOSE: Implement bubble sort algorithm
# RUNTIME: Quadratic, O(N^2)
# INPUTS: xlist, list to be sorted in ascending order

def bubbleSort(xlist):
    for n in range(len(xlist)-1, 0, -1):
        for i in range(n):
            if xlist[i] > xlist[i+1]:
                temp = xlist[i]
                xlist[i] = xlist[i+1]
                xlist[i+1] = temp

xlist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

bubbleSort(xlist)
print(xlist)  # Returns: [17, 20, 26, 31, 44, 54, 55, 77, 93]


# SHORT BUBBLE SORT
# If during a "sweep" no swapping occurs, then the list must be sorted. We can modify the bubble sort
# algorithm to take advantage of this

def shortBubbleSort(xlist):
    exchanges = True
    n = len(xlist) - 1

    while n > 0 and exchanges:
        exchanges = False

        for i in range(n):
            if xlist[i] > xlist[i+1]:
                exchanges = True
                temp = xlist[i]
                xlist[i] = xlist[i+1]
                xlist[i+1] = temp

        n -= 1


xlist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]

shortBubbleSort(xlist)
print(xlist)  # Returns: [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]


# SELECTION SORT
# Improves on bubble sort by making only one exchange during every "sweep" of the items to be sorted.
# On each pass, the selection sort algorithm searches for the largest element and then puts it in
# its proper place.
# But selection sort is still O(N^2), and we require N-1 passes to sort N items.

# FUNCTION: selectionSort(xlist)
# PURPOSE: Implement selection sort algorithm
# RUNTIME: Quadratic, O(N^2), but typically faster than bubble sort
# INPUTS: xlist, a list of objects to be sorted in ascending order

def selectionSort(xlist):
    # Iterate over every position in xlist
    for fillslot in range(len(xlist)-1, 0, -1):
        maxPosition = 0

        # For every such position, sweep once through the sublist whose terminal position is the
        # current position of the loop
        for location in range(1, fillslot+1):
            if xlist[location] > xlist[maxPosition]:
                maxPosition = location

        # Swap the maximal element with the terminal element of the current sublist
        temp = xlist[fillslot]
        xlist[fillslot] = xlist[maxPosition]
        xlist[maxPosition] = temp


xlist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

selectionSort(xlist)
print(xlist)  # Returns: [17, 20, 26, 31, 44, 54, 55, 77, 93]


# INSERTION SORT
# Insertion sort is another O(N^2) algorithm, but it functions differently from bubble sort or selection sort.
# Insertion sort maintains an ordered sub-list in the lower portions of the list, then inserts each new item into
# its proper (sorted) position in the sub-list. Again, we have N-1 passes to sort N items.

def insertionSort(xlist):
    # Sweep through entire list.
    for index in range(1, len(xlist)):
        current = xlist[index]
        position = index

        # Compare each element to all elements before it and "bump" elements "up one" until
        # the current element is in its proper (sorted) place
        while position > 0 and xlist[position - 1] > current:
            xlist[position] = xlist[position - 1]
            position -= 1

        xlist[position] = current

        # Print out list during every sweep of insertion sort (for demonstration)
        # print(xlist)

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

insertionSort(alist)
print(alist)  # Returns: [17, 20, 26, 31, 44, 54, 55, 77, 93]


# SHELL SORT
# Shell sort, aka "decreasing increment sort," improves on insertion sort by breaking the main list
# into several sub-lists, each of which is sorted via insertion sort. The sub-lists are creating using
# a "gap" number N, which chooses all items that are N units apart.
# You think of a standard insertion short as being a shell sort with gap number N = 1.

def shellSort(xlist):
    sublistcount = len(xlist)//2

    while sublistcount > 0:

        for start in range(sublistcount):
            gapInsertionSort(xlist, start, sublistcount)

        print("After increments of size", sublistcount, "the list is", xlist)

        sublistcount //= 2


def gapInsertionSort(xlist, start, gap):

    for i in range(start+gap, len(xlist), gap):
        current = xlist[i]
        position = i

        while position >= gap and xlist[position - gap] > current:
            xlist[position] = xlist[position - gap]
            position -= gap

        xlist[position] = current


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

shellSort(alist)
print(alist)

# All of the above returns:
# After increments of size 4 the list is [20, 26, 44, 17, 54, 31, 93, 55, 77]
# After increments of size 2 the list is [20, 17, 44, 26, 54, 31, 77, 55, 93]
# After increments of size 1 the list is [17, 20, 26, 31, 44, 54, 55, 77, 93]
# [17, 20, 26, 31, 44, 54, 55, 77, 93]
