__author__ = 'Julian'

# PROBLEM 1: Devise an experiment to verify that the list index operator is O(1)
import time


def indextest():
    l = list(range(N))

    for n in range(N):
        l.index(n)

from timeit import Timer

t1 = Timer("indextest()", "from __main__ import indextest")
print("concat ", t1.timeit(number=1000), "milliseconds")


# EXERCISE 4: Given a list of numbers in random order, write an algorithm that works in O(nlog(n))
# to find the kth smallest number in the list.

import numpy as np

# Creates list of 100 random numbers between -100 and 100
numlist = list(np.random.rand(100)*200 - 100)


def kMin(numlist, k):
    # Set "minimum" value to first element of list
    kmin = numlist[0:k]

    # Loop through numList and update the minimum every time you find a smaller element
    for n in numlist:
        if n < minlist:
            kmin = n

    return kmin