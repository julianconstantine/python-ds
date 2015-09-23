__author__ = 'Julian'

# QUEUES
# Queues are ordered collections of elements where new elements are added to one end (the "rear")
# old elements are removed from the other (the "front")
# Queues maintain a "first-in, first-out" (FIFO) ordering property, aka "first-come, first-served"
# In comparison, Stacks are "last-in, first-out" (LIFO)


# CLASS: Queue
# PURPOSE: Implement queue ADT (abstract data type)
# ATTIRBUTES:
#   1) items, list of elements in Queue
# METHODS
#   1) __init__(), class constructor
#   2) isEmpty(), returns True if Queue is empty
#   3) enqueue(item), adds item to "rear" (position 0) of Queue
#   4) dequeue(), removes element at "front" of Queue
#   5) size(), returns number of items inside Queue

class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# Test it out!
q = Queue()
q.enqueue(4)
q.enqueue('Gucci')
q.enqueue('Nina')

print(q.items)  # Returns: ['Nina', 'Gucci', 4]

num = q.dequeue()  # Pops out 4, the first element in queue

print(q.items)  # Returns: ['Nina', 'Gucci']

q.size()  # Returns: 2


# THE JOSEPHUS PROBLEM – "HOT POTATO" SIMULATION
# Simulates a game oh hot potato!

# FUNCTION: josephus(names, num)
# PURPOSE: Calculates last person left in a game of "hot potato" from a list of names where the "potato" is
# passed around num times before a it stop and a player has to leave
# INPUTS: names, list of players; num, number of times "potato" is passed around before someone is eliminated
# OUTPUTS: Last player remaining

def josephus(names, num):
    q = Queue()

    # Enqueues all names in Queue
    for n in names:
        q.enqueue(n)

    while q.size() > 1:

        # Dequeues and enqueues players num times
        for i in range(num):
            q.enqueue(q.dequeue())

        # After num "passes" of the "potato," the last player is kicked out (dequeued)
        q.dequeue()

    return q.dequeue()

names = ['Barack', 'Angela', 'Shinzo', 'Vladimir',
         'David', 'François', 'Narendra', 'Jinping']

josephus(names, 5)


# PRINTER SIMULATION
# We want to simulate tasks being performed by a printer which several students have access over some period of time

# CLASS: Printer
# PURPOSE: Simulate printer queue
# ATTRIBUTES:
#   1) pagerate: pages printed per minute
#   2) currentTask: printing task
#   3) timeRemaining: representing time remaining until completion of all tasks
# METHODS:
#   1) __init__(ppm): class constructor; input pagerate attribute; outputs Printer object
#   2) tick(): decrements timer if currentTask is not completed and sets Printer to idle when finished
#   3) busy(): returns True if Printer is busy
#   4) startNext(newtask): initiates printing newtask and starts timer

class Printer:

    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            # If Printer is still busy, decrement timer by 1
            self.timeRemaining -= 1

            if self.timeRemaining <= 0:
                # If timer runs down to zero, set Printer to idle
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        # Starts newtask and adds rime required to perform it
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages()*60/self.pagerate


# CLASS: Task
# PURPOSE: Implements "printer task" object
# ATTIRBUTES:
#   1) timestamp: (integer?) time that Task was created and placed in Printer queue
#   2) pages: random integer between 1 and 20
# METHODS:
#   1) __init__(time): class constructor; input value for timestamp attribute
#   2) getStamp(): returns timestamp
#   3) getPages(): returns number of pages in Task object
#   4) waitTime(currenttime): returns amount of time the Task has spent waiting in queue


class Task:

    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


# FUNCTION: simulation(numSeconds, pagesPerMinute)
# PURPOSE:
# INPUTS:
#   1) numSeconds:
#   2) pagesPerMinute: pagerate for Printer object
# OUTPUTS: prints average wait time and number of tasks remaining

def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for s in range(numSeconds):
        if newPrintTask():
            task = Task(s)
            printQueue.enqueue(task)

        if not labprinter.busy() and not printQueue.isEmpty():
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(s))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)

    print('Average Wait %6.2f secs %3d tasks remaining.' % (averageWait, printQueue.size()))


# FUNCTION: newPrintTask()
# PURPOSE: simulates creation of new printing tasks (with probability 1/180 every time period)
# INPUTS: none
# OUTPUTS: Boolean indicating whether new Task object has been created

def newPrintTask():
    num = random.randrange(1, 181)

    if num == 180:
        return True
    else:
        return False

# RUN PRINTING SIMULATION
# The book wants you to consider additional modifications to this, but whatever.
# Maybe later.
import random

# Run simulation 10 times at 5 ppm
print("Run printing simulation for one hour at five pages per minute")
print("")

for i in range(10):
    simulation(3600, 5)

# Run simulation 10 times at 10 ppm
print("Run printing simulation for one hour at 10 pages per minute")
print("")
for i in range(10):
    simulation(3600, 10)


