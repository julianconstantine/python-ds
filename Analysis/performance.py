__author__ = 'Julian'

# ALGORITHMIC PERFORMANCE OF PYTHON DATA STRUCTURES

# DATA STRUCTURE 1: LISTS
# Let list be a list of size N; i,j be indices; item be some element; and list1 and list2 be lists of
# size N and K and respectively

# OPERATION                 CODE                        EFFICIENCY
# Indexing                  list.index(item)            O(1) (constant)
# Index Assignment          list[i] = item              O(1) (constant)
# Appending                 list.append(item)           O(1) (constant)
# Popping                   list.pop()                  O(1) (constant)
#                           list.pop(i)                 O(N) (linear)
# Insertion                 list.insert(i, item)        O(N) (linear)
# Deletion                  del list[i]                 O(N) (linear)
# Iteration                                             O(N) (linear)
# Containment               item in list                O(N) (linear)
# Slicing (Get)             list[i:j]                   O(K) (linear)
#         (Del)             del list[i:j]               O(N) (linear)
#         (Set)             list[i:j] = list2           O(N+K) (linear)
# Reverse Sorting           list.reverse()              O(N) (linear)
# Concatenation             list1 + list2               O(K) (linear)
# Sorting                   list.sort()                 O(Nlog(N)) (log linear)
# Multiplication                                        O(NK) (quadratic)


# EXAMPLE: Four different ways to generate a list of 1000 numbers
# METHOD 1: Create list using concatenation
def test1():
    l = []

    for i in range(1000):
        l = l + [i]

    return l


# METHOD 2: Create list using append() function
def test2():
    l = []

    for i in range(1000):
        l.append(i)

    return l


# METHOD 3: Create list using "list comprehension"
def test3():
    l = [i for i in range(1000)]

    return l


# METHOD 4: Create list using range function and list constructor
# This doesn't work! In Python 3 the range() function became re-defined as the xrange() function from
# Python 2, so range() creates an ITERATOR, not a LIST
# But a tutorial I found online says this syntax should still worK?
# Maybe it's been updated further?

# I FIGURED IT OUT: I had already created an object called "list"
# So it thought I was referring to that object
# That's why this is a no-no!

def test4():
    l = list(range(1000))  # Doesn't work b/c range(1000) returns range(0, 1000) as output

    return l

from timeit import Timer

t1 = Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ", t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ", t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ", t4.timeit(number=1000), "milliseconds")

# There is more to these tests, using the "timeit" module, but I don't like them.
# It doesn't really do much for me. Whatever. :/


# DATA STRUCTURE 2: DICTIONARIES
# Let dict be a dictionary containing N key:value pairs

# OPERATION                 CODE                        EFFICIENCY
# Copying                   dict.copy()                 O(N) (linear)
# Getting                   dict.get(key); dict[key]    O(1) (constant)
# Setting                   dict[key] = value           O(1) (constant)
# Deletion                  del dict[key]               O(1) (constant)
# Containment               key in dict                 O(1) (constant)
# Iteration                 for key in dict             O(N) (linear)

