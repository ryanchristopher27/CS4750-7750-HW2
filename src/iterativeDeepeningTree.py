# Contains Iterative Deepening Tree Search Algorithm

# Contains Iterative Deepening Tree Search Algorithm

#each Node in the tree is a room in the grid

# from asyncio.windows_events import NULL
from collections import deque
from shutil import move
from tracemalloc import start

from vacuum import Vacuum

#replaces the vac class - just for my own understanding
class MapInfo(object):
    def __init__(self, vac):
        self.map = vac.map 
        self.startingLoc = vac.startingLoc
        self.dirtyRooms = findDirtyRooms(vac.map)
        

#compares two graph points for equality
def comparePoints(first, second):

    x = first[0]
    y = first[1]

    a = second[0]
    b = second[1]

    if(x == a and y == b):
        return True
    else:
        return False

# iterates through the room and finds all the dirty rooms and put them in the dirty room. 
# array 2x the size of the amount of dirty rooms: x,y
# Pass in map from vacuum object
# Return array of dirty rooms in map
def findDirtyRooms(map):

    dirtyRooms = []
    for i in range(4):
        for j in range(5):
            if(map[i][j] == 1):
                dirtyRooms.append([i, j])

    return dirtyRooms




#Iterative depth Node
#Stores less information than the original node
class Node(object):

    def __init__(self, value, depth, parent):
        self.children = []
        self.value = value #value = [x, y]
        self.depth = depth
        self.parent = parent

    #determines if node is a part of a cycle
    def isCycle(self):
        startingPoint = self
        tracer = self
        while tracer.parent != None:
            if(comparePoints(tracer.parent.value, startingPoint.value)):
                return True
            tracer = tracer.parent
        return False

    #returns the path from the root to the node
    def getPath(self):
        path = []
        tracer = self
        for i in range(self.depth + 1):
            path.insert(0, tracer.value)
            tracer = tracer.parent
        return path

    #expands the node for it's possible children
    #does not allow for children to be added if outside of the bounds
    def expand(self):
        x = self.value[0]
        y = self.value[1]

        left = (x-1, y)
        right = (x+1, y)
        down = (x, y+1)
        up = (x, y-1)

        points = (left, right, up, down)

        for point in points:
            if (point[0] in range(4)) and (point[1] in range(5)): 
                self.children.append(Node(point, self.depth + 1, self))



#Depth limiting search
#Returns False for cutoff, None of no solution
#returns the path from root to node if found
def depthLimitedSearch(mapInfo, depth):
    
    frontier = deque() #LIFO
    dirtyRooms = mapInfo.dirtyRooms #list of dirty rooms
    startingLoc = mapInfo.startingLoc
    result = None #initial result


    frontier.append(Node(startingLoc, 0, None)) #appending the staring node
    
    while len(frontier) > 0: #while the frontier is not empty

        node = frontier.pop()

        for room in dirtyRooms: #checks if current node is a dirty room
            if(comparePoints(room, node.value)):
                return node.getPath()

        if node.depth > depth:
            result = False

        # if the current node isn't in a cylce, expand the current node and append it's children to the frontier
        elif (node.isCycle() == False): 
            node.expand()
            for child in node.children:
                frontier.append(child)
        
    return result #if you never find the solution, retun no solution

def interativeDeepeningSearch(mapInfo):
    depth = 0
    while(True): #go forever...
        result = depthLimitedSearch(mapInfo, depth)
        if(result != False): #if it isn't the cutoff
            return result
        depth += 1 #increment depth

#find the best solution for a given vaccum
#finds the first best solution, then the next best solution, and so forth using iterative deepening search to find the next best solution 
def findSolution(vac):
    path = []
    mapInfo = MapInfo(vac)
    while(len(mapInfo.dirtyRooms) > 0): #while there are still dirty rooms

        foundPath = interativeDeepeningSearch(mapInfo)

        a = 0
        for move in foundPath:
            if(a != 0): #just to skip the starting points, otherwise would suck twice on a dirty point
                path.append(move)
            a += 1

        mapInfo.startingLoc = path[len(path) - 1]
        index = 0
        for room in mapInfo.dirtyRooms:
            if(comparePoints(room, mapInfo.startingLoc) == True):
                break
            else:
                index += 1
        mapInfo.dirtyRooms.remove(mapInfo.dirtyRooms[index])

    return path

#Calculates the cost of a vaccum along a path
def calculateMoveSet(vac, path):
        tracer = vac.startingLoc
        dirtyRooms = findDirtyRooms(vac.map)
        moveSet = []
        for move in path:

            if(move[0] > tracer[0]):
                moveSet.append(("MoveDown", 0.7))
            if(move[0] < tracer[0]):
                moveSet.append(("MoveUp", 0.8))

            if(move[1] < tracer[1]):
                moveSet.append(("MoveLeft", 1.0))
            if(move[1] > tracer[1]):
                moveSet.append(("MoveRight", 0.9))
            
            for room in dirtyRooms:
                if(comparePoints(room, move)):
                    moveSet.append(("Suck", 0.6))

            

            tracer = move

        return moveSet


def calculateCost(moveSet):
    cost = 0
    for move in moveSet:
        cost += move[1]
    return cost


# TESTING!!!!
map = [[0 for i in range(5)] for j in range(4)]
map[0][1] = 1
map[1][0] = 1
map[1][3] = 1
map[2][2] = 1


vac = Vacuum(map, [2, 1], 0, 0, Node(map[2][2], 0, None))

path = findSolution(vac)

moveSet = calculateMoveSet(vac, path)

cost = calculateCost(moveSet)

print(moveSet)
print(cost)

