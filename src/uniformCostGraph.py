# Contains Uniform Cost Graph Search Algorithm

# Imports
from asyncio.windows_events import NULL
from math import dist
from vacuum import Vacuum
import numpy as np
from functions import *
from node import Node
from operator import attrgetter

# fringe = priority queue
    # format: Dict = {'distance from goal': [x-value, y-value]}
def uniformCostGraphSearch(vac, goalLoc):
    visited = np.array([])
    # goalLoc = [3, 3]

    # Populate fringe with expanded nodes from current node
    #fringe = Expand(vac)
    fringe = sorted(Expand(vac), key=attrgetter('pathCost'))
    # Sort fringe based on path cost
    #fringe.sort(key=lambda x: x.pathCost, reverse = True)
    
    count = 0

    while(len(fringe) != 0):
        node = fringe[0]
        fringe = np.delete(fringe, 0)
        if node.value == goalLoc:
            return node
        if node.value not in visited:
            print("\nAdded node to visited: ", node.value)
            visited = np.append(visited, node.value)
            vac.setCurrentNode(node)
            vac.setCurrentLoc(node.value)
            fringe = sorted(np.append(fringe, Expand(vac)), key=attrgetter('pathCost'))



# def InsertAll(successors, fringe):
    

# TESTING

map = [[0 for i in range(5)] for j in range(4)]
startingLoc = [0,0]
currentLoc = [1,1]  # [x-value, y-value]
currentScore = 0.0
stepCount = 0
node = Node([0,0], 0, 0, NULL)
vac = Vacuum(map, startingLoc, currentLoc, currentScore, stepCount, node)
vac.map[3][3] = 1

dirtyRooms = findDirtyRooms(vac.map)
print(dirtyRooms)
successors = Expand(vac)

dist = distanceFromGoal(vac.currentLoc, dirtyRooms)

print("Dist: ", dist)

# successors.sort(key=lambda x: x.pathCost, reverse = True)
# successors.sort(key=attrgetter('pathCost'), reverse = True)
newSuccessors = sorted(successors, key=attrgetter('pathCost'))
#  print(successors)
for x in newSuccessors:
    print(x.value, x.pathCost, x.depth)

popped = newSuccessors[0]
newSuccessors = np.delete(newSuccessors, 0)

print("Popped: ", popped.value)

for x in newSuccessors:
    print(x.value, x.pathCost, x.depth)

print(vac.currentNode.getChildrenValues())

testNode = Node([0, 0], 0, 0, NULL)
testVac = Vacuum([[0 for i in range(5)] for j in range(4)], [0,0], [0,0], 0, 0, testNode)
uniformCostGraphSearch(testVac, [3,3])