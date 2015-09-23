__author__ = 'Julian'

# BIG-O NOTATION
# EXERCISE: Write two functions for finding the minimum element of a list. For the first function, compare each
# element to every other element in the list, so it will be O(N^2). For the second, find a way to make the algorithm
# operate in linear time, i.e. O(N)

# FUNCTION: findMin(numList)
# PURPOSE: finds minimum value in numList in quadratic, i.e. O(N^2), time
# INPUTS:
#   1) numList, list of numbers you want minimum of
# OUTPUTS:
#   1) minList, the minimum value of that list

import time
from random import randrange


def findMin(numList):
    minList = numList[0]

    for n in numList:
        isMin = True

        for m in numList:
            if n > m:
                isMin = False

        if isMin:
            minList = n

    return minList

print(findMin([5, 4, 2, 1, 0]))  # Returns: 0
print(findMin([1, 2, -200, 87000, 34]))  # Returns: -200

for listSize in range(1000, 10001, 1000):
    numList = [randrange(100000) for x in range(listSize)]
    start = time.time()  # Start time (in seconds)

    print(findMin(numList))

    end = time.time()  # End time (in seconds)

    print("Size: %d Time: %f" % (listSize, end-start))


# FUNCTION: findMin2(numList)
# PURPOSE: finds minimum value of numList in linear, i.e. O(N), time
# INPUTS:
#   1) numList, list of numbers you want minimum of
# OUTPUTS:
#   1) minList, the minimum value of that list

def findMin2(numList):
    # Set "minimum" value to first element of list
    minList = numList[0]

    # Loop through numList and update the minimum every time you find a smaller element
    for n in numList:
        if n < minList:
            minList = n

    return minList


for listSize in range(1000, 10001, 1000):
    numList = [randrange(100000) for x in range(listSize)]
    start = time.time()  # Start time (in seconds)

    print(findMin2(numList))

    end = time.time()  # End time (in seconds)

    print("Size: %d Time: %f" % (listSize, end-start))


# ANAGRAM DETECTION
# Compare algorithms for detecting whether two strings (assumed to be of equal length and containing only lowercase
# letters, for now) in terms of computation time

# METHOD 1: CHECKING OFF

# FUNCTION: checkoff(s1, s2)
# PURPOSE: implement "checking off" method to determine if s2 is an anagram of s2
# INPUTS:
#   1) s1, s2: the strings you want to check for "anagram-ness" (anagram-hood?)
# OUTPUTS:
#   1) anagram: Boolean indicating whether s2 is an anagram of s1
# RUNNING TIME: quadratic, O(N^2)

def checkoff(s1, s2):
    list2 = list(s2)  # Convert second string s2 to list
    anagram = True  # Boolean indicating whether s2 is an anagram of s1
    pos1 = 0  # Initialize position in first string s1 to 0

    # Loop through all elements of s1 until we find a character in s1 that is not in s2
    while pos1 < len(s1) and anagram:
        pos2 = 0  # Initialize position in s2 to 0
        found = False  # Boolean indicating whether s1[pos1] is in s2

        # Loop through all characters of s2 (via list2) until the desired element of s1 (s1[pos1])
        # is found or all characters of s2 have been searched
        while pos2 < len(list2) and not found:
            if s1[pos1] == list2[pos2]:
                found = True
            else:
                pos2 += 1

        # If s1[pos1] is found in s2, delete the corresponding element of s2 so it cannot be
        # double counted. Otherwise, s1 and s2 are not anagrams
        if found:
            list2[pos2] = None
        else:
            anagram = False

        pos1 += 1

    return anagram

print(checkoff("abcd", "dcba"))  # Returns: True
print(checkoff("dank", "tank"))  # Returns: False


# METHOD 2: SORT AND COMPARE

# FUNCTION: sortcompare(s1, s2)
# PURPOSE: checks if s1 and s2 are anagrams by sorting them alphabetically and comparing corresponding
# elements of the sorted lists
# INPUTS:
#   1) s1, s2: strings to be chekced
# OUTPUTS:
#   1) match: Boolean returning True is s1 and s2 are anagrams
# RUNNING TIME: O(Nlog(N)) or O(N^2) due to the calls to the list.sort() function

def sortcompare(s1, s2):
    # Convert strings s1 and s2 to lists
    list1 = list(s1)
    list2 = list(s2)

    # Sort lists
    list1.sort()
    list2.sort()

    j = 0  # Initialize counter j to 0
    match = True  # Returns True if strings are anagrams of each other

    # Iterate through all the (sorted) elements of list1 until the corresponding (sorted) element
    # in list2 is not found, or until we have checked all elements of list1
    while j < len(s1) and match:
        if list1[j] == list2[j]:
            j += 1
        else:
            match = False

    return match

sortcompare("gucci", "igucc")  # Returns: True
sortcompare("brochilldankster", "cheldarnlitbrosk")  # Returns: True


# METHOD 3: BRUTE FORCE
# Another method is to generate all possible strings using the characters from s1 and see if
# s2 is among them
# The problem is that this method is O(N!), which is hella slow


# METHOD 4: COUNT AND COMPARE
# Count up the frequencies of all 26 letters in each string and compare to see if they match

# FUNCTION: countcompare(s1, s2)
# PURPOSE: determine whether s1 and s2 are anagrams of each other by counting the frequency
# of each of the 26 letters in each string and comparing them to make sure they are equal
# INPUTS:
#   1) s1, s2: strings to check
# OUTPUTS:
#   1) anagram: Boolean retunring True if s1 and s2 are anagrams

def countcompare(s1, s2):
    # Intialize vectors of 26 zeroes representing the frequencies of each letter in s1 and s2
    count1 = [0]*26
    count2 = [0]*26

    # Calculates position of character s1[i] in alphabet string "abcdefghijklmnopqrstuvwxyz"
    # and increments appropriate frequency counter
    for i in range(len(s1)):
        j = ord(s1[i]) - ord("a")
        count1[j] += 1  #

    # Does the same for the second string s2
    for i in range(len(s2)):
        j = ord(s2[i]) - ord("a")
        count2[j] += 1

    j = 0  # Initialize new loop counter
    anagram = True  # Boolean returning True is s1 and s2 are anagrams, initialized to True

    # Check to see if s1 and s2 contain the same number of each of the 26 letters
    # Repeat until the entire alphabet has been checked or the counts don't add up
    while j < 26 and anagram:
        if count1[j] == count2[j]:
            j += 1
        else:
            anagram = False

    return anagram


print(sortcompare("gucci", "igucc"))  # Returns: True
print(sortcompare("brochilldankster", "cheldarnlitbrosk"))  # Returns: True

