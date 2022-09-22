# Contains Uniform Cost Graph Search Algorithm

# Imports
from asyncio.windows_events import NULL
from math import dist
from vacuum import Vacuum
import numpy as np
from functions import *
from node import Node

# fringe = priority queue
    # format: Dict = {'distance from goal': [x-value, y-value]}
def uniformCostGraphSearch(vac, fringe):
    visited = {}

    fringe = Expand(vac)


    
    count = 0

    # Populate fringe

    #while(fringe):
    


# def InsertAll(successors, fringe):
    
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

#  print(successors)
for x in successors:
    print(x.value, x.pathCost, x.depth)

print(vac.currentNode.getChildrenValues())