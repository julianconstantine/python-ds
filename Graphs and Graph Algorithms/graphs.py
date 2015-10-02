__author__ = 'Julian'

# TWO WAYS TO STORE A GRAPH
#   1) Adjacency Matrix: Simple, but inefficient when "sparse" (which is usually the case)
#   2) Adjacency List: A list of dictionaries, one for each vertex v, which tells you the vertices that v is adjacent
#      to and the weights thereof


# CLASS: Vertex
# PURPOSE: Implement Vertex ADT(?) to make Graphs

class Vertex:
    # Class constructor, creates Vertex with specified id
    def __init__(self, key):
        self.id = key  # Name of Vertex
        self.connectedTo = {}  # Dictionary containing adjacent Vertices and their weights

    # Adds adjacent Vertex
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    # Prints out the list of Vertices adjacent to Vertex
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    # Returns name of Vertex
    def getConnections(self):
        return self.connectedTo.keys()

    # Returns weight of adjacent Vertex nbr
    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


# CLASS: Graph
# PURPOSE: Implement Graph ADT

class Graph:
    # Class constructor
    def __init__(self):
        self.vertList = {}  # Dictionary containing Vertices and their ids
        self.numVertices = 0  # Number of Vertices in the Graph

    # Adds Vertex to Graph with given id and returns the Vertex
    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex

        return newVertex

    # Returns Vertex if found (searches by key)
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    # Overwrites "in" keyword(?). Returns True is the Graph contains a Vertex with key 'n'
    def __contains__(self, n):
        return n in self.vertList

    # Creates a new edge by connecting Vertices f and t. If either f or t does not exist, it creates them first,
    # then connects them
    def addEdge(self, f, t, cost=0):

        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)

        self.vertList[f].addNeighbor(self.vertList[t], cost)

    # Returns list of (names of) Vertices
    def getVertices(self):
        return self.vertList.keys()

    # Overwrites the iter() function and returns an iterator over the Vertices
    def __iter__(self):
        return iter(self.vertList.values())


# Test it out!
g = Graph()

for i in range(6):
   g.addVertex(i)

g.vertList

g.addEdge(0, 1, 5)
g.addEdge(0, 5, 2)
g.addEdge(1, 2, 4)
g.addEdge(2, 3, 9)
g.addEdge(3, 4, 7)
g.addEdge(3, 5, 3)
g.addEdge(4, 0, 1)
g.addEdge(5, 4, 8)
g.addEdge(5, 2, 1)

for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))


# THE WORD LATTER PROBLEM
# The "word ladder puzzle" was invented in 1878 by Lewis Carroll. You started with one word (e.g. "fool") and then
# must transform it into another word (e.g. "sage") by changing one letter at a time. The catch is that every
# transformation must produce a real (English) word, so swapping the first 'o' in "fool" for an 'a' is illegal
# because 'faol' is not a real word

# We will solve this by turning the word ladder puzzle into a graph and then using "breadth first search"






