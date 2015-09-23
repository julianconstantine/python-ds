__author__ = 'Julian'

# UNORDERED LISTS
# Unordered lists don't contain any Node objects, just a reference to the first (head) Node
# Nodes hold the "elements" of an unordered list and a reference to the next "element" (next Node)


# CLASS: Node
# PURPOSE: Implement node in Python
# ATTRIBUTES:
#   1) data, list item ("data field") inside the Node
#   2) next, reference to next Node in linked list
# METHODS:
#   1) __init__(initdata): class constructor; inputs object to be stored inside Node and sets next reference to None
#   2) getData(): returns object stored inside Node
#   3) getNext(): gets reference to next Node in list
#   4) setData(newdata): re-sets object stored inside Node to newdata
#   5) setNext(newnext): sets next reference to newnext

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    # Get element "inside" Node
    def getData(self):
        return self.data

    # Get "next" reference from Node
    def getNext(self):
        return self.next

    # Set element "inside" Node
    def setData(self, newdata):
        self.data = newdata

    # Set "next" reference for Node
    def setNext(self, newnext):
        self.next = newnext


# CLASS: UnorderedList
# PURPOSE: Implement unordered list in Python via linked lists
# ATTRIBUTES:
#   1) head:
# METHODS:
#   1) __init__(): class constructor
#   2) isEmpty(): returns True if list is empty
#   3) add(item): adds item to list by re-setting the head Node
#   4) remove(item): removes item from list by "disconnecting" its Node
#   5) append(item): adds item to end of the list
#   6) insert(index, item): inserts item at a given index
#   7) index(item): returns index of given item
#   8) pop(index=0): removes and returns item at given index, 0 is unspecified

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    # FUNCTION: add(item)
    # PURPOSE: Adds new item to the beginning of the list
    # INPUTS: item, element to be added to list
    # OUTPUTS: None

    def add(self, item):
        temp = Node(item)  # Creates temporary Node containing new element
        temp.setNext(self.head)  # Sets "next" reference of temporary Node to the original head Node
        self.head = temp  # Sets head Node of list to temporary Node

    # FUNCTION: size()
    # PURPOSE: Calculates number of elements in UnorderedList by "traversing" through each Node
    # and counting them until it reaches the end
    # INPUTS: None
    # OUTPUTS: count, number of elements in list

    def size(self):
        current = self.head
        count = 0

        # Increments counter variable until reaches end of the linked list
        while current != None:
            count += 1
            current = current.getNext()

        return count

    # FUNCTION: search(item)
    # PURPOSE: Searches for whether a given element is in the list
    # INPUTS: item, element you want to search for
    # OUTPUTS: found, True if item is in list

    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    # FUNCTION: remove(item)
    # PURPOSE: Removes element from list by traversing through each Node, then re-connecting the Node
    # "behind" the the Node containing the element to be removed to the Node "in front" of it
    # INPUTS: item, element to be removed
    # OUTPUTS: None

    def remove(self, item):
        current = self.head  # Initializes current Node to head Node
        previous = None  # Initializes previous Node to None
        found = False  # Initializes found to False

        # Traverses list until element to be removed is found
        while not found:
            # Sets found to True to break loop
            if current.getData() == item:
                found = True
            # Otherwise, sets current to next Node and stores current Node as previous
            else:
                previous = current
                current = current.getNext()

        # If element is in head Node, re-sets head Node to the next Node to delete the element
        if previous == None:
            self.head = current.getNext()
        # Otherwise, sets "next" reference in previous Node to "next" reference in current Node
        else:
            previous.setNext(current.getNext())

    # FUNCTION: append(item)
    # PURPOSE: Adds item to end of list
    # INPUTS:
    #   1) item: item you want to add to end of list
    # OUTPUTS: None

    def append(self, item):
        current = self.head

        while current.getNext() != None:
            current = current.getNext()

        current.setNext(Node(item))

    # FUNCTION: insert(index, item)
    # PURPOSE: Inserts an item into the list at a given index
    # INPUTS:
    #   1) item: item you want to insert
    #   2) index: position at which you want to insert it
    # OUTPUTS: None

    def insert(self, index, item):
        previous = None
        current = self.head

        temp = Node(item)
        position = 0

        # Traverse UnorderedList until the desired position is reached
        while position != index:
            position += 1
            previous = current
            current = current.getNext()

        # If index = 0, re-set the head Node
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        # Otherwise, "split and re-join" list by setting temp.next to current and previous.next to temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    # FUNCTION: index(item)
    # PURPOSE: Returns index of item in list
    # INPUTS:
    #   1) item, Node data field you want index of
    # OUTPUTS:
    #   1) position, index of item

    def index(self, item):
        current = self.head
        found = False
        position = 0

        while not found:
            position += 1

            if current.getData() == item:
                found = True

            current = current.getNext()

        return position

    # FUNCTION: pop(index=0)
    # PURPOSE: removes item in a given position (if unspecified, defaults to 0) and returns that item
    # INPUTS:
    #   1) index: position of item you want removed, default setting is 0
    # OUTPUTS:
    #   1) out: item in position index

    def pop(self, index=0):
        previous = None
        current = self.head

        position = 0

        while position != index:
            position += 1
            previous = current
            current = current.getNext()

        out = current.getData()

        if index == 0:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        return out


# Test it out!



