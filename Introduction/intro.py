__author__ = 'Julian'

# BUILT-IN COLLECTION DATA TYPES
# Contain multiple elements

# BUILT-IN COLLECTION DATA TYPE #1: LISTS
# SYNTAX: [a, b, c, d, ...] (comma-delimited values enclosed in square brackets)
# Ordered collection of zero or more heterogeneous references to Python data objects
# Lists are MUTABLE
type([1, 4, True, "Gucci"])  # Returns "list"


# SEQUENCE OPERATORS (FOR LISTS, STRINGS, AND TUPLES)
# Defined for any sequentially ordered data type (including lists)
#   1) Indexing "foo[i]": accesses ith element of foo
#   2) Concatenation "a + b": adds the elements of b onto the end of a
#   3) Repetition "foo*N": concatenates foo with itself N times
#   4) Membership "x in foo": asks whether item x is anywhere in sequence foo
#   5) Length "len(foo)": returns number of elements in sequence foo
#   6) Slicing "foo[i:j]": returns elements i through j-1 of the sequence foo

mylist = ['a', 'B', 4, 27, 'gucci']

print(mylist[0])  # Returns 'a'
print(mylist + ['dank'])  # Returns ['a', 'B', 4, 27, 'gucci', 'dank']
print(mylist[1:4]*3)  # Returns ['B', 4, 27, 'B', 4, 27, 'B', 4, 27]. Note: repetition does not multiply the numbers!
print(27 in mylist)  # Returns True
print(len(mylist*3))  # Returns 15


# LIST METHODS (LIST)
# Functions defined for list objects
#   1) Append: list.append(item), adds item to end of list
#   2) Insert: list.insert(j, item), sets list[j] equal to item
#   3) Pop: list.pop(), removes and returns last element of list
#   4) Pop: list.pop(j), removes and returns list[j]
#   5) Sort: list.sort(), sorts list
#   6) Reverse Sort: list.reverse(), sorts list in reverse order
#   7) Delete (by index): del list[j], deletes jth element and "moves everything else down one index"
#   8) Index: list.index(item), returns index of item in list
#   9) Count: list.count(item), counts number of times item appears in list
#   10) Remove (by item): list.remove(item), removes first occurence of item (like "del")

myList = [1024, 3, True, 6.5]

myList.append(False)  # Adds False to end of myList
print(myList)  # Returns [1024, 3, True, 6.5, False]

myList.insert(2, 4.5)  # Replaces myList[2] (third element) with 4.5
print(myList)  # Returns [1024, 4.5, True, 6.5, False]

print(myList.pop())  # Returns False
print(myList)  # Returns [1024, 3, 4.5, True, 6.5]

print(myList.pop(1))  # Removes second element, returns 3
print(myList)  # Returns [1024, 4.5, True, 6.5]

myList.pop(2)  # Removes third element, returns True
print(myList)  # Returns [1024, 4.5, 6.5]

myList.sort()  # Sorts elements in increasing order (all are numeric types, so this makes sense)
print(myList)  # Returns [4.5, 6.5, 1024]

myList.reverse()  # Sorts in decreasing order
print(myList)  # Returns [1024, 6.5, 4.5]

print(myList.count(6.5))  # Returns 1
print(myList.index(4.5))  # Returns 2

myList.remove(6.5)  # Removes 6.5 from myList
print(myList)  # Returns [1024, 4.5]

del myList[0]  # Deletes element 0 (first element)
print(myList)  # Returns [4.5] (Note: this is a list containing 4.5, not 4.5 itself)


# BUILT-IN COLLECTION DATA TYPE #2: STRINGS (STR)
# SYNTAX: 'abcd...'
# Sequential collection of zero or more letters, numbers, and other symbols
# All of these are called CHARACTERS
# Strings are IMMUTABLE
type('Guccissimo')  # Returns str

# STRING METHODS
#   1) Center: str.center(w), returns a string centered in a field of size w
#   2) Count: str.count(item), returns number of occurences of item in str
#   3) Left Justify: str.ljust(w), returns a string left-justified in a field of size w
#   4) Lowercase: str.lower(), converts all letters in string to lowercase
#   5) Right Justify: str.rjust(w), returns a string right-justified in a field of size w
#   6) Find: str.find(item), returns index of item in str
#   7) Split: str.split(schar), splits into two substrings at schar and deletes 'schar'

myStr = 'Guccius grammaticam transcendit'

myStr.center(5)  # Returns original string b/c field is not wide enough
len(myStr)  # Returns 31

myStr.center(50)  # Returns '         Guccius grammaticam transcendit          '
myStr.ljust(50)  # Returns 'Guccius grammaticam transcendit                   '

myStr.lower()  # Returns 'guccius grammaticam transcendit'

myStr.count('a')  # Returns 4 b/c there are four a's in 'Guccius grammaticam transcendit'

myStr.find('tra')  # Returns 20, the index where 'tra' begins
myStr[20]  # Returns 't'

myStr.split('gram')  # Returns ['Guccius ', 'maticam transcendit']
myStr.split(' ')  # Returns ['Guccius', 'grammaticam', 'transcendit']

myStr[0] = '27'  # Returns an error b/c strings are IMMUTABLE


# BUILT-IN COLLECTION DATA TYPE #3: TUPLES
# SYNTAX: (a, b, c, d, ...) (comma-delimited heterogeneous elements enclosed by parentheses)
# Tuples are IMMUTABLE (they are essentially immutable versions of lists)
myTuple = (6, 27, True, 'Gucci')
type(myTuple)

len(myTuple)  # Returns 4
print(myTuple[0])  # Returns 6

# Note: * does not multiply anything elementwise with tuples! (Not like vectors in MATLAB!)
# Returns (6, 27, True, 'Gucci', 6, 27, True, 'Gucci', 6, 27, True, 'Gucci')
print(myTuple * 3)

print(myTuple[0:2])  # Returns (6, 27), a "sub-tuple"

myTuple[0] = 'Dank'  # Gives an error


# BUILT-IN COLLECTION DATA TYPE #4: SETS
# SYNTAX: {a, b, c, d, ...} (comma-delimited heterogeneous elements enclosed by braces)
# Heterogeneous unordered (i.e. NOT sequential) collection of values

# SET OPERATORS
#   1) Membership: "x in S" returns True if x is an element of the set S
#   2) Length: "len(S)" returns the cardinality of S
#   3) Union: "A | B}" returns the union of A and B
#   4) Intersection: "A & B" returns in the intersection of A and B
#   5) Difference: "A - B" returns A not B
#   6) Containment: "A <= B" returns True is A is contained within B
A = {1, 2, 'bytch', 1337}
B = {1, 2, 4, 5, 1337}
type(A)  # Returns set

print(A | B)  # Returns {1, 2, 4, 5, 1337, 'bytch'}
print(A & B)  # Returns {1337, 2, 1}
print(A - B)  # Returns {'bytch'}

# SET METHODS
#   1) Union: A.union(B), returns the union of sets A and B
#   2) Intersection: A.intersection(B), returns the intersection of A and B
#   3) Difference: A.difference(B), returns A not B
#   4) Containment: A.issubset(B), returns True if A is a subset of B
#   5) Add: S.add(item), adds item to set S
#   6) Remove: S.remove(item), removes item from set S
#   7) Pop: S.pop(), removes arbitrary element from set S
#   8) Clear: S.clear(), removes all elements from set S

# I'm going to skip examples because this is easy


# BUILT-IN COLLECTION DATA TYPE #5: DICTIONARIES
# SYNTAX: {key1: value1, key2: value2, ...} (comma-delimited key:value pairs enclosed by braces)
# They're basically like lists, but indexed by user-defined keys rather than (only) ordered numbers
# But dictionaries have NO SPECIFIC ORDER W/RT THE KEYS
capitals = {'Iowa': 'Des Moines', 'Illinois': 'Springfield', 'New York': 'Albany', 1: 'wtfh4x??'}

print(capitals[1])  # Returns wtfh4x??
print(capitals['New York'])  # Returns Albany

# To add a new key: value pair, the syntax is
capitals['California'] = 'Sacramento'

print(len(capitals))  # Returns 5, b/c California/Sacramento has been added


# This will return all the states/capitals (key:value pairs)
# If we include terminal spaces in "is the capital of", we get extra spaces in the final printout
# This little loop shows how dictionaries are indexed
# Dang this is awesome
for k in capitals:
    print(capitals[k], "is the capital of", k)

# DICTIONARY OPERATORS
#   1) Get: "dict[key]" returns the value associated with key
#   2) Membership: "key in dict" returns True if key is in the dictionary dict
#   3) Delete: "del dict[key]" deletes the key:value pair from dict

telext = {'david': 1410, 'brad': 1137}

print(telext['david'])  # Returns 1410
print('brad' in telext)  # Returns True
del telext['brad']  # Removes 'brad': 1137 pair
print(telext)  # Returns {'david': 1410}

# DICTIONARY METHODS
#   1) Keys: "dict.keys()" returns a dict_keys object that has all the keys in dict
#   2) Values: "dict.values()" returns a dict_values object that has all the values in dict
#   3) Items: "dict.items()" returns a dict_items object containing all the key:value pairs
#   4) Get: "dict.get(key)" returns value associated with key; otherwise returns None
#   5) Get: "dict.get(key, alt)" returns value associated with key; otherwise returns alt

telext = {'david': 1410, 'brad': 1137}

telext.keys()  # Returns dict_keys(['brad', 'david'])
type(telext.keys())  # Returns dict_keys
list(telext.keys())  # Returns ['brad', 'david']

telext.values()  # Returns dict_values([1137, 1410])
type(telext.values())  # Returns dict_values
list(telext.values()) # Returns [1137, 1410]

telext.items()  # Returns dict_items([('brad', 1137), ('david', 1410)])

list(telext.items())  # Returns [('brad', 1137), ('david', 1410)]

telext.get('kent')  # Returns nothing
telext.get('kent')  # Returns None

telext.get('kent', 'NO ENTRY')  # Returns 'NO ENTRY'

