__author__ = 'Julian'


# FUNCTION: binarySearch()
# PURPOSE: Implements binary search algorithm on ordered list
# RUNTIME: O(log(N) (Logarithmic)
# INPUTS:
#   1) xlist, ordered list to be searched
#   2) item, item you want to find
# OUTPUT: found, Boolean indicating if item is in xlist

# Binary searching is a "divide-and-conquer" algorithm, b/c it splits the problem (finding an item) into many
# smaller subproblems, solves the subproblems, then re-assembles them at the end to find the solution to the
# larger problem

def binarySearch(xlist, item):
    first = 0
    last = len(xlist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2

        if xlist[midpoint] == item:
            found = True
        else:
            if item < xlist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found

testlist = [1, 3, 18, 87, 89, 100, 1337, 200000]

binarySearch(testlist, 13)  # Returns False
binarySearch(testlist, 1337)  # Returns True


# FUNCTION: binarySearch2()
# PURPOSE: Implement binary search using recursive calls every time the item is not found
# RUNTIME: O(Log(N), in theory, but using the split operator : in Python is O(k), so this is not
# strictly true
# INPUTS:
#   1) xlist, ordered list to be searched
#   2) item, item you want to find
# OUTPUT: True if item is in xlist, otherwise False

def binarySearch2(xlist, item):
    if len(xlist) == 0:
        return False
    else:
        midpoint = len(xlist)//2

        if xlist[midpoint] == item:
            return True
        else:
            if item < xlist[midpoint]:
                return binarySearch2(xlist[:midpoint], item)
            else:
                return binarySearch2(xlist[midpoint+1:], item)


testlist = [1, 3, 18, 87, 89, 100, 1337, 200000]

# Output is same as before!
binarySearch2(testlist, 13)  # Returns False
binarySearch2(testlist, 1337)  # Returns True